# PathModuleTests

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

:::: 
::: 
``` 
   1 """ test_path.py - Test the path module.
   2 
   3 This only runs on Posix and NT right now.  I would like to have more
   4 tests.  You can help!  Just add appropriate pathnames for your
   5 platform (os.name) in each place where the p() function is called.
   6 Then send me the result.  If you can't get the test to run at all on
   7 your platform, there's probably a bug in path.py -- please let me
   8 know!
   9 
  10 TempDirTestCase.testTouch() takes a while to run.  It sleeps a few
  11 seconds to allow some time to pass between calls to check the modify
  12 time on files.
  13 
  14 URL:     http://www.jorendorff.com/articles/python/path
  15 Author:  Jason Orendorff <jason@jorendorff.com>
  16 Date:    7 Mar 2004
  17 Modified by Björn Lindqvist <bjourne@gmail.com>, January 2006
  18 """
  19 
  20 import unittest
  21 import codecs, os, random, shutil, tempfile, time
  22 from path import path, __version__ as path_version
  23 
  24 # This should match the version of path.py being tested.
  25 __version__ = '2.0.4'
  26 
  27 # Uncomment this to speed up testing. One test will fail.
  28 #time.sleep = lambda *args: None
  29 
  30 def p(**choices):
  31     """ Choose a value from several possible values, based on os.name """
  32     return choices[os.name]
  33 
  34 class BasicTestCase(unittest.TestCase):
  35     def testRelpath(self):
  36         root = path(p(nt='C:\\', posix='/'))
  37         foo = path(root, 'foo')
  38         quux = path(foo, 'quux')
  39         bar = path(foo, 'bar')
  40         boz = path(bar, 'Baz', 'Boz')
  41         up = path(os.pardir)
  42 
  43         # basics
  44         self.assertEqual(root.relpathto(boz),
  45                          path('foo', 'bar', 'Baz', 'Boz'))
  46         self.assertEqual(bar.relpathto(boz), path('Baz', 'Boz'))
  47         self.assertEqual(quux.relpathto(boz), path(up, 'bar', 'Baz', 'Boz'))
  48         self.assertEqual(boz.relpathto(quux), path(up, up, up, 'quux'))
  49         self.assertEqual(boz.relpathto(bar), path(up, up))
  50 
  51         # x.relpathto(x) == curdir
  52         self.assertEqual(root.relpathto(root), os.curdir)
  53         self.assertEqual(boz.relpathto(boz), os.curdir)
  54         # Make sure case is properly noted (or ignored)
  55         self.assertEqual(boz.relpathto(boz.normcase()), os.curdir)
  56 
  57         # relpath()
  58         cwd = path(os.getcwd())
  59         self.assertEqual(boz.relpath(), cwd.relpathto(boz))
  60 
  61         if os.name == 'nt':
  62             # Check relpath across drives.
  63             d = path('D:\\')
  64             self.assertEqual(d.relpathto(boz), boz)
  65 
  66     def testStringCompatibility(self):
  67         """ Test compatibility with ordinary strings. """
  68         x = path('xyzzy')
  69         self.assert_(x == 'xyzzy')
  70         self.assert_(x == u'xyzzy')
  71 
  72         # sorting
  73         items = [path('fhj'),
  74                  path('fgh'),
  75                  'E',
  76                  path('d'),
  77                  'A',
  78                  path('B'),
  79                  'c']
  80         items.sort()
  81         self.assert_(items == ['A', 'B', 'E', 'c', 'd', 'fgh', 'fhj'])
  82 
  83     def testProperties(self):
  84         # Create sample path object.
  85         f = p(nt='C:\\Program Files\\Python\\Lib\\xyzzy.py',
  86               posix='/usr/local/python/lib/xyzzy.py')
  87         f = path(f)
  88 
  89         # .parent
  90         self.assertEqual(f.parent, p(nt='C:\\Program Files\\Python\\Lib',
  91                                      posix='/usr/local/python/lib'))
  92 
  93         # .name
  94         self.assertEqual(f.name, 'xyzzy.py')
  95         self.assertEqual(f.parent.name, p(nt='Lib', posix='lib'))
  96 
  97         # .ext
  98         self.assertEqual(f.ext, '.py')
  99         self.assertEqual(f.parent.ext, '')
 100 
 101         # .drive
 102         self.assertEqual(f.drive, p(nt='C:', posix=''))
 103 
 104     def testMethods(self):
 105         # .abspath()
 106         self.assertEqual(path(os.curdir).abspath(), os.getcwd())
 107 
 108         # .getcwd()
 109         cwd = path.cwd()
 110         self.assert_(isinstance(cwd, path))
 111         self.assertEqual(cwd, os.getcwd())
 112 
 113     def testUNC(self):
 114         if hasattr(os.path, 'splitunc'):
 115             p = path(r'\\python1\share1\dir1\file1.txt')
 116             self.assert_(p.uncshare == r'\\python1\share1')
 117             self.assert_(p.splitunc() == os.path.splitunc(str(p)))
 118 
 119     def testDefaultCtor(self):
 120         self.assert_(os.getcwd() == path().abspath())
 121 
 122         # On most platforms, current working directory is "."
 123         self.assert_(path() == ".")
 124 
 125         # But that is different from os.getcwd()...
 126         self.assert_(path() != path().cwd())
 127 
 128     def testSplittingAndStripping(self):
 129         p = path("~/python/config.h.in")
 130         noext = p.stripext()
 131         self.assert_(isinstance(p, path))
 132         self.assertEquals(noext, "~/python/config.h")
 133 
 134     def testTimeProperties(self):
 135         p = path("tempfile")
 136         p.touch()
 137         now = int(time.time())
 138         self.assertEquals(p.ctime(), now)
 139         self.assertEquals(p.mtime(), now)
 140         self.assertEquals(p.atime(), now)
 141 
 142 
 143 class TempDirTestCase(unittest.TestCase):
 144     def setUp(self):
 145         # Create a temporary directory.
 146         f = tempfile.mktemp()
 147         system_tmp_dir = os.path.dirname(f)
 148         my_dir = 'testpath_tempdir_' + str(random.random())[2:]
 149         self.tempdir = os.path.join(system_tmp_dir, my_dir)
 150         os.mkdir(self.tempdir)
 151 
 152     def tearDown(self):
 153         shutil.rmtree(self.tempdir)
 154 
 155     def testTouch(self):
 156         # NOTE: This test takes a long time to run (~10 seconds).
 157         # It sleeps several seconds because on Windows, the resolution
 158         # of a file's mtime and ctime is about 2 seconds.
 159         #
 160         # atime isn't tested because on Windows the resolution of atime
 161         # is something like 24 hours.
 162 
 163         d = path(self.tempdir)
 164         f = path(d, 'test.txt')
 165         t0 = time.time() - 3
 166         f.touch()
 167         t1 = time.time() + 3
 168         try:
 169             self.assert_(f.exists())
 170             self.assert_(f.isfile())
 171             self.assertEqual(f.size(), 0)
 172             self.assert_(t0 <= f.mtime <= t1)
 173             ct = f.ctime
 174             self.assert_(t0 <= ct <= t1)
 175 
 176             time.sleep(5)
 177             fobj = file(f, 'ab')
 178             fobj.write('some bytes')
 179             fobj.close()
 180 
 181             time.sleep(5)
 182             t2 = time.time() - 3
 183             f.touch()
 184             t3 = time.time() + 3
 185 
 186             assert t0 <= t1 < t2 <= t3  # sanity check
 187 
 188             self.assert_(f.exists())
 189             self.assert_(f.isfile())
 190             self.assertEqual(f.size(), 10)
 191             self.assert_(t2 <= f.mtime <= t3)
 192             if hasattr(os.path, 'getctime'):
 193                 ct2 = f.ctime
 194                 if os.name == 'nt':
 195                     # On Windows, "ctime" is CREATION time
 196                     self.assertEqual(ct, ct2)
 197                     self.assert_(ct2 < t2)
 198                 else:
 199                     # On other systems, it might be the CHANGE time 
 200                     # (especially on Unix, time of inode changes)
 201                     self.failUnless(ct == ct2 or ct2 == f.mtime)
 202         finally:
 203             f.remove()
 204 
 205     def testListing(self):
 206         d = path(self.tempdir)
 207         self.assertEqual(d.listdir(), [])
 208         
 209         f = 'testfile.txt'
 210         af = path(d, f)
 211         self.assertEqual(af, os.path.join(d, f))
 212         af.touch()
 213         try:
 214             self.assert_(af.exists())
 215 
 216             self.assertEqual(d.listdir(), [af])
 217 
 218             # .glob()
 219             self.assertEqual(d.glob('testfile.txt'), [af])
 220             self.assertEqual(d.glob('test*.txt'), [af])
 221             self.assertEqual(d.glob('*.txt'), [af])
 222             self.assertEqual(d.glob('*txt'), [af])
 223             self.assertEqual(d.glob('*'), [af])
 224             self.assertEqual(d.glob('*.html'), [])
 225             self.assertEqual(d.glob('testfile'), [])
 226         finally:
 227             af.remove()
 228 
 229         # Try a test with 20 files
 230         files = [path(d, '%d.txt' % i) for i in range(20)]
 231         for f in files:
 232             fobj = file(f, 'w')
 233             fobj.write('some text\n')
 234             fobj.close()
 235         try:
 236             files2 = d.listdir()
 237             files.sort()
 238             files2.sort()
 239             self.assertEqual(files, files2)
 240         finally:
 241             for f in files:
 242                 try:
 243                     f.remove()
 244                 except:
 245                     pass
 246 
 247     def testMakeDirs(self):
 248         d = path(self.tempdir)
 249 
 250         # Placeholder file so that when removedirs() is called,
 251         # it doesn't remove the temporary directory itself.
 252         tempf = path(d, 'temp.txt')
 253         tempf.touch()
 254         try:
 255             foo = path(d, 'foo')
 256             boz = path(foo, 'bar', 'baz', 'boz')
 257             boz.makedirs()
 258             try:
 259                 self.assert_(boz.isdir())
 260             finally:
 261                 boz.removedirs()
 262             self.failIf(foo.exists())
 263             self.assert_(d.exists())
 264 
 265             foo.mkdir(0750)
 266             boz.makedirs(0700)
 267             try:
 268                 self.assert_(boz.isdir())
 269             finally:
 270                 boz.removedirs()
 271             self.failIf(foo.exists())
 272             self.assert_(d.exists())
 273         finally:
 274             os.remove(tempf)
 275 
 276     def assertSetsEqual(self, a, b):
 277         ad = {}
 278         for i in a: ad[i] = None
 279         bd = {}
 280         for i in b: bd[i] = None
 281         self.assertEqual(ad, bd)
 282 
 283     def testShutil(self):
 284         # Note: This only tests the methods exist and do roughly what
 285         # they should, neglecting the details as they are shutil's
 286         # responsibility.
 287 
 288         d = path(self.tempdir)
 289         testDir = path(d, 'testdir')
 290         testFile = path(testDir, 'testfile.txt')
 291         testA = path(testDir, 'A')
 292         testCopy = path(testA, 'testcopy.txt')
 293         testLink = path(testA, 'testlink.txt')
 294         testB = path(testDir, 'B')
 295         testC = path(testB, 'C')
 296         testCopyOfLink = path(testC, testA.relpathto(testLink))
 297 
 298         # Create test dirs and a file
 299         testDir.mkdir()
 300         testA.mkdir()
 301         testB.mkdir()
 302 
 303         f = open(testFile, 'w')
 304         f.write('x' * 10000)
 305         f.close()
 306 
 307         # Test simple file copying.
 308         testFile.copyfile(testCopy)
 309         self.assert_(testCopy.isfile())
 310 
 311         # Test copying into a directory.
 312         testCopy2 = path(testA, testFile.name)
 313         testFile.copy(testA)
 314         self.assert_(testCopy2.isfile())
 315 
 316         # Make a link for the next test to use.
 317         if hasattr(os, 'symlink'):
 318             testFile.symlink(testLink)
 319         else:
 320             testFile.copy(testLink)  # fallback
 321 
 322         # Test copying directory tree.
 323         testA.copytree(testC)
 324         self.assert_(testC.isdir())
 325         self.assertSetsEqual(
 326             testC.listdir(),
 327             [path(testC, testCopy.name),
 328              path(testC, testFile.name),
 329              testCopyOfLink])
 330         self.assert_(not testCopyOfLink.islink())
 331 
 332         # Clean up for another try.
 333         testC.rmtree()
 334         self.assert_(not testC.exists())
 335 
 336         # Copy again, preserving symlinks.
 337         testA.copytree(testC, True)
 338         self.assert_(testC.isdir())
 339         self.assertSetsEqual(
 340             testC.listdir(),
 341             [path(testC, testCopy.name),
 342              path(testC, testFile.name),
 343              testCopyOfLink])
 344         if hasattr(os, 'symlink'):
 345             self.assert_(testCopyOfLink.islink())
 346             self.assert_(testCopyOfLink.readlink() == testFile)
 347 
 348         # Clean up.
 349         testDir.rmtree()
 350         self.assert_(not testDir.exists())
 351         self.assertList(d.listdir(), [])
 352 
 353     def assertList(self, listing, expected):
 354         listing = list(listing)
 355         listing.sort()
 356         expected = list(expected)
 357         expected.sort()
 358         self.assertEqual(listing, expected)
 359 
 360     def testPatterns(self):
 361         d = path(self.tempdir)
 362         names = [ 'x.tmp', 'x.xtmp', 'x2g', 'x22', 'x.txt' ]
 363         dirs = [d, path(d, 'xdir'), path(d, 'xdir.tmp'),
 364                 path(d, 'xdir.tmp', 'xsubdir')]
 365 
 366         for e in dirs:
 367             if not e.isdir():
 368                 e.makedirs()
 369             for name in names:
 370                 path(e, name).touch()
 371         self.assertList(d.listdir('*.tmp'), [path(d, 'x.tmp'),
 372                                              path(d, 'xdir.tmp')])
 373         self.assertList(d.files('*.tmp'), [path(d, 'x.tmp')])
 374         self.assertList(d.dirs('*.tmp'), [path(d, 'xdir.tmp')])
 375         self.assertList(d.walk(),
 376                         [e for e in dirs if e != d] +
 377                         [path(e, n) for e in dirs for n in names])
 378         self.assertList(d.walk('*.tmp'),
 379                         [path(e, 'x.tmp') for e in dirs] +
 380                         [path(d, 'xdir.tmp')])
 381         self.assertList(d.walkfiles('*.tmp'),
 382                         [path(e, 'x.tmp') for e in dirs])
 383         self.assertList(d.walkdirs('*.tmp'), [path(d, 'xdir.tmp')])
 384 
 385         self.assert_(path("/foobar/file.png").match("*.png"))
 386         self.assert_(not path("/foobar/FILE.PNG").matchcase("*.png"))
 387                      
 388 
 389 
 390 if __name__ == '__main__':
 391     if __version__ != path_version:
 392         print ("Version mismatch:  test_path.py version %s, path version %s" %
 393                (__version__, path_version))
 394     unittest.main()
```
:::
::::
