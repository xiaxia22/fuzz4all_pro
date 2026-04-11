# Class MediaTracker

**Source:** `java.desktop\java\awt\MediaTracker.html`

### Class Description

```java
public class
MediaTracker

extends
Object

implements
Serializable
```

The

MediaTracker

class is a utility class to track
the status of a number of media objects. Media objects could
include audio clips as well as images, though currently only
images are supported.

To use a media tracker, create an instance of

MediaTracker

and call its

addImage

method for each image to be tracked. In addition, each image can
be assigned a unique identifier. This identifier controls the
priority order in which the images are fetched. It can also be used
to identify unique subsets of the images that can be waited on
independently. Images with a lower ID are loaded in preference to
those with a higher ID number.

Tracking an animated image
might not always be useful
due to the multi-part nature of animated image
loading and painting,
but it is supported.

MediaTracker

treats an animated image
as completely loaded
when the first frame is completely loaded.
At that point, the

MediaTracker

signals any waiters
that the image is completely loaded.
If no

ImageObserver

s are observing the image
when the first frame has finished loading,
the image might flush itself
to conserve resources
(see

Image.flush()

).

Here is an example of using

MediaTracker

:

```java
import java.applet.Applet;
import java.awt.Color;
import java.awt.Image;
import java.awt.Graphics;
import java.awt.MediaTracker;

public class ImageBlaster extends Applet implements Runnable {
MediaTracker tracker;
Image bg;
Image anim[] = new Image[5];
int index;
Thread animator;

// Get the images for the background (id == 0)
// and the animation frames (id == 1)
// and add them to the MediaTracker
public void init() {
tracker = new MediaTracker(this);
bg = getImage(getDocumentBase(),
"images/background.gif");
tracker.addImage(bg, 0);
for (int i = 0; i < 5; i++) {
anim[i] = getImage(getDocumentBase(),
"images/anim"+i+".gif");
tracker.addImage(anim[i], 1);
}
}

// Start the animation thread.
public void start() {
animator = new Thread(this);
animator.start();
}

// Stop the animation thread.
public void stop() {
animator = null;
}

// Run the animation thread.
// First wait for the background image to fully load
// and paint. Then wait for all of the animation
// frames to finish loading. Finally, loop and
// increment the animation frame index.
public void run() {
try {
tracker.waitForID(0);
tracker.waitForID(1);
} catch (InterruptedException e) {
return;
}
Thread me = Thread.currentThread();
while (animator == me) {
try {
Thread.sleep(100);
} catch (InterruptedException e) {
break;
}
synchronized (this) {
index++;
if (index >= anim.length) {
index = 0;
}
}
repaint();
}
}

// The background image fills the frame so we
// don't need to clear the applet on repaints.
// Just call the paint method.
public void update(Graphics g) {
paint(g);
}

// Paint a large red rectangle if there are any errors
// loading the images. Otherwise always paint the
// background so that it appears incrementally as it
// is loading. Finally, only paint the current animation
// frame if all of the frames (id == 1) are done loading,
// so that we don't get partial animations.
public void paint(Graphics g) {
if ((tracker.statusAll(false) & MediaTracker.ERRORED) != 0) {
g.setColor(Color.red);
g.fillRect(0, 0, size().width, size().height);
return;
}
g.drawImage(bg, 0, 0, this);
if (tracker.statusID(1, false) == MediaTracker.COMPLETE) {
g.drawImage(anim[index], 10, 10, this);
}
}
}
```

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int LOADING

Flag indicating that media is currently being loaded.

**See Also:**
- statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

---

#### public static final int ABORTED

Flag indicating that the downloading of media was aborted.

**See Also:**
- statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

---

#### public static final int ERRORED

Flag indicating that the downloading of media encountered
an error.

**See Also:**
- statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

---

#### public static final int COMPLETE

Flag indicating that the downloading of media was completed
successfully.

**See Also:**
- statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

---

### Constructor Details

#### public MediaTracker​(
Component
comp)

Creates a media tracker to track images for a given component.

**Parameters:**
- comp

- the component on which the images
will eventually be drawn

---

### Method Details

#### public void addImage​(
Image
image,
int id)

Adds an image to the list of images being tracked by this media
tracker. The image will eventually be rendered at its default
(unscaled) size.

**Parameters:**
- image

- the image to be tracked
- id

- an identifier used to track this image

---

#### public void addImage​(
Image
image,
int id,
int w,
int h)

Adds a scaled image to the list of images being tracked
by this media tracker. The image will eventually be
rendered at the indicated width and height.

**Parameters:**
- image

- the image to be tracked
- id

- an identifier that can be used to track this image
- w

- the width at which the image is rendered
- h

- the height at which the image is rendered

---

#### public boolean checkAll()

Checks to see if all images being tracked by this media tracker
have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Returns:**
- true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise

**See Also:**
- checkAll(boolean)

,

checkID(int)

,

isErrorAny()

,

isErrorID(int)

---

#### public boolean checkAll​(boolean load)

Checks to see if all images being tracked by this media tracker
have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

**Parameters:**
- load

- if

true

, start loading any
images that are not yet being loaded

**Returns:**
- true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise

**See Also:**
- checkID(int)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

---

#### public boolean isErrorAny()

Checks the error status of all of the images.

**Returns:**
- true

if any of the images tracked
by this media tracker had an error during
loading;

false

otherwise

**See Also:**
- isErrorID(int)

,

getErrorsAny()

---

#### public
Object
[] getErrorsAny()

Returns a list of all media that have encountered an error.

**Returns:**
- an array of media objects tracked by this
media tracker that have encountered
an error, or

null

if
there are none with errors

**See Also:**
- isErrorAny()

,

getErrorsID(int)

---

#### public void waitForAll()
throws
InterruptedException

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Throws:**
- InterruptedException

- if any thread has
interrupted this thread

**See Also:**
- waitForID(int)

,

waitForAll(long)

,

isErrorAny()

,

isErrorID(int)

---

#### public boolean waitForAll​(long ms)
throws
InterruptedException

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading, or until the length of time specified in milliseconds
by the

ms

argument has passed.

If there is an error while loading or scaling an image, then
that image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:**
- ms

- the number of milliseconds to wait
for the loading to complete

**Returns:**
- true

if all images were successfully
loaded;

false

otherwise

**Throws:**
- InterruptedException

- if any thread has
interrupted this thread.

**See Also:**
- waitForID(int)

,

waitForAll(long)

,

isErrorAny()

,

isErrorID(int)

---

#### public int statusAll​(boolean load)

Calculates and returns the bitwise inclusive

OR

of the
status of all media that are tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

**Parameters:**
- load

- if

true

, start loading
any images that are not yet being loaded

**Returns:**
- the bitwise inclusive

OR

of the status of
all of the media being tracked

**See Also:**
- statusID(int, boolean)

,

LOADING

,

ABORTED

,

ERRORED

,

COMPLETE

---

#### public boolean checkID​(int id)

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:**
- id

- the identifier of the images to check

**Returns:**
- true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise

**See Also:**
- checkID(int, boolean)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

---

#### public boolean checkID​(int id,
boolean load)

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:**
- id

- the identifier of the images to check
- load

- if

true

, start loading any
images that are not yet being loaded

**Returns:**
- true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise

**See Also:**
- checkID(int, boolean)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

---

#### public boolean isErrorID​(int id)

Checks the error status of all of the images tracked by this
media tracker with the specified identifier.

**Parameters:**
- id

- the identifier of the images to check

**Returns:**
- true

if any of the images with the
specified identifier had an error during
loading;

false

otherwise

**See Also:**
- isErrorAny()

,

getErrorsID(int)

---

#### public
Object
[] getErrorsID​(int id)

Returns a list of media with the specified ID that
have encountered an error.

**Parameters:**
- id

- the identifier of the images to check

**Returns:**
- an array of media objects tracked by this media
tracker with the specified identifier
that have encountered an error, or

null

if there are none with errors

**See Also:**
- isErrorID(int)

,

isErrorAny()

,

getErrorsAny()

---

#### public void waitForID​(int id)
throws
InterruptedException

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

**Parameters:**
- id

- the identifier of the images to check

**Throws:**
- InterruptedException

- if any thread has
interrupted this thread.

**See Also:**
- waitForAll()

,

isErrorAny()

,

isErrorID(int)

---

#### public boolean waitForID​(int id,
long ms)
throws
InterruptedException

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading, or until the
length of time specified in milliseconds by the

ms

argument has passed.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

statusID

,

isErrorID

, and

isErrorAny

methods to check for errors.

**Parameters:**
- id

- the identifier of the images to check
- ms

- the length of time, in milliseconds, to wait
for the loading to complete

**Returns:**
- true

if the loading completed in time;
otherwise

false

**Throws:**
- InterruptedException

- if any thread has
interrupted this thread.

**See Also:**
- waitForAll()

,

waitForID(int)

,

statusID(int, boolean)

,

isErrorAny()

,

isErrorID(int)

---

#### public int statusID​(int id,
boolean load)

Calculates and returns the bitwise inclusive

OR

of the
status of all media with the specified identifier that are
tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

**Parameters:**
- id

- the identifier of the images to check
- load

- if

true

, start loading
any images that are not yet being loaded

**Returns:**
- the bitwise inclusive

OR

of the status of
all of the media with the specified
identifier that are being tracked

**See Also:**
- statusAll(boolean)

,

LOADING

,

ABORTED

,

ERRORED

,

COMPLETE

---

#### public void removeImage​(
Image
image)

Removes the specified image from this media tracker.
All instances of the specified image are removed,
regardless of scale or ID.

**Parameters:**
- image

- the image to be removed

**See Also:**
- removeImage(java.awt.Image, int)

,

removeImage(java.awt.Image, int, int, int)

**Since:**
- 1.1

---

#### public void removeImage​(
Image
image,
int id)

Removes the specified image from the specified tracking
ID of this media tracker.
All instances of

Image

being tracked
under the specified ID are removed regardless of scale.

**Parameters:**
- image

- the image to be removed
- id

- the tracking ID from which to remove the image

**See Also:**
- removeImage(java.awt.Image)

,

removeImage(java.awt.Image, int, int, int)

**Since:**
- 1.1

---

#### public void removeImage​(
Image
image,
int id,
int width,
int height)

Removes the specified image with the specified
width, height, and ID from this media tracker.
Only the specified instance (with any duplicates) is removed.

**Parameters:**
- image

- the image to be removed
- id

- the tracking ID from which to remove the image
- width

- the width to remove (-1 for unscaled)
- height

- the height to remove (-1 for unscaled)

**See Also:**
- removeImage(java.awt.Image)

,

removeImage(java.awt.Image, int)

**Since:**
- 1.1

---

### Additional Sections

#### Class MediaTracker

java.lang.Object

- java.awt.MediaTracker

java.awt.MediaTracker

**All Implemented Interfaces:** Serializable

```java
public class
MediaTracker

extends
Object

implements
Serializable
```

The

MediaTracker

class is a utility class to track
the status of a number of media objects. Media objects could
include audio clips as well as images, though currently only
images are supported.

To use a media tracker, create an instance of

MediaTracker

and call its

addImage

method for each image to be tracked. In addition, each image can
be assigned a unique identifier. This identifier controls the
priority order in which the images are fetched. It can also be used
to identify unique subsets of the images that can be waited on
independently. Images with a lower ID are loaded in preference to
those with a higher ID number.

Tracking an animated image
might not always be useful
due to the multi-part nature of animated image
loading and painting,
but it is supported.

MediaTracker

treats an animated image
as completely loaded
when the first frame is completely loaded.
At that point, the

MediaTracker

signals any waiters
that the image is completely loaded.
If no

ImageObserver

s are observing the image
when the first frame has finished loading,
the image might flush itself
to conserve resources
(see

Image.flush()

).

Here is an example of using

MediaTracker

:

```java
import java.applet.Applet;
import java.awt.Color;
import java.awt.Image;
import java.awt.Graphics;
import java.awt.MediaTracker;

public class ImageBlaster extends Applet implements Runnable {
MediaTracker tracker;
Image bg;
Image anim[] = new Image[5];
int index;
Thread animator;

// Get the images for the background (id == 0)
// and the animation frames (id == 1)
// and add them to the MediaTracker
public void init() {
tracker = new MediaTracker(this);
bg = getImage(getDocumentBase(),
"images/background.gif");
tracker.addImage(bg, 0);
for (int i = 0; i < 5; i++) {
anim[i] = getImage(getDocumentBase(),
"images/anim"+i+".gif");
tracker.addImage(anim[i], 1);
}
}

// Start the animation thread.
public void start() {
animator = new Thread(this);
animator.start();
}

// Stop the animation thread.
public void stop() {
animator = null;
}

// Run the animation thread.
// First wait for the background image to fully load
// and paint. Then wait for all of the animation
// frames to finish loading. Finally, loop and
// increment the animation frame index.
public void run() {
try {
tracker.waitForID(0);
tracker.waitForID(1);
} catch (InterruptedException e) {
return;
}
Thread me = Thread.currentThread();
while (animator == me) {
try {
Thread.sleep(100);
} catch (InterruptedException e) {
break;
}
synchronized (this) {
index++;
if (index >= anim.length) {
index = 0;
}
}
repaint();
}
}

// The background image fills the frame so we
// don't need to clear the applet on repaints.
// Just call the paint method.
public void update(Graphics g) {
paint(g);
}

// Paint a large red rectangle if there are any errors
// loading the images. Otherwise always paint the
// background so that it appears incrementally as it
// is loading. Finally, only paint the current animation
// frame if all of the frames (id == 1) are done loading,
// so that we don't get partial animations.
public void paint(Graphics g) {
if ((tracker.statusAll(false) & MediaTracker.ERRORED) != 0) {
g.setColor(Color.red);
g.fillRect(0, 0, size().width, size().height);
return;
}
g.drawImage(bg, 0, 0, this);
if (tracker.statusID(1, false) == MediaTracker.COMPLETE) {
g.drawImage(anim[index], 10, 10, this);
}
}
}
```

**Since:** 1.0
**See Also:** Serialized Form

public class

MediaTracker

extends

Object

implements

Serializable

The

MediaTracker

class is a utility class to track
the status of a number of media objects. Media objects could
include audio clips as well as images, though currently only
images are supported.

To use a media tracker, create an instance of

MediaTracker

and call its

addImage

method for each image to be tracked. In addition, each image can
be assigned a unique identifier. This identifier controls the
priority order in which the images are fetched. It can also be used
to identify unique subsets of the images that can be waited on
independently. Images with a lower ID are loaded in preference to
those with a higher ID number.

Tracking an animated image
might not always be useful
due to the multi-part nature of animated image
loading and painting,
but it is supported.

MediaTracker

treats an animated image
as completely loaded
when the first frame is completely loaded.
At that point, the

MediaTracker

signals any waiters
that the image is completely loaded.
If no

ImageObserver

s are observing the image
when the first frame has finished loading,
the image might flush itself
to conserve resources
(see

Image.flush()

).

Here is an example of using

MediaTracker

:

```java
import java.applet.Applet;
import java.awt.Color;
import java.awt.Image;
import java.awt.Graphics;
import java.awt.MediaTracker;

public class ImageBlaster extends Applet implements Runnable {
MediaTracker tracker;
Image bg;
Image anim[] = new Image[5];
int index;
Thread animator;

// Get the images for the background (id == 0)
// and the animation frames (id == 1)
// and add them to the MediaTracker
public void init() {
tracker = new MediaTracker(this);
bg = getImage(getDocumentBase(),
"images/background.gif");
tracker.addImage(bg, 0);
for (int i = 0; i < 5; i++) {
anim[i] = getImage(getDocumentBase(),
"images/anim"+i+".gif");
tracker.addImage(anim[i], 1);
}
}

// Start the animation thread.
public void start() {
animator = new Thread(this);
animator.start();
}

// Stop the animation thread.
public void stop() {
animator = null;
}

// Run the animation thread.
// First wait for the background image to fully load
// and paint. Then wait for all of the animation
// frames to finish loading. Finally, loop and
// increment the animation frame index.
public void run() {
try {
tracker.waitForID(0);
tracker.waitForID(1);
} catch (InterruptedException e) {
return;
}
Thread me = Thread.currentThread();
while (animator == me) {
try {
Thread.sleep(100);
} catch (InterruptedException e) {
break;
}
synchronized (this) {
index++;
if (index >= anim.length) {
index = 0;
}
}
repaint();
}
}

// The background image fills the frame so we
// don't need to clear the applet on repaints.
// Just call the paint method.
public void update(Graphics g) {
paint(g);
}

// Paint a large red rectangle if there are any errors
// loading the images. Otherwise always paint the
// background so that it appears incrementally as it
// is loading. Finally, only paint the current animation
// frame if all of the frames (id == 1) are done loading,
// so that we don't get partial animations.
public void paint(Graphics g) {
if ((tracker.statusAll(false) & MediaTracker.ERRORED) != 0) {
g.setColor(Color.red);
g.fillRect(0, 0, size().width, size().height);
return;
}
g.drawImage(bg, 0, 0, this);
if (tracker.statusID(1, false) == MediaTracker.COMPLETE) {
g.drawImage(anim[index], 10, 10, this);
}
}
}
```

To use a media tracker, create an instance of

MediaTracker

and call its

addImage

method for each image to be tracked. In addition, each image can
be assigned a unique identifier. This identifier controls the
priority order in which the images are fetched. It can also be used
to identify unique subsets of the images that can be waited on
independently. Images with a lower ID are loaded in preference to
those with a higher ID number.

Tracking an animated image
might not always be useful
due to the multi-part nature of animated image
loading and painting,
but it is supported.

MediaTracker

treats an animated image
as completely loaded
when the first frame is completely loaded.
At that point, the

MediaTracker

signals any waiters
that the image is completely loaded.
If no

ImageObserver

s are observing the image
when the first frame has finished loading,
the image might flush itself
to conserve resources
(see

Image.flush()

).

Here is an example of using

MediaTracker

:

```java
import java.applet.Applet;
import java.awt.Color;
import java.awt.Image;
import java.awt.Graphics;
import java.awt.MediaTracker;

public class ImageBlaster extends Applet implements Runnable {
MediaTracker tracker;
Image bg;
Image anim[] = new Image[5];
int index;
Thread animator;

// Get the images for the background (id == 0)
// and the animation frames (id == 1)
// and add them to the MediaTracker
public void init() {
tracker = new MediaTracker(this);
bg = getImage(getDocumentBase(),
"images/background.gif");
tracker.addImage(bg, 0);
for (int i = 0; i < 5; i++) {
anim[i] = getImage(getDocumentBase(),
"images/anim"+i+".gif");
tracker.addImage(anim[i], 1);
}
}

// Start the animation thread.
public void start() {
animator = new Thread(this);
animator.start();
}

// Stop the animation thread.
public void stop() {
animator = null;
}

// Run the animation thread.
// First wait for the background image to fully load
// and paint. Then wait for all of the animation
// frames to finish loading. Finally, loop and
// increment the animation frame index.
public void run() {
try {
tracker.waitForID(0);
tracker.waitForID(1);
} catch (InterruptedException e) {
return;
}
Thread me = Thread.currentThread();
while (animator == me) {
try {
Thread.sleep(100);
} catch (InterruptedException e) {
break;
}
synchronized (this) {
index++;
if (index >= anim.length) {
index = 0;
}
}
repaint();
}
}

// The background image fills the frame so we
// don't need to clear the applet on repaints.
// Just call the paint method.
public void update(Graphics g) {
paint(g);
}

// Paint a large red rectangle if there are any errors
// loading the images. Otherwise always paint the
// background so that it appears incrementally as it
// is loading. Finally, only paint the current animation
// frame if all of the frames (id == 1) are done loading,
// so that we don't get partial animations.
public void paint(Graphics g) {
if ((tracker.statusAll(false) & MediaTracker.ERRORED) != 0) {
g.setColor(Color.red);
g.fillRect(0, 0, size().width, size().height);
return;
}
g.drawImage(bg, 0, 0, this);
if (tracker.statusID(1, false) == MediaTracker.COMPLETE) {
g.drawImage(anim[index], 10, 10, this);
}
}
}
```

Tracking an animated image
might not always be useful
due to the multi-part nature of animated image
loading and painting,
but it is supported.

MediaTracker

treats an animated image
as completely loaded
when the first frame is completely loaded.
At that point, the

MediaTracker

signals any waiters
that the image is completely loaded.
If no

ImageObserver

s are observing the image
when the first frame has finished loading,
the image might flush itself
to conserve resources
(see

Image.flush()

).

Here is an example of using

MediaTracker

:

```java
import java.applet.Applet;
import java.awt.Color;
import java.awt.Image;
import java.awt.Graphics;
import java.awt.MediaTracker;

public class ImageBlaster extends Applet implements Runnable {
MediaTracker tracker;
Image bg;
Image anim[] = new Image[5];
int index;
Thread animator;

// Get the images for the background (id == 0)
// and the animation frames (id == 1)
// and add them to the MediaTracker
public void init() {
tracker = new MediaTracker(this);
bg = getImage(getDocumentBase(),
"images/background.gif");
tracker.addImage(bg, 0);
for (int i = 0; i < 5; i++) {
anim[i] = getImage(getDocumentBase(),
"images/anim"+i+".gif");
tracker.addImage(anim[i], 1);
}
}

// Start the animation thread.
public void start() {
animator = new Thread(this);
animator.start();
}

// Stop the animation thread.
public void stop() {
animator = null;
}

// Run the animation thread.
// First wait for the background image to fully load
// and paint. Then wait for all of the animation
// frames to finish loading. Finally, loop and
// increment the animation frame index.
public void run() {
try {
tracker.waitForID(0);
tracker.waitForID(1);
} catch (InterruptedException e) {
return;
}
Thread me = Thread.currentThread();
while (animator == me) {
try {
Thread.sleep(100);
} catch (InterruptedException e) {
break;
}
synchronized (this) {
index++;
if (index >= anim.length) {
index = 0;
}
}
repaint();
}
}

// The background image fills the frame so we
// don't need to clear the applet on repaints.
// Just call the paint method.
public void update(Graphics g) {
paint(g);
}

// Paint a large red rectangle if there are any errors
// loading the images. Otherwise always paint the
// background so that it appears incrementally as it
// is loading. Finally, only paint the current animation
// frame if all of the frames (id == 1) are done loading,
// so that we don't get partial animations.
public void paint(Graphics g) {
if ((tracker.statusAll(false) & MediaTracker.ERRORED) != 0) {
g.setColor(Color.red);
g.fillRect(0, 0, size().width, size().height);
return;
}
g.drawImage(bg, 0, 0, this);
if (tracker.statusID(1, false) == MediaTracker.COMPLETE) {
g.drawImage(anim[index], 10, 10, this);
}
}
}
```

Here is an example of using

MediaTracker

:

```java
import java.applet.Applet;
import java.awt.Color;
import java.awt.Image;
import java.awt.Graphics;
import java.awt.MediaTracker;

public class ImageBlaster extends Applet implements Runnable {
MediaTracker tracker;
Image bg;
Image anim[] = new Image[5];
int index;
Thread animator;

// Get the images for the background (id == 0)
// and the animation frames (id == 1)
// and add them to the MediaTracker
public void init() {
tracker = new MediaTracker(this);
bg = getImage(getDocumentBase(),
"images/background.gif");
tracker.addImage(bg, 0);
for (int i = 0; i < 5; i++) {
anim[i] = getImage(getDocumentBase(),
"images/anim"+i+".gif");
tracker.addImage(anim[i], 1);
}
}

// Start the animation thread.
public void start() {
animator = new Thread(this);
animator.start();
}

// Stop the animation thread.
public void stop() {
animator = null;
}

// Run the animation thread.
// First wait for the background image to fully load
// and paint. Then wait for all of the animation
// frames to finish loading. Finally, loop and
// increment the animation frame index.
public void run() {
try {
tracker.waitForID(0);
tracker.waitForID(1);
} catch (InterruptedException e) {
return;
}
Thread me = Thread.currentThread();
while (animator == me) {
try {
Thread.sleep(100);
} catch (InterruptedException e) {
break;
}
synchronized (this) {
index++;
if (index >= anim.length) {
index = 0;
}
}
repaint();
}
}

// The background image fills the frame so we
// don't need to clear the applet on repaints.
// Just call the paint method.
public void update(Graphics g) {
paint(g);
}

// Paint a large red rectangle if there are any errors
// loading the images. Otherwise always paint the
// background so that it appears incrementally as it
// is loading. Finally, only paint the current animation
// frame if all of the frames (id == 1) are done loading,
// so that we don't get partial animations.
public void paint(Graphics g) {
if ((tracker.statusAll(false) & MediaTracker.ERRORED) != 0) {
g.setColor(Color.red);
g.fillRect(0, 0, size().width, size().height);
return;
}
g.drawImage(bg, 0, 0, this);
if (tracker.statusID(1, false) == MediaTracker.COMPLETE) {
g.drawImage(anim[index], 10, 10, this);
}
}
}
```

import java.applet.Applet;
import java.awt.Color;
import java.awt.Image;
import java.awt.Graphics;
import java.awt.MediaTracker;

public class ImageBlaster extends Applet implements Runnable {
MediaTracker tracker;
Image bg;
Image anim[] = new Image[5];
int index;
Thread animator;

// Get the images for the background (id == 0)
// and the animation frames (id == 1)
// and add them to the MediaTracker
public void init() {
tracker = new MediaTracker(this);
bg = getImage(getDocumentBase(),
"images/background.gif");
tracker.addImage(bg, 0);
for (int i = 0; i < 5; i++) {
anim[i] = getImage(getDocumentBase(),
"images/anim"+i+".gif");
tracker.addImage(anim[i], 1);
}
}

// Start the animation thread.
public void start() {
animator = new Thread(this);
animator.start();
}

// Stop the animation thread.
public void stop() {
animator = null;
}

// Run the animation thread.
// First wait for the background image to fully load
// and paint. Then wait for all of the animation
// frames to finish loading. Finally, loop and
// increment the animation frame index.
public void run() {
try {
tracker.waitForID(0);
tracker.waitForID(1);
} catch (InterruptedException e) {
return;
}
Thread me = Thread.currentThread();
while (animator == me) {
try {
Thread.sleep(100);
} catch (InterruptedException e) {
break;
}
synchronized (this) {
index++;
if (index >= anim.length) {
index = 0;
}
}
repaint();
}
}

// The background image fills the frame so we
// don't need to clear the applet on repaints.
// Just call the paint method.
public void update(Graphics g) {
paint(g);
}

// Paint a large red rectangle if there are any errors
// loading the images. Otherwise always paint the
// background so that it appears incrementally as it
// is loading. Finally, only paint the current animation
// frame if all of the frames (id == 1) are done loading,
// so that we don't get partial animations.
public void paint(Graphics g) {
if ((tracker.statusAll(false) & MediaTracker.ERRORED) != 0) {
g.setColor(Color.red);
g.fillRect(0, 0, size().width, size().height);
return;
}
g.drawImage(bg, 0, 0, this);
if (tracker.statusID(1, false) == MediaTracker.COMPLETE) {
g.drawImage(anim[index], 10, 10, this);
}
}
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ABORTED

Flag indicating that the downloading of media was aborted.

static int

COMPLETE

Flag indicating that the downloading of media was completed
successfully.

static int

ERRORED

Flag indicating that the downloading of media encountered
an error.

static int

LOADING

Flag indicating that media is currently being loaded.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MediaTracker

​(

Component

comp)

Creates a media tracker to track images for a given component.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addImage

​(

Image

image,
int id)

Adds an image to the list of images being tracked by this media
tracker.

void

addImage

​(

Image

image,
int id,
int w,
int h)

Adds a scaled image to the list of images being tracked
by this media tracker.

boolean

checkAll

()

Checks to see if all images being tracked by this media tracker
have finished loading.

boolean

checkAll

​(boolean load)

Checks to see if all images being tracked by this media tracker
have finished loading.

boolean

checkID

​(int id)

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

boolean

checkID

​(int id,
boolean load)

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

Object

[]

getErrorsAny

()

Returns a list of all media that have encountered an error.

Object

[]

getErrorsID

​(int id)

Returns a list of media with the specified ID that
have encountered an error.

boolean

isErrorAny

()

Checks the error status of all of the images.

boolean

isErrorID

​(int id)

Checks the error status of all of the images tracked by this
media tracker with the specified identifier.

void

removeImage

​(

Image

image)

Removes the specified image from this media tracker.

void

removeImage

​(

Image

image,
int id)

Removes the specified image from the specified tracking
ID of this media tracker.

void

removeImage

​(

Image

image,
int id,
int width,
int height)

Removes the specified image with the specified
width, height, and ID from this media tracker.

int

statusAll

​(boolean load)

Calculates and returns the bitwise inclusive

OR

of the
status of all media that are tracked by this media tracker.

int

statusID

​(int id,
boolean load)

Calculates and returns the bitwise inclusive

OR

of the
status of all media with the specified identifier that are
tracked by this media tracker.

void

waitForAll

()

Starts loading all images tracked by this media tracker.

boolean

waitForAll

​(long ms)

Starts loading all images tracked by this media tracker.

void

waitForID

​(int id)

Starts loading all images tracked by this media tracker with the
specified identifier.

boolean

waitForID

​(int id,
long ms)

Starts loading all images tracked by this media tracker with the
specified identifier.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

ABORTED

Flag indicating that the downloading of media was aborted.

static int

COMPLETE

Flag indicating that the downloading of media was completed
successfully.

static int

ERRORED

Flag indicating that the downloading of media encountered
an error.

static int

LOADING

Flag indicating that media is currently being loaded.

---

#### Field Summary

Flag indicating that the downloading of media was aborted.

Flag indicating that the downloading of media was completed
successfully.

Flag indicating that the downloading of media encountered
an error.

Flag indicating that media is currently being loaded.

Constructor Summary

Constructors

Constructor

Description

MediaTracker

​(

Component

comp)

Creates a media tracker to track images for a given component.

---

#### Constructor Summary

Creates a media tracker to track images for a given component.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addImage

​(

Image

image,
int id)

Adds an image to the list of images being tracked by this media
tracker.

void

addImage

​(

Image

image,
int id,
int w,
int h)

Adds a scaled image to the list of images being tracked
by this media tracker.

boolean

checkAll

()

Checks to see if all images being tracked by this media tracker
have finished loading.

boolean

checkAll

​(boolean load)

Checks to see if all images being tracked by this media tracker
have finished loading.

boolean

checkID

​(int id)

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

boolean

checkID

​(int id,
boolean load)

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

Object

[]

getErrorsAny

()

Returns a list of all media that have encountered an error.

Object

[]

getErrorsID

​(int id)

Returns a list of media with the specified ID that
have encountered an error.

boolean

isErrorAny

()

Checks the error status of all of the images.

boolean

isErrorID

​(int id)

Checks the error status of all of the images tracked by this
media tracker with the specified identifier.

void

removeImage

​(

Image

image)

Removes the specified image from this media tracker.

void

removeImage

​(

Image

image,
int id)

Removes the specified image from the specified tracking
ID of this media tracker.

void

removeImage

​(

Image

image,
int id,
int width,
int height)

Removes the specified image with the specified
width, height, and ID from this media tracker.

int

statusAll

​(boolean load)

Calculates and returns the bitwise inclusive

OR

of the
status of all media that are tracked by this media tracker.

int

statusID

​(int id,
boolean load)

Calculates and returns the bitwise inclusive

OR

of the
status of all media with the specified identifier that are
tracked by this media tracker.

void

waitForAll

()

Starts loading all images tracked by this media tracker.

boolean

waitForAll

​(long ms)

Starts loading all images tracked by this media tracker.

void

waitForID

​(int id)

Starts loading all images tracked by this media tracker with the
specified identifier.

boolean

waitForID

​(int id,
long ms)

Starts loading all images tracked by this media tracker with the
specified identifier.

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

Adds an image to the list of images being tracked by this media
tracker.

Adds a scaled image to the list of images being tracked
by this media tracker.

Checks to see if all images being tracked by this media tracker
have finished loading.

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

Returns a list of all media that have encountered an error.

Returns a list of media with the specified ID that
have encountered an error.

Checks the error status of all of the images.

Checks the error status of all of the images tracked by this
media tracker with the specified identifier.

Removes the specified image from this media tracker.

Removes the specified image from the specified tracking
ID of this media tracker.

Removes the specified image with the specified
width, height, and ID from this media tracker.

Calculates and returns the bitwise inclusive

OR

of the
status of all media that are tracked by this media tracker.

Calculates and returns the bitwise inclusive

OR

of the
status of all media with the specified identifier that are
tracked by this media tracker.

Starts loading all images tracked by this media tracker.

Starts loading all images tracked by this media tracker with the
specified identifier.

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

============ FIELD DETAIL ===========

- Field Detail

- LOADING

```java
public static final int LOADING
```

Flag indicating that media is currently being loaded.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

- ABORTED

```java
public static final int ABORTED
```

Flag indicating that the downloading of media was aborted.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

- ERRORED

```java
public static final int ERRORED
```

Flag indicating that the downloading of media encountered
an error.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

- COMPLETE

```java
public static final int COMPLETE
```

Flag indicating that the downloading of media was completed
successfully.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MediaTracker

```java
public MediaTracker​(
Component
comp)
```

Creates a media tracker to track images for a given component.

**Parameters:** comp

- the component on which the images
will eventually be drawn

============ METHOD DETAIL ==========

- Method Detail

- addImage

```java
public void addImage​(
Image
image,
int id)
```

Adds an image to the list of images being tracked by this media
tracker. The image will eventually be rendered at its default
(unscaled) size.

**Parameters:** image

- the image to be tracked
**Parameters:** id

- an identifier used to track this image

- addImage

```java
public void addImage​(
Image
image,
int id,
int w,
int h)
```

Adds a scaled image to the list of images being tracked
by this media tracker. The image will eventually be
rendered at the indicated width and height.

**Parameters:** image

- the image to be tracked
**Parameters:** id

- an identifier that can be used to track this image
**Parameters:** w

- the width at which the image is rendered
**Parameters:** h

- the height at which the image is rendered

- checkAll

```java
public boolean checkAll()
```

Checks to see if all images being tracked by this media tracker
have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkAll(boolean)

,

checkID(int)

,

isErrorAny()

,

isErrorID(int)

- checkAll

```java
public boolean checkAll​(boolean load)
```

Checks to see if all images being tracked by this media tracker
have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

**Parameters:** load

- if

true

, start loading any
images that are not yet being loaded
**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkID(int)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

- isErrorAny

```java
public boolean isErrorAny()
```

Checks the error status of all of the images.

**Returns:** true

if any of the images tracked
by this media tracker had an error during
loading;

false

otherwise
**See Also:** isErrorID(int)

,

getErrorsAny()

- getErrorsAny

```java
public
Object
[] getErrorsAny()
```

Returns a list of all media that have encountered an error.

**Returns:** an array of media objects tracked by this
media tracker that have encountered
an error, or

null

if
there are none with errors
**See Also:** isErrorAny()

,

getErrorsID(int)

- waitForAll

```java
public void waitForAll()
throws
InterruptedException
```

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Throws:** InterruptedException

- if any thread has
interrupted this thread
**See Also:** waitForID(int)

,

waitForAll(long)

,

isErrorAny()

,

isErrorID(int)

- waitForAll

```java
public boolean waitForAll​(long ms)
throws
InterruptedException
```

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading, or until the length of time specified in milliseconds
by the

ms

argument has passed.

If there is an error while loading or scaling an image, then
that image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:** ms

- the number of milliseconds to wait
for the loading to complete
**Returns:** true

if all images were successfully
loaded;

false

otherwise
**Throws:** InterruptedException

- if any thread has
interrupted this thread.
**See Also:** waitForID(int)

,

waitForAll(long)

,

isErrorAny()

,

isErrorID(int)

- statusAll

```java
public int statusAll​(boolean load)
```

Calculates and returns the bitwise inclusive

OR

of the
status of all media that are tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

**Parameters:** load

- if

true

, start loading
any images that are not yet being loaded
**Returns:** the bitwise inclusive

OR

of the status of
all of the media being tracked
**See Also:** statusID(int, boolean)

,

LOADING

,

ABORTED

,

ERRORED

,

COMPLETE

- checkID

```java
public boolean checkID​(int id)
```

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:** id

- the identifier of the images to check
**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkID(int, boolean)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

- checkID

```java
public boolean checkID​(int id,
boolean load)
```

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:** id

- the identifier of the images to check
**Parameters:** load

- if

true

, start loading any
images that are not yet being loaded
**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkID(int, boolean)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

- isErrorID

```java
public boolean isErrorID​(int id)
```

Checks the error status of all of the images tracked by this
media tracker with the specified identifier.

**Parameters:** id

- the identifier of the images to check
**Returns:** true

if any of the images with the
specified identifier had an error during
loading;

false

otherwise
**See Also:** isErrorAny()

,

getErrorsID(int)

- getErrorsID

```java
public
Object
[] getErrorsID​(int id)
```

Returns a list of media with the specified ID that
have encountered an error.

**Parameters:** id

- the identifier of the images to check
**Returns:** an array of media objects tracked by this media
tracker with the specified identifier
that have encountered an error, or

null

if there are none with errors
**See Also:** isErrorID(int)

,

isErrorAny()

,

getErrorsAny()

- waitForID

```java
public void waitForID​(int id)
throws
InterruptedException
```

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

**Parameters:** id

- the identifier of the images to check
**Throws:** InterruptedException

- if any thread has
interrupted this thread.
**See Also:** waitForAll()

,

isErrorAny()

,

isErrorID(int)

- waitForID

```java
public boolean waitForID​(int id,
long ms)
throws
InterruptedException
```

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading, or until the
length of time specified in milliseconds by the

ms

argument has passed.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

statusID

,

isErrorID

, and

isErrorAny

methods to check for errors.

**Parameters:** id

- the identifier of the images to check
**Parameters:** ms

- the length of time, in milliseconds, to wait
for the loading to complete
**Returns:** true

if the loading completed in time;
otherwise

false
**Throws:** InterruptedException

- if any thread has
interrupted this thread.
**See Also:** waitForAll()

,

waitForID(int)

,

statusID(int, boolean)

,

isErrorAny()

,

isErrorID(int)

- statusID

```java
public int statusID​(int id,
boolean load)
```

Calculates and returns the bitwise inclusive

OR

of the
status of all media with the specified identifier that are
tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

**Parameters:** id

- the identifier of the images to check
**Parameters:** load

- if

true

, start loading
any images that are not yet being loaded
**Returns:** the bitwise inclusive

OR

of the status of
all of the media with the specified
identifier that are being tracked
**See Also:** statusAll(boolean)

,

LOADING

,

ABORTED

,

ERRORED

,

COMPLETE

- removeImage

```java
public void removeImage​(
Image
image)
```

Removes the specified image from this media tracker.
All instances of the specified image are removed,
regardless of scale or ID.

**Parameters:** image

- the image to be removed
**Since:** 1.1
**See Also:** removeImage(java.awt.Image, int)

,

removeImage(java.awt.Image, int, int, int)

- removeImage

```java
public void removeImage​(
Image
image,
int id)
```

Removes the specified image from the specified tracking
ID of this media tracker.
All instances of

Image

being tracked
under the specified ID are removed regardless of scale.

**Parameters:** image

- the image to be removed
**Parameters:** id

- the tracking ID from which to remove the image
**Since:** 1.1
**See Also:** removeImage(java.awt.Image)

,

removeImage(java.awt.Image, int, int, int)

- removeImage

```java
public void removeImage​(
Image
image,
int id,
int width,
int height)
```

Removes the specified image with the specified
width, height, and ID from this media tracker.
Only the specified instance (with any duplicates) is removed.

**Parameters:** image

- the image to be removed
**Parameters:** id

- the tracking ID from which to remove the image
**Parameters:** width

- the width to remove (-1 for unscaled)
**Parameters:** height

- the height to remove (-1 for unscaled)
**Since:** 1.1
**See Also:** removeImage(java.awt.Image)

,

removeImage(java.awt.Image, int)

Field Detail

- LOADING

```java
public static final int LOADING
```

Flag indicating that media is currently being loaded.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

- ABORTED

```java
public static final int ABORTED
```

Flag indicating that the downloading of media was aborted.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

- ERRORED

```java
public static final int ERRORED
```

Flag indicating that the downloading of media encountered
an error.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

- COMPLETE

```java
public static final int COMPLETE
```

Flag indicating that the downloading of media was completed
successfully.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

---

#### Field Detail

LOADING

```java
public static final int LOADING
```

Flag indicating that media is currently being loaded.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

---

#### LOADING

public static final int LOADING

Flag indicating that media is currently being loaded.

ABORTED

```java
public static final int ABORTED
```

Flag indicating that the downloading of media was aborted.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

---

#### ABORTED

public static final int ABORTED

Flag indicating that the downloading of media was aborted.

ERRORED

```java
public static final int ERRORED
```

Flag indicating that the downloading of media encountered
an error.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

---

#### ERRORED

public static final int ERRORED

Flag indicating that the downloading of media encountered
an error.

COMPLETE

```java
public static final int COMPLETE
```

Flag indicating that the downloading of media was completed
successfully.

**See Also:** statusAll(boolean)

,

statusID(int, boolean)

,

Constant Field Values

---

#### COMPLETE

public static final int COMPLETE

Flag indicating that the downloading of media was completed
successfully.

Constructor Detail

- MediaTracker

```java
public MediaTracker​(
Component
comp)
```

Creates a media tracker to track images for a given component.

**Parameters:** comp

- the component on which the images
will eventually be drawn

---

#### Constructor Detail

MediaTracker

```java
public MediaTracker​(
Component
comp)
```

Creates a media tracker to track images for a given component.

**Parameters:** comp

- the component on which the images
will eventually be drawn

---

#### MediaTracker

public MediaTracker​(

Component

comp)

Creates a media tracker to track images for a given component.

Method Detail

- addImage

```java
public void addImage​(
Image
image,
int id)
```

Adds an image to the list of images being tracked by this media
tracker. The image will eventually be rendered at its default
(unscaled) size.

**Parameters:** image

- the image to be tracked
**Parameters:** id

- an identifier used to track this image

- addImage

```java
public void addImage​(
Image
image,
int id,
int w,
int h)
```

Adds a scaled image to the list of images being tracked
by this media tracker. The image will eventually be
rendered at the indicated width and height.

**Parameters:** image

- the image to be tracked
**Parameters:** id

- an identifier that can be used to track this image
**Parameters:** w

- the width at which the image is rendered
**Parameters:** h

- the height at which the image is rendered

- checkAll

```java
public boolean checkAll()
```

Checks to see if all images being tracked by this media tracker
have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkAll(boolean)

,

checkID(int)

,

isErrorAny()

,

isErrorID(int)

- checkAll

```java
public boolean checkAll​(boolean load)
```

Checks to see if all images being tracked by this media tracker
have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

**Parameters:** load

- if

true

, start loading any
images that are not yet being loaded
**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkID(int)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

- isErrorAny

```java
public boolean isErrorAny()
```

Checks the error status of all of the images.

**Returns:** true

if any of the images tracked
by this media tracker had an error during
loading;

false

otherwise
**See Also:** isErrorID(int)

,

getErrorsAny()

- getErrorsAny

```java
public
Object
[] getErrorsAny()
```

Returns a list of all media that have encountered an error.

**Returns:** an array of media objects tracked by this
media tracker that have encountered
an error, or

null

if
there are none with errors
**See Also:** isErrorAny()

,

getErrorsID(int)

- waitForAll

```java
public void waitForAll()
throws
InterruptedException
```

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Throws:** InterruptedException

- if any thread has
interrupted this thread
**See Also:** waitForID(int)

,

waitForAll(long)

,

isErrorAny()

,

isErrorID(int)

- waitForAll

```java
public boolean waitForAll​(long ms)
throws
InterruptedException
```

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading, or until the length of time specified in milliseconds
by the

ms

argument has passed.

If there is an error while loading or scaling an image, then
that image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:** ms

- the number of milliseconds to wait
for the loading to complete
**Returns:** true

if all images were successfully
loaded;

false

otherwise
**Throws:** InterruptedException

- if any thread has
interrupted this thread.
**See Also:** waitForID(int)

,

waitForAll(long)

,

isErrorAny()

,

isErrorID(int)

- statusAll

```java
public int statusAll​(boolean load)
```

Calculates and returns the bitwise inclusive

OR

of the
status of all media that are tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

**Parameters:** load

- if

true

, start loading
any images that are not yet being loaded
**Returns:** the bitwise inclusive

OR

of the status of
all of the media being tracked
**See Also:** statusID(int, boolean)

,

LOADING

,

ABORTED

,

ERRORED

,

COMPLETE

- checkID

```java
public boolean checkID​(int id)
```

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:** id

- the identifier of the images to check
**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkID(int, boolean)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

- checkID

```java
public boolean checkID​(int id,
boolean load)
```

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:** id

- the identifier of the images to check
**Parameters:** load

- if

true

, start loading any
images that are not yet being loaded
**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkID(int, boolean)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

- isErrorID

```java
public boolean isErrorID​(int id)
```

Checks the error status of all of the images tracked by this
media tracker with the specified identifier.

**Parameters:** id

- the identifier of the images to check
**Returns:** true

if any of the images with the
specified identifier had an error during
loading;

false

otherwise
**See Also:** isErrorAny()

,

getErrorsID(int)

- getErrorsID

```java
public
Object
[] getErrorsID​(int id)
```

Returns a list of media with the specified ID that
have encountered an error.

**Parameters:** id

- the identifier of the images to check
**Returns:** an array of media objects tracked by this media
tracker with the specified identifier
that have encountered an error, or

null

if there are none with errors
**See Also:** isErrorID(int)

,

isErrorAny()

,

getErrorsAny()

- waitForID

```java
public void waitForID​(int id)
throws
InterruptedException
```

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

**Parameters:** id

- the identifier of the images to check
**Throws:** InterruptedException

- if any thread has
interrupted this thread.
**See Also:** waitForAll()

,

isErrorAny()

,

isErrorID(int)

- waitForID

```java
public boolean waitForID​(int id,
long ms)
throws
InterruptedException
```

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading, or until the
length of time specified in milliseconds by the

ms

argument has passed.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

statusID

,

isErrorID

, and

isErrorAny

methods to check for errors.

**Parameters:** id

- the identifier of the images to check
**Parameters:** ms

- the length of time, in milliseconds, to wait
for the loading to complete
**Returns:** true

if the loading completed in time;
otherwise

false
**Throws:** InterruptedException

- if any thread has
interrupted this thread.
**See Also:** waitForAll()

,

waitForID(int)

,

statusID(int, boolean)

,

isErrorAny()

,

isErrorID(int)

- statusID

```java
public int statusID​(int id,
boolean load)
```

Calculates and returns the bitwise inclusive

OR

of the
status of all media with the specified identifier that are
tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

**Parameters:** id

- the identifier of the images to check
**Parameters:** load

- if

true

, start loading
any images that are not yet being loaded
**Returns:** the bitwise inclusive

OR

of the status of
all of the media with the specified
identifier that are being tracked
**See Also:** statusAll(boolean)

,

LOADING

,

ABORTED

,

ERRORED

,

COMPLETE

- removeImage

```java
public void removeImage​(
Image
image)
```

Removes the specified image from this media tracker.
All instances of the specified image are removed,
regardless of scale or ID.

**Parameters:** image

- the image to be removed
**Since:** 1.1
**See Also:** removeImage(java.awt.Image, int)

,

removeImage(java.awt.Image, int, int, int)

- removeImage

```java
public void removeImage​(
Image
image,
int id)
```

Removes the specified image from the specified tracking
ID of this media tracker.
All instances of

Image

being tracked
under the specified ID are removed regardless of scale.

**Parameters:** image

- the image to be removed
**Parameters:** id

- the tracking ID from which to remove the image
**Since:** 1.1
**See Also:** removeImage(java.awt.Image)

,

removeImage(java.awt.Image, int, int, int)

- removeImage

```java
public void removeImage​(
Image
image,
int id,
int width,
int height)
```

Removes the specified image with the specified
width, height, and ID from this media tracker.
Only the specified instance (with any duplicates) is removed.

**Parameters:** image

- the image to be removed
**Parameters:** id

- the tracking ID from which to remove the image
**Parameters:** width

- the width to remove (-1 for unscaled)
**Parameters:** height

- the height to remove (-1 for unscaled)
**Since:** 1.1
**See Also:** removeImage(java.awt.Image)

,

removeImage(java.awt.Image, int)

---

#### Method Detail

addImage

```java
public void addImage​(
Image
image,
int id)
```

Adds an image to the list of images being tracked by this media
tracker. The image will eventually be rendered at its default
(unscaled) size.

**Parameters:** image

- the image to be tracked
**Parameters:** id

- an identifier used to track this image

---

#### addImage

public void addImage​(

Image

image,
int id)

Adds an image to the list of images being tracked by this media
tracker. The image will eventually be rendered at its default
(unscaled) size.

addImage

```java
public void addImage​(
Image
image,
int id,
int w,
int h)
```

Adds a scaled image to the list of images being tracked
by this media tracker. The image will eventually be
rendered at the indicated width and height.

**Parameters:** image

- the image to be tracked
**Parameters:** id

- an identifier that can be used to track this image
**Parameters:** w

- the width at which the image is rendered
**Parameters:** h

- the height at which the image is rendered

---

#### addImage

public void addImage​(

Image

image,
int id,
int w,
int h)

Adds a scaled image to the list of images being tracked
by this media tracker. The image will eventually be
rendered at the indicated width and height.

checkAll

```java
public boolean checkAll()
```

Checks to see if all images being tracked by this media tracker
have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkAll(boolean)

,

checkID(int)

,

isErrorAny()

,

isErrorID(int)

---

#### checkAll

public boolean checkAll()

Checks to see if all images being tracked by this media tracker
have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

checkAll

```java
public boolean checkAll​(boolean load)
```

Checks to see if all images being tracked by this media tracker
have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

**Parameters:** load

- if

true

, start loading any
images that are not yet being loaded
**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkID(int)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

---

#### checkAll

public boolean checkAll​(boolean load)

Checks to see if all images being tracked by this media tracker
have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

If there is an error while loading or scaling an image, that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

isErrorAny

```java
public boolean isErrorAny()
```

Checks the error status of all of the images.

**Returns:** true

if any of the images tracked
by this media tracker had an error during
loading;

false

otherwise
**See Also:** isErrorID(int)

,

getErrorsAny()

---

#### isErrorAny

public boolean isErrorAny()

Checks the error status of all of the images.

getErrorsAny

```java
public
Object
[] getErrorsAny()
```

Returns a list of all media that have encountered an error.

**Returns:** an array of media objects tracked by this
media tracker that have encountered
an error, or

null

if
there are none with errors
**See Also:** isErrorAny()

,

getErrorsID(int)

---

#### getErrorsAny

public

Object

[] getErrorsAny()

Returns a list of all media that have encountered an error.

waitForAll

```java
public void waitForAll()
throws
InterruptedException
```

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Throws:** InterruptedException

- if any thread has
interrupted this thread
**See Also:** waitForID(int)

,

waitForAll(long)

,

isErrorAny()

,

isErrorID(int)

---

#### waitForAll

public void waitForAll()
throws

InterruptedException

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

waitForAll

```java
public boolean waitForAll​(long ms)
throws
InterruptedException
```

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading, or until the length of time specified in milliseconds
by the

ms

argument has passed.

If there is an error while loading or scaling an image, then
that image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:** ms

- the number of milliseconds to wait
for the loading to complete
**Returns:** true

if all images were successfully
loaded;

false

otherwise
**Throws:** InterruptedException

- if any thread has
interrupted this thread.
**See Also:** waitForID(int)

,

waitForAll(long)

,

isErrorAny()

,

isErrorID(int)

---

#### waitForAll

public boolean waitForAll​(long ms)
throws

InterruptedException

Starts loading all images tracked by this media tracker. This
method waits until all the images being tracked have finished
loading, or until the length of time specified in milliseconds
by the

ms

argument has passed.

If there is an error while loading or scaling an image, then
that image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

If there is an error while loading or scaling an image, then
that image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

statusAll

```java
public int statusAll​(boolean load)
```

Calculates and returns the bitwise inclusive

OR

of the
status of all media that are tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

**Parameters:** load

- if

true

, start loading
any images that are not yet being loaded
**Returns:** the bitwise inclusive

OR

of the status of
all of the media being tracked
**See Also:** statusID(int, boolean)

,

LOADING

,

ABORTED

,

ERRORED

,

COMPLETE

---

#### statusAll

public int statusAll​(boolean load)

Calculates and returns the bitwise inclusive

OR

of the
status of all media that are tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

checkID

```java
public boolean checkID​(int id)
```

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:** id

- the identifier of the images to check
**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkID(int, boolean)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

---

#### checkID

public boolean checkID​(int id)

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

This method does not start loading the images if they are not
already loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

checkID

```java
public boolean checkID​(int id,
boolean load)
```

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

**Parameters:** id

- the identifier of the images to check
**Parameters:** load

- if

true

, start loading any
images that are not yet being loaded
**Returns:** true

if all images have finished loading,
have been aborted, or have encountered
an error;

false

otherwise
**See Also:** checkID(int, boolean)

,

checkAll()

,

isErrorAny()

,

isErrorID(int)

---

#### checkID

public boolean checkID​(int id,
boolean load)

Checks to see if all images tracked by this media tracker that
are tagged with the specified identifier have finished loading.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

If the value of the

load

flag is

true

,
then this method starts loading any images that are not yet
being loaded.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

or

isErrorID

methods to
check for errors.

isErrorID

```java
public boolean isErrorID​(int id)
```

Checks the error status of all of the images tracked by this
media tracker with the specified identifier.

**Parameters:** id

- the identifier of the images to check
**Returns:** true

if any of the images with the
specified identifier had an error during
loading;

false

otherwise
**See Also:** isErrorAny()

,

getErrorsID(int)

---

#### isErrorID

public boolean isErrorID​(int id)

Checks the error status of all of the images tracked by this
media tracker with the specified identifier.

getErrorsID

```java
public
Object
[] getErrorsID​(int id)
```

Returns a list of media with the specified ID that
have encountered an error.

**Parameters:** id

- the identifier of the images to check
**Returns:** an array of media objects tracked by this media
tracker with the specified identifier
that have encountered an error, or

null

if there are none with errors
**See Also:** isErrorID(int)

,

isErrorAny()

,

getErrorsAny()

---

#### getErrorsID

public

Object

[] getErrorsID​(int id)

Returns a list of media with the specified ID that
have encountered an error.

waitForID

```java
public void waitForID​(int id)
throws
InterruptedException
```

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

**Parameters:** id

- the identifier of the images to check
**Throws:** InterruptedException

- if any thread has
interrupted this thread.
**See Also:** waitForAll()

,

isErrorAny()

,

isErrorID(int)

---

#### waitForID

public void waitForID​(int id)
throws

InterruptedException

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

isErrorAny

and

isErrorID

methods to
check for errors.

waitForID

```java
public boolean waitForID​(int id,
long ms)
throws
InterruptedException
```

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading, or until the
length of time specified in milliseconds by the

ms

argument has passed.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

statusID

,

isErrorID

, and

isErrorAny

methods to check for errors.

**Parameters:** id

- the identifier of the images to check
**Parameters:** ms

- the length of time, in milliseconds, to wait
for the loading to complete
**Returns:** true

if the loading completed in time;
otherwise

false
**Throws:** InterruptedException

- if any thread has
interrupted this thread.
**See Also:** waitForAll()

,

waitForID(int)

,

statusID(int, boolean)

,

isErrorAny()

,

isErrorID(int)

---

#### waitForID

public boolean waitForID​(int id,
long ms)
throws

InterruptedException

Starts loading all images tracked by this media tracker with the
specified identifier. This method waits until all the images with
the specified identifier have finished loading, or until the
length of time specified in milliseconds by the

ms

argument has passed.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

statusID

,

isErrorID

, and

isErrorAny

methods to check for errors.

If there is an error while loading or scaling an image, then that
image is considered to have finished loading. Use the

statusID

,

isErrorID

, and

isErrorAny

methods to check for errors.

statusID

```java
public int statusID​(int id,
boolean load)
```

Calculates and returns the bitwise inclusive

OR

of the
status of all media with the specified identifier that are
tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

**Parameters:** id

- the identifier of the images to check
**Parameters:** load

- if

true

, start loading
any images that are not yet being loaded
**Returns:** the bitwise inclusive

OR

of the status of
all of the media with the specified
identifier that are being tracked
**See Also:** statusAll(boolean)

,

LOADING

,

ABORTED

,

ERRORED

,

COMPLETE

---

#### statusID

public int statusID​(int id,
boolean load)

Calculates and returns the bitwise inclusive

OR

of the
status of all media with the specified identifier that are
tracked by this media tracker.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

Possible flags defined by the

MediaTracker

class are

LOADING

,

ABORTED

,

ERRORED

, and

COMPLETE

. An image that hasn't started
loading has zero as its status.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

If the value of

load

is

true

, then
this method starts loading any images that are not yet being loaded.

removeImage

```java
public void removeImage​(
Image
image)
```

Removes the specified image from this media tracker.
All instances of the specified image are removed,
regardless of scale or ID.

**Parameters:** image

- the image to be removed
**Since:** 1.1
**See Also:** removeImage(java.awt.Image, int)

,

removeImage(java.awt.Image, int, int, int)

---

#### removeImage

public void removeImage​(

Image

image)

Removes the specified image from this media tracker.
All instances of the specified image are removed,
regardless of scale or ID.

removeImage

```java
public void removeImage​(
Image
image,
int id)
```

Removes the specified image from the specified tracking
ID of this media tracker.
All instances of

Image

being tracked
under the specified ID are removed regardless of scale.

**Parameters:** image

- the image to be removed
**Parameters:** id

- the tracking ID from which to remove the image
**Since:** 1.1
**See Also:** removeImage(java.awt.Image)

,

removeImage(java.awt.Image, int, int, int)

---

#### removeImage

public void removeImage​(

Image

image,
int id)

Removes the specified image from the specified tracking
ID of this media tracker.
All instances of

Image

being tracked
under the specified ID are removed regardless of scale.

removeImage

```java
public void removeImage​(
Image
image,
int id,
int width,
int height)
```

Removes the specified image with the specified
width, height, and ID from this media tracker.
Only the specified instance (with any duplicates) is removed.

**Parameters:** image

- the image to be removed
**Parameters:** id

- the tracking ID from which to remove the image
**Parameters:** width

- the width to remove (-1 for unscaled)
**Parameters:** height

- the height to remove (-1 for unscaled)
**Since:** 1.1
**See Also:** removeImage(java.awt.Image)

,

removeImage(java.awt.Image, int)

---

#### removeImage

public void removeImage​(

Image

image,
int id,
int width,
int height)

Removes the specified image with the specified
width, height, and ID from this media tracker.
Only the specified instance (with any duplicates) is removed.

---

