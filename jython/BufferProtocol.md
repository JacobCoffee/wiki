# BufferProtocol

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Buffer Protocol 

This page proposes (now begins to document) a design for a Jython equivalent to the CPython buffer protocol. A good place to start is this [worked example (pdf)](attachments/BufferProtocol/buffer_api_model.pdf "worked example (pdf)") that motivated the current design.

## What is the Buffer API? 

The Jython Buffer API is an interface you can use in Java when accessing or implementing certain built-in types, or your own. It is the basis of the type `memoryview`{.backtick} with which it shares many features.

In CPython, certain objects are based on an underlying memory array or buffer. The CPython designers judged it desirable to be able to access that buffer directly, without intermediate copying. CPython provides this at the C level in the form of the *buffer protocol*. This is used heavily in the implementation of some core types and standard library modules.

The capability is just as useful in Jython, and has been implemented for version 2.7.

## Accessing an Object that has the Buffer API 

Objects flag their willingness to provide a buffer by implementing the following interface:

:::: 
::: 
``` 
   1 public interface BufferProtocol {
   2     Buffer getBuffer(int flags);   
   3 }
```
:::
::::

Here is a simple example of the API used, adapted from the implementation of `bytearray`{.backtick}:

:::: 
::: 
``` 
   1     protected void init(BufferProtocol value) throws PyException {
   2         // Get the buffer view
   3         try (PyBuffer view = value.getBuffer(PyBUF.FULL_RO)) {
   4             // Create storage for the bytes
   5             this.storage = new byte[view.getLen()];
   6             this.size = storage.length;
   7             this.offset = 0
   8             // Have the view drop them in
   9             view.copyTo(this.storage, this.offset);
  10         }
  11     }
```
:::
::::

The reason for the try-with-resources construct is to ensure the view is released when the client has finished with it. (Some objects change behaviour for the lifetime of the exported view. Notably, a `bytearray`{.backtick} cannot be resized while exporting.)

The `flags`{.backtick} argument indicates the buffer characteristics wanted by the consumer, and what kind of data organisation the consumer can cope with. The return is an implementation of `PyBuffer`{.backtick} appropriate to the storage organisation of the exporter. In the example, the consumer says it can cope with any organisation (FULL), but that it will only be reading (RO).

The business about exporter storage organisation is only relevant if you are going to access the actual byte array. Here, the client says it can cope with any organisation, because it is only going to use the buffer\'s own `copyTo`{.backtick} method. Every buffer implementation has to understand its own storage and provide `copyTo`{.backtick}, `charAt`{.backtick}, `storeAt`{.backtick}, and several other methods.

This interface is quite rich, but the Javadoc is thorough. In fact, the interface is defined in two stages: a part that is independent of the type of unit in the buffer, and a part that is definite that the units are `byte`{.backtick}s.

The type-agnostic part of the interface is `PyBUF`{.backtick}:

:::: 
::: 
``` 
   1 public interface PyBUF {
   2 
   3     boolean isReadonly();
   4 
   5     // Access to buffer (client responsible for indexing)
   6     int getNdim();
   7     int[] getShape();
   8     int getItemsize();
   9     int getLen();
  10     int[] getStrides();
  11     int[] getSuboffsets();
  12     boolean isContiguous(char order);
  13 
  14     // Constants taken from CPython object.h in v3.3
  15     static final int MAX_NDIM = 64;
  16     static final int WRITABLE = 0x0001;
  17     static final int SIMPLE = 0;
  18     static final int FORMAT = 0x0004;
  19     static final int ND = 0x0008;
  20     static final int STRIDES = 0x0010 | ND;
  21     static final int C_CONTIGUOUS = 0x0020 | STRIDES;
  22     static final int F_CONTIGUOUS = 0x0040 | STRIDES;
  23     static final int ANY_CONTIGUOUS = 0x0080 | STRIDES;
  24     static final int INDIRECT = 0x0100 | STRIDES;
  25     static final int CONTIG = ND | WRITABLE;
  26     static final int CONTIG_RO = ND;
  27     static final int STRIDED = STRIDES | WRITABLE;
  28     static final int STRIDED_RO = STRIDES;
  29     static final int RECORDS = STRIDES | WRITABLE | FORMAT;
  30     static final int RECORDS_RO = STRIDES | FORMAT;
  31     static final int FULL = INDIRECT | WRITABLE | FORMAT;
  32     static final int FULL_RO = INDIRECT | FORMAT;
  33     static final int NAVIGATION = SIMPLE | ND | STRIDES | INDIRECT;
  34     static final int IS_C_CONTIGUOUS = C_CONTIGUOUS & ~STRIDES;
  35     static final int IS_F_CONTIGUOUS = F_CONTIGUOUS & ~STRIDES;
  36     static final int CONTIGUITY = (C_CONTIGUOUS | F_CONTIGUOUS | ANY_CONTIGUOUS) & ~STRIDES;
  37 }
```
:::
::::

The byte-oriented part of the interface is `PyBuffer`{.backtick}. For the most part, you can ignore the difference between `PyBUF`{.backtick} and `PyBuffer`{.backtick} and think of all the methods as belonging to `PyBuffer`{.backtick}:

:::: 
::: 
``` 
   1 public interface PyBuffer extends PyBUF, BufferProtocol, AutoCloseable {
   2 
   3     // Access to buffer contents (index calculation done by buffer)
   4     byte byteAt(int index) throws IndexOutOfBoundsException;
   5     int intAt(int index) throws IndexOutOfBoundsException;
   6     void storeAt(byte value, int index) throws IndexOutOfBoundsException;
   7     byte byteAt(int... indices) throws IndexOutOfBoundsException;
   8     int intAt(int... indices) throws IndexOutOfBoundsException;
   9     void storeAt(byte value, int... indices) throws IndexOutOfBoundsException;
  10 
  11     // Bulk operations (index calculation done by buffer)
  12     void copyTo(byte[] dest, int destPos);
  13     void copyTo(int srcIndex, byte[] dest, int destPos, int length);
  14     void copyFrom(byte[] src, int srcPos, int destIndex, int length);
  15     void copyFrom(PyBuffer src);
  16 
  17     // Releasing a buffer or getting another (or a slice)
  18     void release();
  19     void close(); // Alias for release()
  20     boolean isReleased();
  21     @Override PyBuffer getBuffer(int flags); // from BufferProtocol
  22     public PyBuffer getBufferSlice(int flags, int start, int length);
  23     public PyBuffer getBufferSlice(int flags, int start, int length, int stride);
  24 
  25     // Access to buffer (client responsible for indexing)
  26     public static class Pointer {
  27         public byte[] storage;
  28         public int offset;
  29         public Pointer(byte[] storage, int offset) {
  30             this.storage = storage;
  31             this.offset = offset;
  32         }
  33     }
  34 
  35     PyBuffer.Pointer getBuf();
  36     PyBuffer.Pointer getPointer(int index);
  37     PyBuffer.Pointer getPointer(int... indices);
  38 
  39     // Interpreting the bytes
  40     String getFormat();
  41 }
```
:::
::::

Notice that an object that implements `PyBuffer`{.backtick} must itself implement the `BufferProtocol`{.backtick}. A buffer can give you a buffer, which may just be itself or could be an independent object, depending on the implementation.

Note that `PyBuffer`{.backtick} extends the `AutoCloseable`{.backtick} interface, so that you can use the try-with-resources construct to manage buffer lifetime. (This was added shortly after Java 7 became the minimum platform.)

## Adding the Buffer API to an Object 

The core package org.python.core only defines the interfaces. Several `PyBuffer`{.backtick} implementations that could be exported by object implementations are provided in `org.python.core.buffer`{.backtick}. The place to start is with one of these basic types:

::: {}
  ---------------------- ----------------------------------
  **Buffer Type**        **Suitable for \...**
  SimpleBuffer           read-only 1D array of bytes
  SimpleWritableBuffer   1D array of bytes
  SimpleStringBuffer     Java String (representing bytes)
  ---------------------- ----------------------------------
:::

These could all be extended or for a more sophisticated behaviour, consider extending `BaseBuffer`{.backtick}.

## Converting from CPython 

### Similarities with CPython 

- The navigational arrays (`shape`{.backtick}, `strides`{.backtick}, `suboffsets`{.backtick}) and `format`{.backtick}, `unitsize`{.backtick} are present with the same meanings.

- The \"request flags\" have the same values, with similar names `PyBUF.STRIDED`{.backtick} in place of `PyBUF_STRIDED`{.backtick}.

- The discipline of matching `get`{.backtick} and `release`{.backtick} applies also in Jython.

### Differences from CPython 

- `PyBuffer`{.backtick} is a Java interface: quantities that were struct members become `getXXX()`{.backtick} methods.

- `PyBuffer`{.backtick} always supplies full information (`shape`{.backtick}, `strides`{.backtick}, `format`{.backtick}).

- The different buffer organisations are expressed through different classes implementing the interface.

- Library functions taking `PyObject`{.backtick} or `PyBuffer`{.backtick} arguments in CPython become methods on those types.

- A `PyBuffer`{.backtick} manages the get-release accounting for exporters.

- And you have try-with-resources to help you keep your end of the bargain.

- Wherever CPython uses a `char*`{.backtick} pointer, Jython reference a buffer of bytes and an offset within it.
