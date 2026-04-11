# Interface AppletStub

**Source:** `java.desktop\java\applet\AppletStub.html`

### Class Description

```java
@Deprecated
(
since
="9")
public interface
AppletStub
```

When an applet is first created, an applet stub is attached to it
using the applet's

setStub

method. This stub
serves as the interface between the applet and the browser
environment or applet viewer environment in which the application
is running.

**Since:** 1.0
**See Also:** Applet.setStub(java.applet.AppletStub)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isActive()

Determines if the applet is active. An applet is active just
before its

start

method is called. It becomes
inactive just before its

stop

method is called.

**Returns:**
- true

if the applet is active;

false

otherwise.

---

#### URL
getDocumentBase()

Gets the URL of the document in which the applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

**Returns:**
- the

URL

of the document that contains the
applet.

**See Also:**
- getCodeBase()

---

#### URL
getCodeBase()

Gets the base URL. This is the URL of the directory which contains the applet.

**Returns:**
- the base

URL

of
the directory which contains the applet.

**See Also:**
- getDocumentBase()

---

#### String
getParameter​(
String
name)

Returns the value of the named parameter in the HTML tag. For
example, if an applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

**Parameters:**
- name

- a parameter name.

**Returns:**
- the value of the named parameter,
or

null

if not set.

---

#### AppletContext
getAppletContext()

Returns the applet's context.

**Returns:**
- the applet's context.

---

#### void appletResize​(int width,
int height)

Called when the applet wants to be resized.

**Parameters:**
- width

- the new requested width for the applet.
- height

- the new requested height for the applet.

---

### Additional Sections

#### Interface AppletStub

```java
@Deprecated
(
since
="9")
public interface
AppletStub
```

Deprecated.

The Applet API is deprecated, no replacement.

When an applet is first created, an applet stub is attached to it
using the applet's

setStub

method. This stub
serves as the interface between the applet and the browser
environment or applet viewer environment in which the application
is running.

**Since:** 1.0
**See Also:** Applet.setStub(java.applet.AppletStub)

@Deprecated

(

since

="9")
public interface

AppletStub

When an applet is first created, an applet stub is attached to it
using the applet's

setStub

method. This stub
serves as the interface between the applet and the browser
environment or applet viewer environment in which the application
is running.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

appletResize

​(int width,
int height)

Deprecated.

Called when the applet wants to be resized.

AppletContext

getAppletContext

()

Deprecated.

Returns the applet's context.

URL

getCodeBase

()

Deprecated.

Gets the base URL.

URL

getDocumentBase

()

Deprecated.

Gets the URL of the document in which the applet is embedded.

String

getParameter

​(

String

name)

Deprecated.

Returns the value of the named parameter in the HTML tag.

boolean

isActive

()

Deprecated.

Determines if the applet is active.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

appletResize

​(int width,
int height)

Deprecated.

Called when the applet wants to be resized.

AppletContext

getAppletContext

()

Deprecated.

Returns the applet's context.

URL

getCodeBase

()

Deprecated.

Gets the base URL.

URL

getDocumentBase

()

Deprecated.

Gets the URL of the document in which the applet is embedded.

String

getParameter

​(

String

name)

Deprecated.

Returns the value of the named parameter in the HTML tag.

boolean

isActive

()

Deprecated.

Determines if the applet is active.

---

#### Method Summary

Deprecated.

Called when the applet wants to be resized.

Returns the applet's context.

Gets the base URL.

Gets the URL of the document in which the applet is embedded.

Returns the value of the named parameter in the HTML tag.

Determines if the applet is active.

============ METHOD DETAIL ==========

- Method Detail

- isActive

```java
boolean isActive()
```

Deprecated.

Determines if the applet is active. An applet is active just
before its

start

method is called. It becomes
inactive just before its

stop

method is called.

**Returns:** true

if the applet is active;

false

otherwise.

- getDocumentBase

```java
URL
getDocumentBase()
```

Deprecated.

Gets the URL of the document in which the applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

**Returns:** the

URL

of the document that contains the
applet.
**See Also:** getCodeBase()

- getCodeBase

```java
URL
getCodeBase()
```

Deprecated.

Gets the base URL. This is the URL of the directory which contains the applet.

**Returns:** the base

URL

of
the directory which contains the applet.
**See Also:** getDocumentBase()

- getParameter

```java
String
getParameter​(
String
name)
```

Deprecated.

Returns the value of the named parameter in the HTML tag. For
example, if an applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

**Parameters:** name

- a parameter name.
**Returns:** the value of the named parameter,
or

null

if not set.

- getAppletContext

```java
AppletContext
getAppletContext()
```

Deprecated.

Returns the applet's context.

**Returns:** the applet's context.

- appletResize

```java
void appletResize​(int width,
int height)
```

Deprecated.

Called when the applet wants to be resized.

**Parameters:** width

- the new requested width for the applet.
**Parameters:** height

- the new requested height for the applet.

Method Detail

- isActive

```java
boolean isActive()
```

Deprecated.

Determines if the applet is active. An applet is active just
before its

start

method is called. It becomes
inactive just before its

stop

method is called.

**Returns:** true

if the applet is active;

false

otherwise.

- getDocumentBase

```java
URL
getDocumentBase()
```

Deprecated.

Gets the URL of the document in which the applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

**Returns:** the

URL

of the document that contains the
applet.
**See Also:** getCodeBase()

- getCodeBase

```java
URL
getCodeBase()
```

Deprecated.

Gets the base URL. This is the URL of the directory which contains the applet.

**Returns:** the base

URL

of
the directory which contains the applet.
**See Also:** getDocumentBase()

- getParameter

```java
String
getParameter​(
String
name)
```

Deprecated.

Returns the value of the named parameter in the HTML tag. For
example, if an applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

**Parameters:** name

- a parameter name.
**Returns:** the value of the named parameter,
or

null

if not set.

- getAppletContext

```java
AppletContext
getAppletContext()
```

Deprecated.

Returns the applet's context.

**Returns:** the applet's context.

- appletResize

```java
void appletResize​(int width,
int height)
```

Deprecated.

Called when the applet wants to be resized.

**Parameters:** width

- the new requested width for the applet.
**Parameters:** height

- the new requested height for the applet.

---

#### Method Detail

isActive

```java
boolean isActive()
```

Deprecated.

Determines if the applet is active. An applet is active just
before its

start

method is called. It becomes
inactive just before its

stop

method is called.

**Returns:** true

if the applet is active;

false

otherwise.

---

#### isActive

boolean isActive()

Determines if the applet is active. An applet is active just
before its

start

method is called. It becomes
inactive just before its

stop

method is called.

getDocumentBase

```java
URL
getDocumentBase()
```

Deprecated.

Gets the URL of the document in which the applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

**Returns:** the

URL

of the document that contains the
applet.
**See Also:** getCodeBase()

---

#### getDocumentBase

URL

getDocumentBase()

Gets the URL of the document in which the applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

http://www.oracle.com/technetwork/java/index.html

getCodeBase

```java
URL
getCodeBase()
```

Deprecated.

Gets the base URL. This is the URL of the directory which contains the applet.

**Returns:** the base

URL

of
the directory which contains the applet.
**See Also:** getDocumentBase()

---

#### getCodeBase

URL

getCodeBase()

Gets the base URL. This is the URL of the directory which contains the applet.

getParameter

```java
String
getParameter​(
String
name)
```

Deprecated.

Returns the value of the named parameter in the HTML tag. For
example, if an applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

**Parameters:** name

- a parameter name.
**Returns:** the value of the named parameter,
or

null

if not set.

---

#### getParameter

String

getParameter​(

String

name)

Returns the value of the named parameter in the HTML tag. For
example, if an applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>

then a call to

getParameter("Color")

returns the
value

"blue"

.

getAppletContext

```java
AppletContext
getAppletContext()
```

Deprecated.

Returns the applet's context.

**Returns:** the applet's context.

---

#### getAppletContext

AppletContext

getAppletContext()

Returns the applet's context.

appletResize

```java
void appletResize​(int width,
int height)
```

Deprecated.

Called when the applet wants to be resized.

**Parameters:** width

- the new requested width for the applet.
**Parameters:** height

- the new requested height for the applet.

---

#### appletResize

void appletResize​(int width,
int height)

Called when the applet wants to be resized.

---

