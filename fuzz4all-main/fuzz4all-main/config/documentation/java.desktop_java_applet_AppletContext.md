# Interface AppletContext

**Source:** `java.desktop\java\applet\AppletContext.html`

### Class Description

```java
@Deprecated
(
since
="9")
public interface
AppletContext
```

This interface corresponds to an applet's environment: the
document containing the applet and the other applets in the same
document.

The methods in this interface can be used by an applet to obtain
information about its environment.

**Since:** 1.0

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### AudioClip
getAudioClip​(
URL
url)

Creates an audio clip.

**Parameters:**
- url

- an absolute URL giving the location of the audio clip.

**Returns:**
- the audio clip at the specified URL.

---

#### Image
getImage​(
URL
url)

Returns an

Image

object that can then be painted on
the screen. The

url

argument that is
passed as an argument must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When the applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:**
- url

- an absolute URL giving the location of the image.

**Returns:**
- the image at the specified URL.

**See Also:**
- Image

---

#### Applet
getApplet​(
String
name)

Finds and returns the applet in the document represented by this
applet context with the given name. The name can be set in the
HTML tag by setting the

name

attribute.

**Parameters:**
- name

- an applet name.

**Returns:**
- the applet with the given name, or

null

if
not found.

---

#### Enumeration
<
Applet
> getApplets()

Finds all the applets in the document represented by this applet
context.

**Returns:**
- an enumeration of all applets in the document represented by
this applet context.

---

#### void showDocument​(
URL
url)

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The browser or
applet viewer determines which window or frame to display the
Web page. This method may be ignored by applet contexts that
are not browsers.

**Parameters:**
- url

- an absolute URL giving the location of the document.

---

#### void showDocument​(
URL
url,

String
target)

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The

target

argument indicates in which HTML frame the
document is to be displayed.
The target argument is interpreted as follows:

Target arguments and their descriptions

Target Argument

Description

"_self"

Show in the window and frame that contain the applet.

"_parent"

Show in the applet's parent frame. If the applet's frame has no
parent frame, acts the same as "_self".

"_top"

Show in the top-level frame of the applet's window. If the
applet's frame is the top-level frame, acts the same as "_self".

"_blank"

Show in a new, unnamed top-level window.

name

Show in the frame or window named

name

. If a target named

name

does not already exist, a new top-level window with the
specified name is created, and the document is shown there.

An applet viewer or browser is free to ignore

showDocument

.

**Parameters:**
- url

- an absolute URL giving the location of the document.
- target

- a

String

indicating where to display
the page.

---

#### void showStatus​(
String
status)

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

**Parameters:**
- status

- a string to display in the status window.

---

#### void setStream​(
String
key,

InputStream
stream)
throws
IOException

Associates the specified stream with the specified key in this
applet context. If the applet context previously contained a mapping
for this key, the old value is replaced.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Parameters:**
- key

- key with which the specified value is to be associated.
- stream

- stream to be associated with the specified key. If this
parameter is

null

, the specified key is removed
in this applet context.

**Throws:**
- IOException

- if the stream size exceeds a certain
size limit. Size limit is decided by the implementor of this
interface.

**Since:**
- 1.4

---

#### InputStream
getStream​(
String
key)

Returns the stream to which specified key is associated within this
applet context. Returns

null

if the applet context contains
no stream for this key.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Parameters:**
- key

- key whose associated stream is to be returned.

**Returns:**
- the stream to which this applet context maps the key

**Since:**
- 1.4

---

#### Iterator
<
String
> getStreamKeys()

Finds all the keys of the streams in this applet context.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Returns:**
- an Iterator of all the names of the streams in this applet
context.

**Since:**
- 1.4

---

### Additional Sections

#### Interface AppletContext

```java
@Deprecated
(
since
="9")
public interface
AppletContext
```

Deprecated.

The Applet API is deprecated, no replacement.

This interface corresponds to an applet's environment: the
document containing the applet and the other applets in the same
document.

The methods in this interface can be used by an applet to obtain
information about its environment.

**Since:** 1.0

@Deprecated

(

since

="9")
public interface

AppletContext

This interface corresponds to an applet's environment: the
document containing the applet and the other applets in the same
document.

The methods in this interface can be used by an applet to obtain
information about its environment.

The methods in this interface can be used by an applet to obtain
information about its environment.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Applet

getApplet

​(

String

name)

Deprecated.

Finds and returns the applet in the document represented by this
applet context with the given name.

Enumeration

<

Applet

>

getApplets

()

Deprecated.

Finds all the applets in the document represented by this applet
context.

AudioClip

getAudioClip

​(

URL

url)

Deprecated.

Creates an audio clip.

Image

getImage

​(

URL

url)

Deprecated.

Returns an

Image

object that can then be painted on
the screen.

InputStream

getStream

​(

String

key)

Deprecated.

Returns the stream to which specified key is associated within this
applet context.

Iterator

<

String

>

getStreamKeys

()

Deprecated.

Finds all the keys of the streams in this applet context.

void

setStream

​(

String

key,

InputStream

stream)

Deprecated.

Associates the specified stream with the specified key in this
applet context.

void

showDocument

​(

URL

url)

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument.

void

showDocument

​(

URL

url,

String

target)

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument.

void

showStatus

​(

String

status)

Deprecated.

Requests that the argument string be displayed in the
"status window".

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Applet

getApplet

​(

String

name)

Deprecated.

Finds and returns the applet in the document represented by this
applet context with the given name.

Enumeration

<

Applet

>

getApplets

()

Deprecated.

Finds all the applets in the document represented by this applet
context.

AudioClip

getAudioClip

​(

URL

url)

Deprecated.

Creates an audio clip.

Image

getImage

​(

URL

url)

Deprecated.

Returns an

Image

object that can then be painted on
the screen.

InputStream

getStream

​(

String

key)

Deprecated.

Returns the stream to which specified key is associated within this
applet context.

Iterator

<

String

>

getStreamKeys

()

Deprecated.

Finds all the keys of the streams in this applet context.

void

setStream

​(

String

key,

InputStream

stream)

Deprecated.

Associates the specified stream with the specified key in this
applet context.

void

showDocument

​(

URL

url)

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument.

void

showDocument

​(

URL

url,

String

target)

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument.

void

showStatus

​(

String

status)

Deprecated.

Requests that the argument string be displayed in the
"status window".

---

#### Method Summary

Deprecated.

Finds and returns the applet in the document represented by this
applet context with the given name.

Finds all the applets in the document represented by this applet
context.

Creates an audio clip.

Returns an

Image

object that can then be painted on
the screen.

Returns the stream to which specified key is associated within this
applet context.

Finds all the keys of the streams in this applet context.

Associates the specified stream with the specified key in this
applet context.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument.

Requests that the argument string be displayed in the
"status window".

============ METHOD DETAIL ==========

- Method Detail

- getAudioClip

```java
AudioClip
getAudioClip​(
URL
url)
```

Deprecated.

Creates an audio clip.

**Parameters:** url

- an absolute URL giving the location of the audio clip.
**Returns:** the audio clip at the specified URL.

- getImage

```java
Image
getImage​(
URL
url)
```

Deprecated.

Returns an

Image

object that can then be painted on
the screen. The

url

argument that is
passed as an argument must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When the applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:** url

- an absolute URL giving the location of the image.
**Returns:** the image at the specified URL.
**See Also:** Image

- getApplet

```java
Applet
getApplet​(
String
name)
```

Deprecated.

Finds and returns the applet in the document represented by this
applet context with the given name. The name can be set in the
HTML tag by setting the

name

attribute.

**Parameters:** name

- an applet name.
**Returns:** the applet with the given name, or

null

if
not found.

- getApplets

```java
Enumeration
<
Applet
> getApplets()
```

Deprecated.

Finds all the applets in the document represented by this applet
context.

**Returns:** an enumeration of all applets in the document represented by
this applet context.

- showDocument

```java
void showDocument​(
URL
url)
```

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The browser or
applet viewer determines which window or frame to display the
Web page. This method may be ignored by applet contexts that
are not browsers.

**Parameters:** url

- an absolute URL giving the location of the document.

- showDocument

```java
void showDocument​(
URL
url,

String
target)
```

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The

target

argument indicates in which HTML frame the
document is to be displayed.
The target argument is interpreted as follows:

Target arguments and their descriptions

Target Argument

Description

"_self"

Show in the window and frame that contain the applet.

"_parent"

Show in the applet's parent frame. If the applet's frame has no
parent frame, acts the same as "_self".

"_top"

Show in the top-level frame of the applet's window. If the
applet's frame is the top-level frame, acts the same as "_self".

"_blank"

Show in a new, unnamed top-level window.

name

Show in the frame or window named

name

. If a target named

name

does not already exist, a new top-level window with the
specified name is created, and the document is shown there.

An applet viewer or browser is free to ignore

showDocument

.

**Parameters:** url

- an absolute URL giving the location of the document.
**Parameters:** target

- a

String

indicating where to display
the page.

- showStatus

```java
void showStatus​(
String
status)
```

Deprecated.

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

**Parameters:** status

- a string to display in the status window.

- setStream

```java
void setStream​(
String
key,

InputStream
stream)
throws
IOException
```

Deprecated.

Associates the specified stream with the specified key in this
applet context. If the applet context previously contained a mapping
for this key, the old value is replaced.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Parameters:** key

- key with which the specified value is to be associated.
**Parameters:** stream

- stream to be associated with the specified key. If this
parameter is

null

, the specified key is removed
in this applet context.
**Throws:** IOException

- if the stream size exceeds a certain
size limit. Size limit is decided by the implementor of this
interface.
**Since:** 1.4

- getStream

```java
InputStream
getStream​(
String
key)
```

Deprecated.

Returns the stream to which specified key is associated within this
applet context. Returns

null

if the applet context contains
no stream for this key.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Parameters:** key

- key whose associated stream is to be returned.
**Returns:** the stream to which this applet context maps the key
**Since:** 1.4

- getStreamKeys

```java
Iterator
<
String
> getStreamKeys()
```

Deprecated.

Finds all the keys of the streams in this applet context.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Returns:** an Iterator of all the names of the streams in this applet
context.
**Since:** 1.4

Method Detail

- getAudioClip

```java
AudioClip
getAudioClip​(
URL
url)
```

Deprecated.

Creates an audio clip.

**Parameters:** url

- an absolute URL giving the location of the audio clip.
**Returns:** the audio clip at the specified URL.

- getImage

```java
Image
getImage​(
URL
url)
```

Deprecated.

Returns an

Image

object that can then be painted on
the screen. The

url

argument that is
passed as an argument must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When the applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:** url

- an absolute URL giving the location of the image.
**Returns:** the image at the specified URL.
**See Also:** Image

- getApplet

```java
Applet
getApplet​(
String
name)
```

Deprecated.

Finds and returns the applet in the document represented by this
applet context with the given name. The name can be set in the
HTML tag by setting the

name

attribute.

**Parameters:** name

- an applet name.
**Returns:** the applet with the given name, or

null

if
not found.

- getApplets

```java
Enumeration
<
Applet
> getApplets()
```

Deprecated.

Finds all the applets in the document represented by this applet
context.

**Returns:** an enumeration of all applets in the document represented by
this applet context.

- showDocument

```java
void showDocument​(
URL
url)
```

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The browser or
applet viewer determines which window or frame to display the
Web page. This method may be ignored by applet contexts that
are not browsers.

**Parameters:** url

- an absolute URL giving the location of the document.

- showDocument

```java
void showDocument​(
URL
url,

String
target)
```

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The

target

argument indicates in which HTML frame the
document is to be displayed.
The target argument is interpreted as follows:

Target arguments and their descriptions

Target Argument

Description

"_self"

Show in the window and frame that contain the applet.

"_parent"

Show in the applet's parent frame. If the applet's frame has no
parent frame, acts the same as "_self".

"_top"

Show in the top-level frame of the applet's window. If the
applet's frame is the top-level frame, acts the same as "_self".

"_blank"

Show in a new, unnamed top-level window.

name

Show in the frame or window named

name

. If a target named

name

does not already exist, a new top-level window with the
specified name is created, and the document is shown there.

An applet viewer or browser is free to ignore

showDocument

.

**Parameters:** url

- an absolute URL giving the location of the document.
**Parameters:** target

- a

String

indicating where to display
the page.

- showStatus

```java
void showStatus​(
String
status)
```

Deprecated.

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

**Parameters:** status

- a string to display in the status window.

- setStream

```java
void setStream​(
String
key,

InputStream
stream)
throws
IOException
```

Deprecated.

Associates the specified stream with the specified key in this
applet context. If the applet context previously contained a mapping
for this key, the old value is replaced.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Parameters:** key

- key with which the specified value is to be associated.
**Parameters:** stream

- stream to be associated with the specified key. If this
parameter is

null

, the specified key is removed
in this applet context.
**Throws:** IOException

- if the stream size exceeds a certain
size limit. Size limit is decided by the implementor of this
interface.
**Since:** 1.4

- getStream

```java
InputStream
getStream​(
String
key)
```

Deprecated.

Returns the stream to which specified key is associated within this
applet context. Returns

null

if the applet context contains
no stream for this key.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Parameters:** key

- key whose associated stream is to be returned.
**Returns:** the stream to which this applet context maps the key
**Since:** 1.4

- getStreamKeys

```java
Iterator
<
String
> getStreamKeys()
```

Deprecated.

Finds all the keys of the streams in this applet context.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Returns:** an Iterator of all the names of the streams in this applet
context.
**Since:** 1.4

---

#### Method Detail

getAudioClip

```java
AudioClip
getAudioClip​(
URL
url)
```

Deprecated.

Creates an audio clip.

**Parameters:** url

- an absolute URL giving the location of the audio clip.
**Returns:** the audio clip at the specified URL.

---

#### getAudioClip

AudioClip

getAudioClip​(

URL

url)

Creates an audio clip.

getImage

```java
Image
getImage​(
URL
url)
```

Deprecated.

Returns an

Image

object that can then be painted on
the screen. The

url

argument that is
passed as an argument must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When the applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:** url

- an absolute URL giving the location of the image.
**Returns:** the image at the specified URL.
**See Also:** Image

---

#### getImage

Image

getImage​(

URL

url)

Returns an

Image

object that can then be painted on
the screen. The

url

argument that is
passed as an argument must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When the applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

This method always returns immediately, whether or not the image
exists. When the applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

getApplet

```java
Applet
getApplet​(
String
name)
```

Deprecated.

Finds and returns the applet in the document represented by this
applet context with the given name. The name can be set in the
HTML tag by setting the

name

attribute.

**Parameters:** name

- an applet name.
**Returns:** the applet with the given name, or

null

if
not found.

---

#### getApplet

Applet

getApplet​(

String

name)

Finds and returns the applet in the document represented by this
applet context with the given name. The name can be set in the
HTML tag by setting the

name

attribute.

getApplets

```java
Enumeration
<
Applet
> getApplets()
```

Deprecated.

Finds all the applets in the document represented by this applet
context.

**Returns:** an enumeration of all applets in the document represented by
this applet context.

---

#### getApplets

Enumeration

<

Applet

> getApplets()

Finds all the applets in the document represented by this applet
context.

showDocument

```java
void showDocument​(
URL
url)
```

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The browser or
applet viewer determines which window or frame to display the
Web page. This method may be ignored by applet contexts that
are not browsers.

**Parameters:** url

- an absolute URL giving the location of the document.

---

#### showDocument

void showDocument​(

URL

url)

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The browser or
applet viewer determines which window or frame to display the
Web page. This method may be ignored by applet contexts that
are not browsers.

showDocument

```java
void showDocument​(
URL
url,

String
target)
```

Deprecated.

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The

target

argument indicates in which HTML frame the
document is to be displayed.
The target argument is interpreted as follows:

Target arguments and their descriptions

Target Argument

Description

"_self"

Show in the window and frame that contain the applet.

"_parent"

Show in the applet's parent frame. If the applet's frame has no
parent frame, acts the same as "_self".

"_top"

Show in the top-level frame of the applet's window. If the
applet's frame is the top-level frame, acts the same as "_self".

"_blank"

Show in a new, unnamed top-level window.

name

Show in the frame or window named

name

. If a target named

name

does not already exist, a new top-level window with the
specified name is created, and the document is shown there.

An applet viewer or browser is free to ignore

showDocument

.

**Parameters:** url

- an absolute URL giving the location of the document.
**Parameters:** target

- a

String

indicating where to display
the page.

---

#### showDocument

void showDocument​(

URL

url,

String

target)

Requests that the browser or applet viewer show the Web page
indicated by the

url

argument. The

target

argument indicates in which HTML frame the
document is to be displayed.
The target argument is interpreted as follows:

Target arguments and their descriptions

Target Argument

Description

"_self"

Show in the window and frame that contain the applet.

"_parent"

Show in the applet's parent frame. If the applet's frame has no
parent frame, acts the same as "_self".

"_top"

Show in the top-level frame of the applet's window. If the
applet's frame is the top-level frame, acts the same as "_self".

"_blank"

Show in a new, unnamed top-level window.

name

Show in the frame or window named

name

. If a target named

name

does not already exist, a new top-level window with the
specified name is created, and the document is shown there.

An applet viewer or browser is free to ignore

showDocument

.

An applet viewer or browser is free to ignore

showDocument

.

showStatus

```java
void showStatus​(
String
status)
```

Deprecated.

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

**Parameters:** status

- a string to display in the status window.

---

#### showStatus

void showStatus​(

String

status)

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

setStream

```java
void setStream​(
String
key,

InputStream
stream)
throws
IOException
```

Deprecated.

Associates the specified stream with the specified key in this
applet context. If the applet context previously contained a mapping
for this key, the old value is replaced.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Parameters:** key

- key with which the specified value is to be associated.
**Parameters:** stream

- stream to be associated with the specified key. If this
parameter is

null

, the specified key is removed
in this applet context.
**Throws:** IOException

- if the stream size exceeds a certain
size limit. Size limit is decided by the implementor of this
interface.
**Since:** 1.4

---

#### setStream

void setStream​(

String

key,

InputStream

stream)
throws

IOException

Associates the specified stream with the specified key in this
applet context. If the applet context previously contained a mapping
for this key, the old value is replaced.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

getStream

```java
InputStream
getStream​(
String
key)
```

Deprecated.

Returns the stream to which specified key is associated within this
applet context. Returns

null

if the applet context contains
no stream for this key.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Parameters:** key

- key whose associated stream is to be returned.
**Returns:** the stream to which this applet context maps the key
**Since:** 1.4

---

#### getStream

InputStream

getStream​(

String

key)

Returns the stream to which specified key is associated within this
applet context. Returns

null

if the applet context contains
no stream for this key.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

getStreamKeys

```java
Iterator
<
String
> getStreamKeys()
```

Deprecated.

Finds all the keys of the streams in this applet context.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

**Returns:** an Iterator of all the names of the streams in this applet
context.
**Since:** 1.4

---

#### getStreamKeys

Iterator

<

String

> getStreamKeys()

Finds all the keys of the streams in this applet context.

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

For security reasons, mapping of streams and keys exists for each
codebase. In other words, applet from one codebase cannot access
the streams created by an applet from a different codebase

---

