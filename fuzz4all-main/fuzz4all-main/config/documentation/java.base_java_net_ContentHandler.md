# Class ContentHandler

**Source:** `java.base\java\net\ContentHandler.html`

### Class Description

```java
public abstract class
ContentHandler

extends
Object
```

The abstract class

ContentHandler

is the superclass
of all classes that read an

Object

from a

URLConnection

.

An application does not generally call the

getContent

method in this class directly. Instead, an
application calls the

getContent

method in class

URL

or in

URLConnection

.
The application's content handler factory (an instance of a class that
implements the interface

ContentHandlerFactory

set up by a call to

setContentHandlerFactory

is called with a

String

giving the
MIME type of the object being received on the socket. The factory returns an
instance of a subclass of

ContentHandler

, and its

getContent

method is called to create the object.

If no content handler could be

found

,
URLConnection will look for a content handler in a user-definable set of places.
Users can define a vertical-bar delimited set of class prefixes
to search through by defining the

URLConnection.contentPathProp

property. The class name must be of the form:

{package-prefix}.{major}.{minor}

where

{major}.{minor}

is formed by taking the
content-type string, replacing all slash characters with a

period

('.'), and all other non-alphanumeric characters
with the underscore character '

_

'. The alphanumeric
characters are specifically the 26 uppercase ASCII letters
'

A

' through '

Z

', the 26 lowercase ASCII
letters '

a

' through '

z

', and the 10 ASCII
digits '

0

' through '

9

'.

e.g.
YoyoDyne.experimental.text.plain

If no user-defined content handler is found, then the system
tries to load a specific

content-type

handler from one
of the built-in handlers, if one exists.

If the loading of the content handler class would be performed by
a classloader that is outside of the delegation chain of the caller,
the JVM will need the RuntimePermission "getClassLoader".

**Since:** 1.0
**See Also:** getContent(java.net.URLConnection)

,

ContentHandlerFactory

,

URL.getContent()

,

URLConnection

,

URLConnection.getContent()

,

URLConnection.setContentHandlerFactory(java.net.ContentHandlerFactory)

---

### Field Details

*No entries found.*

### Constructor Details

#### public ContentHandler()

*No description found.*

---

### Method Details

#### public abstract
Object
getContent​(
URLConnection
urlc)
throws
IOException

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object from it.

**Parameters:**
- urlc

- a URL connection.

**Returns:**
- the object read by the

ContentHandler

.

**Throws:**
- IOException

- if an I/O error occurs while reading the object.

---

#### public
Object
getContent​(
URLConnection
urlc,

Class
[] classes)
throws
IOException

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object that matches one of the types specified.

The default implementation of this method should call

getContent(URLConnection)

and screen the return type for a match of the suggested types.

**Parameters:**
- urlc

- a URL connection.
- classes

- an array of types requested

**Returns:**
- the object read by the

ContentHandler

that is
the first match of the suggested types or

null

if none of the requested are supported.

**Throws:**
- IOException

- if an I/O error occurs while reading the object.

**Since:**
- 1.3

---

### Additional Sections

#### Class ContentHandler

java.lang.Object

- java.net.ContentHandler

java.net.ContentHandler

```java
public abstract class
ContentHandler

extends
Object
```

The abstract class

ContentHandler

is the superclass
of all classes that read an

Object

from a

URLConnection

.

An application does not generally call the

getContent

method in this class directly. Instead, an
application calls the

getContent

method in class

URL

or in

URLConnection

.
The application's content handler factory (an instance of a class that
implements the interface

ContentHandlerFactory

set up by a call to

setContentHandlerFactory

is called with a

String

giving the
MIME type of the object being received on the socket. The factory returns an
instance of a subclass of

ContentHandler

, and its

getContent

method is called to create the object.

If no content handler could be

found

,
URLConnection will look for a content handler in a user-definable set of places.
Users can define a vertical-bar delimited set of class prefixes
to search through by defining the

URLConnection.contentPathProp

property. The class name must be of the form:

{package-prefix}.{major}.{minor}

where

{major}.{minor}

is formed by taking the
content-type string, replacing all slash characters with a

period

('.'), and all other non-alphanumeric characters
with the underscore character '

_

'. The alphanumeric
characters are specifically the 26 uppercase ASCII letters
'

A

' through '

Z

', the 26 lowercase ASCII
letters '

a

' through '

z

', and the 10 ASCII
digits '

0

' through '

9

'.

e.g.
YoyoDyne.experimental.text.plain

If no user-defined content handler is found, then the system
tries to load a specific

content-type

handler from one
of the built-in handlers, if one exists.

If the loading of the content handler class would be performed by
a classloader that is outside of the delegation chain of the caller,
the JVM will need the RuntimePermission "getClassLoader".

**Since:** 1.0
**See Also:** getContent(java.net.URLConnection)

,

ContentHandlerFactory

,

URL.getContent()

,

URLConnection

,

URLConnection.getContent()

,

URLConnection.setContentHandlerFactory(java.net.ContentHandlerFactory)

public abstract class

ContentHandler

extends

Object

The abstract class

ContentHandler

is the superclass
of all classes that read an

Object

from a

URLConnection

.

An application does not generally call the

getContent

method in this class directly. Instead, an
application calls the

getContent

method in class

URL

or in

URLConnection

.
The application's content handler factory (an instance of a class that
implements the interface

ContentHandlerFactory

set up by a call to

setContentHandlerFactory

is called with a

String

giving the
MIME type of the object being received on the socket. The factory returns an
instance of a subclass of

ContentHandler

, and its

getContent

method is called to create the object.

If no content handler could be

found

,
URLConnection will look for a content handler in a user-definable set of places.
Users can define a vertical-bar delimited set of class prefixes
to search through by defining the

URLConnection.contentPathProp

property. The class name must be of the form:

{package-prefix}.{major}.{minor}

where

{major}.{minor}

is formed by taking the
content-type string, replacing all slash characters with a

period

('.'), and all other non-alphanumeric characters
with the underscore character '

_

'. The alphanumeric
characters are specifically the 26 uppercase ASCII letters
'

A

' through '

Z

', the 26 lowercase ASCII
letters '

a

' through '

z

', and the 10 ASCII
digits '

0

' through '

9

'.

e.g.
YoyoDyne.experimental.text.plain

If no user-defined content handler is found, then the system
tries to load a specific

content-type

handler from one
of the built-in handlers, if one exists.

If the loading of the content handler class would be performed by
a classloader that is outside of the delegation chain of the caller,
the JVM will need the RuntimePermission "getClassLoader".

An application does not generally call the

getContent

method in this class directly. Instead, an
application calls the

getContent

method in class

URL

or in

URLConnection

.
The application's content handler factory (an instance of a class that
implements the interface

ContentHandlerFactory

set up by a call to

setContentHandlerFactory

is called with a

String

giving the
MIME type of the object being received on the socket. The factory returns an
instance of a subclass of

ContentHandler

, and its

getContent

method is called to create the object.

If no content handler could be

found

,
URLConnection will look for a content handler in a user-definable set of places.
Users can define a vertical-bar delimited set of class prefixes
to search through by defining the

URLConnection.contentPathProp

property. The class name must be of the form:

{package-prefix}.{major}.{minor}

where

{major}.{minor}

is formed by taking the
content-type string, replacing all slash characters with a

period

('.'), and all other non-alphanumeric characters
with the underscore character '

_

'. The alphanumeric
characters are specifically the 26 uppercase ASCII letters
'

A

' through '

Z

', the 26 lowercase ASCII
letters '

a

' through '

z

', and the 10 ASCII
digits '

0

' through '

9

'.

e.g.
YoyoDyne.experimental.text.plain

If no user-defined content handler is found, then the system
tries to load a specific

content-type

handler from one
of the built-in handlers, if one exists.

If the loading of the content handler class would be performed by
a classloader that is outside of the delegation chain of the caller,
the JVM will need the RuntimePermission "getClassLoader".

If no content handler could be

found

,
URLConnection will look for a content handler in a user-definable set of places.
Users can define a vertical-bar delimited set of class prefixes
to search through by defining the

URLConnection.contentPathProp

property. The class name must be of the form:

{package-prefix}.{major}.{minor}

where

{major}.{minor}

is formed by taking the
content-type string, replacing all slash characters with a

period

('.'), and all other non-alphanumeric characters
with the underscore character '

_

'. The alphanumeric
characters are specifically the 26 uppercase ASCII letters
'

A

' through '

Z

', the 26 lowercase ASCII
letters '

a

' through '

z

', and the 10 ASCII
digits '

0

' through '

9

'.

e.g.
YoyoDyne.experimental.text.plain

If no user-defined content handler is found, then the system
tries to load a specific

content-type

handler from one
of the built-in handlers, if one exists.

If the loading of the content handler class would be performed by
a classloader that is outside of the delegation chain of the caller,
the JVM will need the RuntimePermission "getClassLoader".

where

{major}.{minor}

is formed by taking the
content-type string, replacing all slash characters with a

period

('.'), and all other non-alphanumeric characters
with the underscore character '

_

'. The alphanumeric
characters are specifically the 26 uppercase ASCII letters
'

A

' through '

Z

', the 26 lowercase ASCII
letters '

a

' through '

z

', and the 10 ASCII
digits '

0

' through '

9

'.

e.g.
YoyoDyne.experimental.text.plain

e.g.
YoyoDyne.experimental.text.plain

If the loading of the content handler class would be performed by
a classloader that is outside of the delegation chain of the caller,
the JVM will need the RuntimePermission "getClassLoader".

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ContentHandler

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

abstract

Object

getContent

​(

URLConnection

urlc)

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object from it.

Object

getContent

​(

URLConnection

urlc,

Class

[] classes)

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object that matches one of the types specified.

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

ContentHandler

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

abstract

Object

getContent

​(

URLConnection

urlc)

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object from it.

Object

getContent

​(

URLConnection

urlc,

Class

[] classes)

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object that matches one of the types specified.

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

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object from it.

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object that matches one of the types specified.

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

- ContentHandler

```java
public ContentHandler()
```

============ METHOD DETAIL ==========

- Method Detail

- getContent

```java
public abstract
Object
getContent​(
URLConnection
urlc)
throws
IOException
```

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object from it.

**Parameters:** urlc

- a URL connection.
**Returns:** the object read by the

ContentHandler

.
**Throws:** IOException

- if an I/O error occurs while reading the object.

- getContent

```java
public
Object
getContent​(
URLConnection
urlc,

Class
[] classes)
throws
IOException
```

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object that matches one of the types specified.

The default implementation of this method should call

getContent(URLConnection)

and screen the return type for a match of the suggested types.

**Parameters:** urlc

- a URL connection.
**Parameters:** classes

- an array of types requested
**Returns:** the object read by the

ContentHandler

that is
the first match of the suggested types or

null

if none of the requested are supported.
**Throws:** IOException

- if an I/O error occurs while reading the object.
**Since:** 1.3

Constructor Detail

- ContentHandler

```java
public ContentHandler()
```

---

#### Constructor Detail

ContentHandler

```java
public ContentHandler()
```

---

#### ContentHandler

public ContentHandler()

Method Detail

- getContent

```java
public abstract
Object
getContent​(
URLConnection
urlc)
throws
IOException
```

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object from it.

**Parameters:** urlc

- a URL connection.
**Returns:** the object read by the

ContentHandler

.
**Throws:** IOException

- if an I/O error occurs while reading the object.

- getContent

```java
public
Object
getContent​(
URLConnection
urlc,

Class
[] classes)
throws
IOException
```

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object that matches one of the types specified.

The default implementation of this method should call

getContent(URLConnection)

and screen the return type for a match of the suggested types.

**Parameters:** urlc

- a URL connection.
**Parameters:** classes

- an array of types requested
**Returns:** the object read by the

ContentHandler

that is
the first match of the suggested types or

null

if none of the requested are supported.
**Throws:** IOException

- if an I/O error occurs while reading the object.
**Since:** 1.3

---

#### Method Detail

getContent

```java
public abstract
Object
getContent​(
URLConnection
urlc)
throws
IOException
```

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object from it.

**Parameters:** urlc

- a URL connection.
**Returns:** the object read by the

ContentHandler

.
**Throws:** IOException

- if an I/O error occurs while reading the object.

---

#### getContent

public abstract

Object

getContent​(

URLConnection

urlc)
throws

IOException

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object from it.

getContent

```java
public
Object
getContent​(
URLConnection
urlc,

Class
[] classes)
throws
IOException
```

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object that matches one of the types specified.

The default implementation of this method should call

getContent(URLConnection)

and screen the return type for a match of the suggested types.

**Parameters:** urlc

- a URL connection.
**Parameters:** classes

- an array of types requested
**Returns:** the object read by the

ContentHandler

that is
the first match of the suggested types or

null

if none of the requested are supported.
**Throws:** IOException

- if an I/O error occurs while reading the object.
**Since:** 1.3

---

#### getContent

public

Object

getContent​(

URLConnection

urlc,

Class

[] classes)
throws

IOException

Given a URL connect stream positioned at the beginning of the
representation of an object, this method reads that stream and
creates an object that matches one of the types specified.

The default implementation of this method should call

getContent(URLConnection)

and screen the return type for a match of the suggested types.

---

