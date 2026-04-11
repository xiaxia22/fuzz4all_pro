# Class BufferStrategy

**Source:** `java.desktop\java\awt\image\BufferStrategy.html`

### Class Description

```java
public abstract class
BufferStrategy

extends
Object
```

The

BufferStrategy

class represents the mechanism with which
to organize complex memory on a particular

Canvas

or

Window

. Hardware and software limitations determine whether and
how a particular buffer strategy can be implemented. These limitations
are detectable through the capabilities of the

GraphicsConfiguration

used when creating the

Canvas

or

Window

.

It is worth noting that the terms

buffer

and

surface

are meant
to be synonymous: an area of contiguous memory, either in video device
memory or in system memory.

There are several types of complex buffer strategies, including
sequential ring buffering and blit buffering.
Sequential ring buffering (i.e., double or triple
buffering) is the most common; an application draws to a single

back
buffer

and then moves the contents to the front (display) in a single
step, either by copying the data or moving the video pointer.
Moving the video pointer exchanges the buffers so that the first buffer
drawn becomes the

front buffer

, or what is currently displayed on the
device; this is called

page flipping

.

Alternatively, the contents of the back buffer can be copied, or

blitted

forward in a chain instead of moving the video pointer.

```java
Double buffering:

*********** ***********
* * ------> * *
[To display] <---- * Front B * Show * Back B. * <---- Rendering
* * <------ * *
*********** ***********

Triple buffering:

[To *********** *********** ***********
display] * * --------+---------+------> * *
<---- * Front B * Show * Mid. B. * * Back B. * <---- Rendering
* * <------ * * <----- * *
*********** *********** ***********
```

Here is an example of how buffer strategies can be created and used:

```java
// Check the capabilities of the GraphicsConfiguration
...

// Create our component
Window w = new Window(gc);

// Show our window
w.setVisible(true);

// Create a general double-buffering strategy
w.createBufferStrategy(2);
BufferStrategy strategy = w.getBufferStrategy();

// Main loop
while (!done) {
// Prepare for rendering the next frame
// ...

// Render single frame
do {
// The following loop ensures that the contents of the drawing buffer
// are consistent in case the underlying surface was recreated
do {
// Get a new graphics context every time through the loop
// to make sure the strategy is validated
Graphics graphics = strategy.getDrawGraphics();

// Render to graphics
// ...

// Dispose the graphics
graphics.dispose();

// Repeat the rendering if the drawing buffer contents
// were restored
} while (strategy.contentsRestored());

// Display the buffer
strategy.show();

// Repeat the rendering if the drawing buffer was lost
} while (strategy.contentsLost());
}

// Dispose the window
w.setVisible(false);
w.dispose();
```

**Direct Known Subclasses:** Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

### Field Details

*No entries found.*

### Constructor Details

#### public BufferStrategy()

*No description found.*

---

### Method Details

#### public abstract
BufferCapabilities
getCapabilities()

Returns the

BufferCapabilities

for this

BufferStrategy

.

**Returns:**
- the buffering capabilities of this strategy

---

#### public abstract
Graphics
getDrawGraphics()

Creates a graphics context for the drawing buffer. This method may not
be synchronized for performance reasons; use of this method by multiple
threads should be handled at the application level. Disposal of the
graphics object obtained must be handled by the application.

**Returns:**
- a graphics context for the drawing buffer

---

#### public abstract boolean contentsLost()

Returns whether the drawing buffer was lost since the last call to

getDrawGraphics

. Since the buffers in a buffer strategy
are usually type

VolatileImage

, they may become lost.
For a discussion on lost buffers, see

VolatileImage

.

**Returns:**
- Whether or not the drawing buffer was lost since the last call
to

getDrawGraphics

.

**See Also:**
- VolatileImage

---

#### public abstract boolean contentsRestored()

Returns whether the drawing buffer was recently restored from a lost
state and reinitialized to the default background color (white).
Since the buffers in a buffer strategy are usually type

VolatileImage

, they may become lost. If a surface has
been recently restored from a lost state since the last call to

getDrawGraphics

, it may require repainting.
For a discussion on lost buffers, see

VolatileImage

.

**Returns:**
- Whether or not the drawing buffer was restored since the last
call to

getDrawGraphics

.

**See Also:**
- VolatileImage

---

#### public abstract void show()

Makes the next available buffer visible by either copying the memory
(blitting) or changing the display pointer (flipping).

---

#### public void dispose()

Releases system resources currently consumed by this

BufferStrategy

and
removes it from the associated Component. After invoking this
method,

getBufferStrategy

will return null. Trying
to use a

BufferStrategy

after it has been disposed will
result in undefined behavior.

**See Also:**
- Window.createBufferStrategy(int)

,

Canvas.createBufferStrategy(int)

,

Window.getBufferStrategy()

,

Canvas.getBufferStrategy()

**Since:**
- 1.6

---

### Additional Sections

#### Class BufferStrategy

java.lang.Object

- java.awt.image.BufferStrategy

java.awt.image.BufferStrategy

**Direct Known Subclasses:** Component.BltBufferStrategy

,

Component.FlipBufferStrategy

```java
public abstract class
BufferStrategy

extends
Object
```

The

BufferStrategy

class represents the mechanism with which
to organize complex memory on a particular

Canvas

or

Window

. Hardware and software limitations determine whether and
how a particular buffer strategy can be implemented. These limitations
are detectable through the capabilities of the

GraphicsConfiguration

used when creating the

Canvas

or

Window

.

It is worth noting that the terms

buffer

and

surface

are meant
to be synonymous: an area of contiguous memory, either in video device
memory or in system memory.

There are several types of complex buffer strategies, including
sequential ring buffering and blit buffering.
Sequential ring buffering (i.e., double or triple
buffering) is the most common; an application draws to a single

back
buffer

and then moves the contents to the front (display) in a single
step, either by copying the data or moving the video pointer.
Moving the video pointer exchanges the buffers so that the first buffer
drawn becomes the

front buffer

, or what is currently displayed on the
device; this is called

page flipping

.

Alternatively, the contents of the back buffer can be copied, or

blitted

forward in a chain instead of moving the video pointer.

```java
Double buffering:

*********** ***********
* * ------> * *
[To display] <---- * Front B * Show * Back B. * <---- Rendering
* * <------ * *
*********** ***********

Triple buffering:

[To *********** *********** ***********
display] * * --------+---------+------> * *
<---- * Front B * Show * Mid. B. * * Back B. * <---- Rendering
* * <------ * * <----- * *
*********** *********** ***********
```

Here is an example of how buffer strategies can be created and used:

```java
// Check the capabilities of the GraphicsConfiguration
...

// Create our component
Window w = new Window(gc);

// Show our window
w.setVisible(true);

// Create a general double-buffering strategy
w.createBufferStrategy(2);
BufferStrategy strategy = w.getBufferStrategy();

// Main loop
while (!done) {
// Prepare for rendering the next frame
// ...

// Render single frame
do {
// The following loop ensures that the contents of the drawing buffer
// are consistent in case the underlying surface was recreated
do {
// Get a new graphics context every time through the loop
// to make sure the strategy is validated
Graphics graphics = strategy.getDrawGraphics();

// Render to graphics
// ...

// Dispose the graphics
graphics.dispose();

// Repeat the rendering if the drawing buffer contents
// were restored
} while (strategy.contentsRestored());

// Display the buffer
strategy.show();

// Repeat the rendering if the drawing buffer was lost
} while (strategy.contentsLost());
}

// Dispose the window
w.setVisible(false);
w.dispose();
```

**Since:** 1.4
**See Also:** Window

,

Canvas

,

GraphicsConfiguration

,

VolatileImage

public abstract class

BufferStrategy

extends

Object

The

BufferStrategy

class represents the mechanism with which
to organize complex memory on a particular

Canvas

or

Window

. Hardware and software limitations determine whether and
how a particular buffer strategy can be implemented. These limitations
are detectable through the capabilities of the

GraphicsConfiguration

used when creating the

Canvas

or

Window

.

It is worth noting that the terms

buffer

and

surface

are meant
to be synonymous: an area of contiguous memory, either in video device
memory or in system memory.

There are several types of complex buffer strategies, including
sequential ring buffering and blit buffering.
Sequential ring buffering (i.e., double or triple
buffering) is the most common; an application draws to a single

back
buffer

and then moves the contents to the front (display) in a single
step, either by copying the data or moving the video pointer.
Moving the video pointer exchanges the buffers so that the first buffer
drawn becomes the

front buffer

, or what is currently displayed on the
device; this is called

page flipping

.

Alternatively, the contents of the back buffer can be copied, or

blitted

forward in a chain instead of moving the video pointer.

```java
Double buffering:

*********** ***********
* * ------> * *
[To display] <---- * Front B * Show * Back B. * <---- Rendering
* * <------ * *
*********** ***********

Triple buffering:

[To *********** *********** ***********
display] * * --------+---------+------> * *
<---- * Front B * Show * Mid. B. * * Back B. * <---- Rendering
* * <------ * * <----- * *
*********** *********** ***********
```

Here is an example of how buffer strategies can be created and used:

```java
// Check the capabilities of the GraphicsConfiguration
...

// Create our component
Window w = new Window(gc);

// Show our window
w.setVisible(true);

// Create a general double-buffering strategy
w.createBufferStrategy(2);
BufferStrategy strategy = w.getBufferStrategy();

// Main loop
while (!done) {
// Prepare for rendering the next frame
// ...

// Render single frame
do {
// The following loop ensures that the contents of the drawing buffer
// are consistent in case the underlying surface was recreated
do {
// Get a new graphics context every time through the loop
// to make sure the strategy is validated
Graphics graphics = strategy.getDrawGraphics();

// Render to graphics
// ...

// Dispose the graphics
graphics.dispose();

// Repeat the rendering if the drawing buffer contents
// were restored
} while (strategy.contentsRestored());

// Display the buffer
strategy.show();

// Repeat the rendering if the drawing buffer was lost
} while (strategy.contentsLost());
}

// Dispose the window
w.setVisible(false);
w.dispose();
```

It is worth noting that the terms

buffer

and

surface

are meant
to be synonymous: an area of contiguous memory, either in video device
memory or in system memory.

There are several types of complex buffer strategies, including
sequential ring buffering and blit buffering.
Sequential ring buffering (i.e., double or triple
buffering) is the most common; an application draws to a single

back
buffer

and then moves the contents to the front (display) in a single
step, either by copying the data or moving the video pointer.
Moving the video pointer exchanges the buffers so that the first buffer
drawn becomes the

front buffer

, or what is currently displayed on the
device; this is called

page flipping

.

Alternatively, the contents of the back buffer can be copied, or

blitted

forward in a chain instead of moving the video pointer.

```java
Double buffering:

*********** ***********
* * ------> * *
[To display] <---- * Front B * Show * Back B. * <---- Rendering
* * <------ * *
*********** ***********

Triple buffering:

[To *********** *********** ***********
display] * * --------+---------+------> * *
<---- * Front B * Show * Mid. B. * * Back B. * <---- Rendering
* * <------ * * <----- * *
*********** *********** ***********
```

Here is an example of how buffer strategies can be created and used:

```java
// Check the capabilities of the GraphicsConfiguration
...

// Create our component
Window w = new Window(gc);

// Show our window
w.setVisible(true);

// Create a general double-buffering strategy
w.createBufferStrategy(2);
BufferStrategy strategy = w.getBufferStrategy();

// Main loop
while (!done) {
// Prepare for rendering the next frame
// ...

// Render single frame
do {
// The following loop ensures that the contents of the drawing buffer
// are consistent in case the underlying surface was recreated
do {
// Get a new graphics context every time through the loop
// to make sure the strategy is validated
Graphics graphics = strategy.getDrawGraphics();

// Render to graphics
// ...

// Dispose the graphics
graphics.dispose();

// Repeat the rendering if the drawing buffer contents
// were restored
} while (strategy.contentsRestored());

// Display the buffer
strategy.show();

// Repeat the rendering if the drawing buffer was lost
} while (strategy.contentsLost());
}

// Dispose the window
w.setVisible(false);
w.dispose();
```

There are several types of complex buffer strategies, including
sequential ring buffering and blit buffering.
Sequential ring buffering (i.e., double or triple
buffering) is the most common; an application draws to a single

back
buffer

and then moves the contents to the front (display) in a single
step, either by copying the data or moving the video pointer.
Moving the video pointer exchanges the buffers so that the first buffer
drawn becomes the

front buffer

, or what is currently displayed on the
device; this is called

page flipping

.

Alternatively, the contents of the back buffer can be copied, or

blitted

forward in a chain instead of moving the video pointer.

```java
Double buffering:

*********** ***********
* * ------> * *
[To display] <---- * Front B * Show * Back B. * <---- Rendering
* * <------ * *
*********** ***********

Triple buffering:

[To *********** *********** ***********
display] * * --------+---------+------> * *
<---- * Front B * Show * Mid. B. * * Back B. * <---- Rendering
* * <------ * * <----- * *
*********** *********** ***********
```

Here is an example of how buffer strategies can be created and used:

```java
// Check the capabilities of the GraphicsConfiguration
...

// Create our component
Window w = new Window(gc);

// Show our window
w.setVisible(true);

// Create a general double-buffering strategy
w.createBufferStrategy(2);
BufferStrategy strategy = w.getBufferStrategy();

// Main loop
while (!done) {
// Prepare for rendering the next frame
// ...

// Render single frame
do {
// The following loop ensures that the contents of the drawing buffer
// are consistent in case the underlying surface was recreated
do {
// Get a new graphics context every time through the loop
// to make sure the strategy is validated
Graphics graphics = strategy.getDrawGraphics();

// Render to graphics
// ...

// Dispose the graphics
graphics.dispose();

// Repeat the rendering if the drawing buffer contents
// were restored
} while (strategy.contentsRestored());

// Display the buffer
strategy.show();

// Repeat the rendering if the drawing buffer was lost
} while (strategy.contentsLost());
}

// Dispose the window
w.setVisible(false);
w.dispose();
```

Alternatively, the contents of the back buffer can be copied, or

blitted

forward in a chain instead of moving the video pointer.

```java
Double buffering:

*********** ***********
* * ------> * *
[To display] <---- * Front B * Show * Back B. * <---- Rendering
* * <------ * *
*********** ***********

Triple buffering:

[To *********** *********** ***********
display] * * --------+---------+------> * *
<---- * Front B * Show * Mid. B. * * Back B. * <---- Rendering
* * <------ * * <----- * *
*********** *********** ***********
```

Here is an example of how buffer strategies can be created and used:

```java
// Check the capabilities of the GraphicsConfiguration
...

// Create our component
Window w = new Window(gc);

// Show our window
w.setVisible(true);

// Create a general double-buffering strategy
w.createBufferStrategy(2);
BufferStrategy strategy = w.getBufferStrategy();

// Main loop
while (!done) {
// Prepare for rendering the next frame
// ...

// Render single frame
do {
// The following loop ensures that the contents of the drawing buffer
// are consistent in case the underlying surface was recreated
do {
// Get a new graphics context every time through the loop
// to make sure the strategy is validated
Graphics graphics = strategy.getDrawGraphics();

// Render to graphics
// ...

// Dispose the graphics
graphics.dispose();

// Repeat the rendering if the drawing buffer contents
// were restored
} while (strategy.contentsRestored());

// Display the buffer
strategy.show();

// Repeat the rendering if the drawing buffer was lost
} while (strategy.contentsLost());
}

// Dispose the window
w.setVisible(false);
w.dispose();
```

Double buffering:

*********** ***********
* * ------> * *
[To display] <---- * Front B * Show * Back B. * <---- Rendering
* * <------ * *
*********** ***********

Triple buffering:

[To *********** *********** ***********
display] * * --------+---------+------> * *
<---- * Front B * Show * Mid. B. * * Back B. * <---- Rendering
* * <------ * * <----- * *
*********** *********** ***********

Here is an example of how buffer strategies can be created and used:

```java
// Check the capabilities of the GraphicsConfiguration
...

// Create our component
Window w = new Window(gc);

// Show our window
w.setVisible(true);

// Create a general double-buffering strategy
w.createBufferStrategy(2);
BufferStrategy strategy = w.getBufferStrategy();

// Main loop
while (!done) {
// Prepare for rendering the next frame
// ...

// Render single frame
do {
// The following loop ensures that the contents of the drawing buffer
// are consistent in case the underlying surface was recreated
do {
// Get a new graphics context every time through the loop
// to make sure the strategy is validated
Graphics graphics = strategy.getDrawGraphics();

// Render to graphics
// ...

// Dispose the graphics
graphics.dispose();

// Repeat the rendering if the drawing buffer contents
// were restored
} while (strategy.contentsRestored());

// Display the buffer
strategy.show();

// Repeat the rendering if the drawing buffer was lost
} while (strategy.contentsLost());
}

// Dispose the window
w.setVisible(false);
w.dispose();
```

// Check the capabilities of the GraphicsConfiguration
...

// Create our component
Window w = new Window(gc);

// Show our window
w.setVisible(true);

// Create a general double-buffering strategy
w.createBufferStrategy(2);
BufferStrategy strategy = w.getBufferStrategy();

// Main loop
while (!done) {
// Prepare for rendering the next frame
// ...

// Render single frame
do {
// The following loop ensures that the contents of the drawing buffer
// are consistent in case the underlying surface was recreated
do {
// Get a new graphics context every time through the loop
// to make sure the strategy is validated
Graphics graphics = strategy.getDrawGraphics();

// Render to graphics
// ...

// Dispose the graphics
graphics.dispose();

// Repeat the rendering if the drawing buffer contents
// were restored
} while (strategy.contentsRestored());

// Display the buffer
strategy.show();

// Repeat the rendering if the drawing buffer was lost
} while (strategy.contentsLost());
}

// Dispose the window
w.setVisible(false);
w.dispose();

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BufferStrategy

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract boolean

contentsLost

()

Returns whether the drawing buffer was lost since the last call to

getDrawGraphics

.

abstract boolean

contentsRestored

()

Returns whether the drawing buffer was recently restored from a lost
state and reinitialized to the default background color (white).

void

dispose

()

Releases system resources currently consumed by this

BufferStrategy

and
removes it from the associated Component.

abstract

BufferCapabilities

getCapabilities

()

Returns the

BufferCapabilities

for this

BufferStrategy

.

abstract

Graphics

getDrawGraphics

()

Creates a graphics context for the drawing buffer.

abstract void

show

()

Makes the next available buffer visible by either copying the memory
(blitting) or changing the display pointer (flipping).

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

BufferStrategy

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract boolean

contentsLost

()

Returns whether the drawing buffer was lost since the last call to

getDrawGraphics

.

abstract boolean

contentsRestored

()

Returns whether the drawing buffer was recently restored from a lost
state and reinitialized to the default background color (white).

void

dispose

()

Releases system resources currently consumed by this

BufferStrategy

and
removes it from the associated Component.

abstract

BufferCapabilities

getCapabilities

()

Returns the

BufferCapabilities

for this

BufferStrategy

.

abstract

Graphics

getDrawGraphics

()

Creates a graphics context for the drawing buffer.

abstract void

show

()

Makes the next available buffer visible by either copying the memory
(blitting) or changing the display pointer (flipping).

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns whether the drawing buffer was lost since the last call to

getDrawGraphics

.

Returns whether the drawing buffer was recently restored from a lost
state and reinitialized to the default background color (white).

Releases system resources currently consumed by this

BufferStrategy

and
removes it from the associated Component.

Returns the

BufferCapabilities

for this

BufferStrategy

.

Creates a graphics context for the drawing buffer.

Makes the next available buffer visible by either copying the memory
(blitting) or changing the display pointer (flipping).

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BufferStrategy

```java
public BufferStrategy()
```

============ METHOD DETAIL ==========

- Method Detail

- getCapabilities

```java
public abstract
BufferCapabilities
getCapabilities()
```

Returns the

BufferCapabilities

for this

BufferStrategy

.

**Returns:** the buffering capabilities of this strategy

- getDrawGraphics

```java
public abstract
Graphics
getDrawGraphics()
```

Creates a graphics context for the drawing buffer. This method may not
be synchronized for performance reasons; use of this method by multiple
threads should be handled at the application level. Disposal of the
graphics object obtained must be handled by the application.

**Returns:** a graphics context for the drawing buffer

- contentsLost

```java
public abstract boolean contentsLost()
```

Returns whether the drawing buffer was lost since the last call to

getDrawGraphics

. Since the buffers in a buffer strategy
are usually type

VolatileImage

, they may become lost.
For a discussion on lost buffers, see

VolatileImage

.

**Returns:** Whether or not the drawing buffer was lost since the last call
to

getDrawGraphics

.
**See Also:** VolatileImage

- contentsRestored

```java
public abstract boolean contentsRestored()
```

Returns whether the drawing buffer was recently restored from a lost
state and reinitialized to the default background color (white).
Since the buffers in a buffer strategy are usually type

VolatileImage

, they may become lost. If a surface has
been recently restored from a lost state since the last call to

getDrawGraphics

, it may require repainting.
For a discussion on lost buffers, see

VolatileImage

.

**Returns:** Whether or not the drawing buffer was restored since the last
call to

getDrawGraphics

.
**See Also:** VolatileImage

- show

```java
public abstract void show()
```

Makes the next available buffer visible by either copying the memory
(blitting) or changing the display pointer (flipping).

- dispose

```java
public void dispose()
```

Releases system resources currently consumed by this

BufferStrategy

and
removes it from the associated Component. After invoking this
method,

getBufferStrategy

will return null. Trying
to use a

BufferStrategy

after it has been disposed will
result in undefined behavior.

**Since:** 1.6
**See Also:** Window.createBufferStrategy(int)

,

Canvas.createBufferStrategy(int)

,

Window.getBufferStrategy()

,

Canvas.getBufferStrategy()

Constructor Detail

- BufferStrategy

```java
public BufferStrategy()
```

---

#### Constructor Detail

BufferStrategy

```java
public BufferStrategy()
```

---

#### BufferStrategy

public BufferStrategy()

Method Detail

- getCapabilities

```java
public abstract
BufferCapabilities
getCapabilities()
```

Returns the

BufferCapabilities

for this

BufferStrategy

.

**Returns:** the buffering capabilities of this strategy

- getDrawGraphics

```java
public abstract
Graphics
getDrawGraphics()
```

Creates a graphics context for the drawing buffer. This method may not
be synchronized for performance reasons; use of this method by multiple
threads should be handled at the application level. Disposal of the
graphics object obtained must be handled by the application.

**Returns:** a graphics context for the drawing buffer

- contentsLost

```java
public abstract boolean contentsLost()
```

Returns whether the drawing buffer was lost since the last call to

getDrawGraphics

. Since the buffers in a buffer strategy
are usually type

VolatileImage

, they may become lost.
For a discussion on lost buffers, see

VolatileImage

.

**Returns:** Whether or not the drawing buffer was lost since the last call
to

getDrawGraphics

.
**See Also:** VolatileImage

- contentsRestored

```java
public abstract boolean contentsRestored()
```

Returns whether the drawing buffer was recently restored from a lost
state and reinitialized to the default background color (white).
Since the buffers in a buffer strategy are usually type

VolatileImage

, they may become lost. If a surface has
been recently restored from a lost state since the last call to

getDrawGraphics

, it may require repainting.
For a discussion on lost buffers, see

VolatileImage

.

**Returns:** Whether or not the drawing buffer was restored since the last
call to

getDrawGraphics

.
**See Also:** VolatileImage

- show

```java
public abstract void show()
```

Makes the next available buffer visible by either copying the memory
(blitting) or changing the display pointer (flipping).

- dispose

```java
public void dispose()
```

Releases system resources currently consumed by this

BufferStrategy

and
removes it from the associated Component. After invoking this
method,

getBufferStrategy

will return null. Trying
to use a

BufferStrategy

after it has been disposed will
result in undefined behavior.

**Since:** 1.6
**See Also:** Window.createBufferStrategy(int)

,

Canvas.createBufferStrategy(int)

,

Window.getBufferStrategy()

,

Canvas.getBufferStrategy()

---

#### Method Detail

getCapabilities

```java
public abstract
BufferCapabilities
getCapabilities()
```

Returns the

BufferCapabilities

for this

BufferStrategy

.

**Returns:** the buffering capabilities of this strategy

---

#### getCapabilities

public abstract

BufferCapabilities

getCapabilities()

Returns the

BufferCapabilities

for this

BufferStrategy

.

getDrawGraphics

```java
public abstract
Graphics
getDrawGraphics()
```

Creates a graphics context for the drawing buffer. This method may not
be synchronized for performance reasons; use of this method by multiple
threads should be handled at the application level. Disposal of the
graphics object obtained must be handled by the application.

**Returns:** a graphics context for the drawing buffer

---

#### getDrawGraphics

public abstract

Graphics

getDrawGraphics()

Creates a graphics context for the drawing buffer. This method may not
be synchronized for performance reasons; use of this method by multiple
threads should be handled at the application level. Disposal of the
graphics object obtained must be handled by the application.

contentsLost

```java
public abstract boolean contentsLost()
```

Returns whether the drawing buffer was lost since the last call to

getDrawGraphics

. Since the buffers in a buffer strategy
are usually type

VolatileImage

, they may become lost.
For a discussion on lost buffers, see

VolatileImage

.

**Returns:** Whether or not the drawing buffer was lost since the last call
to

getDrawGraphics

.
**See Also:** VolatileImage

---

#### contentsLost

public abstract boolean contentsLost()

Returns whether the drawing buffer was lost since the last call to

getDrawGraphics

. Since the buffers in a buffer strategy
are usually type

VolatileImage

, they may become lost.
For a discussion on lost buffers, see

VolatileImage

.

contentsRestored

```java
public abstract boolean contentsRestored()
```

Returns whether the drawing buffer was recently restored from a lost
state and reinitialized to the default background color (white).
Since the buffers in a buffer strategy are usually type

VolatileImage

, they may become lost. If a surface has
been recently restored from a lost state since the last call to

getDrawGraphics

, it may require repainting.
For a discussion on lost buffers, see

VolatileImage

.

**Returns:** Whether or not the drawing buffer was restored since the last
call to

getDrawGraphics

.
**See Also:** VolatileImage

---

#### contentsRestored

public abstract boolean contentsRestored()

Returns whether the drawing buffer was recently restored from a lost
state and reinitialized to the default background color (white).
Since the buffers in a buffer strategy are usually type

VolatileImage

, they may become lost. If a surface has
been recently restored from a lost state since the last call to

getDrawGraphics

, it may require repainting.
For a discussion on lost buffers, see

VolatileImage

.

show

```java
public abstract void show()
```

Makes the next available buffer visible by either copying the memory
(blitting) or changing the display pointer (flipping).

---

#### show

public abstract void show()

Makes the next available buffer visible by either copying the memory
(blitting) or changing the display pointer (flipping).

dispose

```java
public void dispose()
```

Releases system resources currently consumed by this

BufferStrategy

and
removes it from the associated Component. After invoking this
method,

getBufferStrategy

will return null. Trying
to use a

BufferStrategy

after it has been disposed will
result in undefined behavior.

**Since:** 1.6
**See Also:** Window.createBufferStrategy(int)

,

Canvas.createBufferStrategy(int)

,

Window.getBufferStrategy()

,

Canvas.getBufferStrategy()

---

#### dispose

public void dispose()

Releases system resources currently consumed by this

BufferStrategy

and
removes it from the associated Component. After invoking this
method,

getBufferStrategy

will return null. Trying
to use a

BufferStrategy

after it has been disposed will
result in undefined behavior.

---

