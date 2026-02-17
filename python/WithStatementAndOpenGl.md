# WithStatementAndOpenGl

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

(I think you should bring this up in the [OpenGl](./OpenGl.html) community; if the with-statement supports the usage I don\'t see why not. [GvR](GvR))

(Doing so. \-- Andrew Dalke)

OpenGL programmers have complained about using Python because the code indentation doesn\'t follow the display tree. For an example pulled from one of my (Andrew Dalke) projects

            glBegin(GL_QUAD_STRIP)
            glColor3f(1.0,1.0,1.0) #corner 1
            glNormal3f(0.57735027, 0.57735027, 0.57735027)
            glVertex3f(0.5, 0.5, 0.5)
            glColor3f(1.0,0.0,1.0) #corner 2
            glNormal3f(0.57735027, -0.57735027, 0.57735027)
            glVertex3f(0.5, -0.5, 0.5)
            ...
            glEnd()

Some people write this as some variant of

            glBegin(GL_QUAD_STRIP)
            if 1:
              glColor3f(1.0,1.0,1.0) #corner 1
              glNormal3f(0.57735027, 0.57735027, 0.57735027)
              glVertex3f(0.5, 0.5, 0.5)
              glColor3f(1.0,0.0,1.0) #corner 2
              glNormal3f(0.57735027, -0.57735027, 0.57735027)
              glVertex3f(0.5, -0.5, 0.5)
              ...
            glEnd()

and sometimes using try/finally so that errors don\'t cause the gl state to become corrupted.

Would an appropriate use of this proposal be to allow

      with QUAD_STRIP:
          glColor3f(1.0,1.0,1.0) #corner 1
          glNormal3f(0.57735027, 0.57735027, 0.57735027)
          glVertex3f(0.5, 0.5, 0.5)
          glColor3f(1.0,0.0,1.0) #corner 2
          glNormal3f(0.57735027, -0.57735027, 0.57735027)
          glVertex3f(0.5, -0.5, 0.5)
          ....

where there are a bunch of small classes for each of the possible glBegins, such as

    class QUAD_STRIP:
      @staticmethod
      def __enter__():
        glBegin(GL_QUAD_STRIP)
      @staticmethod
      def __exit__(*args):
        glEnd()

If so, I rather like that ability as it makes the graphics programmer\'s intent clearer and prevents problems balancing glBegin and glEnd - even in the face of code errors in the actual code block! \-- Andrew Dalke

------------------------------------------------------------------------

I\'m (Andrew Dalke) often one to resist change to Python. The [WithStatement](WithStatement) is a counter-example. I really like how it cleans up some OpenGL programming. Consider this example from OpenGLContext\'s indexlineset.py

               dl = displaylist.DisplayList()
               ...
               # compile the color-friendly ILS
               dl.start()
               try:
                   glEnable( GL_COLOR_MATERIAL )
                   for polyline, color in zip(indices, colorIndices):
                       if type(color) == int:
                           glColor3d( *colors[color] )
                           glBegin( GL_LINE_STRIP )
                           try:
                               for i in polyline:
                                   glVertex3f(*points[i])
                           finally:
                               glEnd()
                        else:
                           glBegin( GL_LINE_STRIP )
                           try:
                               for i,c in zip(polyline, color):
                                   glColor3d( *colors[c] )
                                   glVertex3f(*points[i])
                           finally:
                                glEnd()
                   glDisable( GL_COLOR_MATERIAL )
               finally:
                   dl.end()

Assuming a few minor helper classes and a couple of new `__enter__/__exit__` methods and it can be rewritten using \'with\' statements like this:

               dl = displaylist.DisplayList()
               ...
               with dl:
                   with GLEnable( GL_COLOR_MATERIAL ):
                       for polyline, color in zip(indices, colorIndices):
                           if type(color) == int:
                               glColor3d( *colors[color] )
                           with GLGeometry( GL_LINE_STRIP ):
                               for i in polyline:
                                   glVertex3f(*points[i])
                        else:
                           with GLBegin( GL_LINE_STRIP ):
                               for i,c in zip(polyline, color):
                                   glColor3d( *colors[c] )
                                   glVertex3f(*points[i])

Shorter, cleaner, less error-prone, easier to read and maintain. +1 from me! \-- Andrew Dalke
