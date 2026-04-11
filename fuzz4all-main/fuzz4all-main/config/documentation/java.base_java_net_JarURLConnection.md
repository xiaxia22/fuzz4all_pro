# Class JarURLConnection

**Source:** `java.base\java\net\JarURLConnection.html`

### Class Description

```java
public abstract class
JarURLConnection

extends
URLConnection
```

A URL Connection to a Java ARchive (JAR) file or an entry in a JAR
file.

The syntax of a JAR URL is:

```java
jar:<url>!/{entry}
```

for example:

jar:http://www.foo.com/bar/baz.jar!/COM/foo/Quux.class

Jar URLs should be used to refer to a JAR file or entries in
a JAR file. The example above is a JAR URL which refers to a JAR
entry. If the entry name is omitted, the URL refers to the whole
JAR file:

jar:http://www.foo.com/bar/baz.jar!/

Users should cast the generic URLConnection to a
JarURLConnection when they know that the URL they created is a JAR
URL, and they need JAR-specific functionality. For example:

```java
URL url = new URL("jar:file:/home/duke/duke.jar!/");
JarURLConnection jarConnection = (JarURLConnection)url.openConnection();
Manifest manifest = jarConnection.getManifest();
```

JarURLConnection instances can only be used to read from JAR files.
It is not possible to get a

OutputStream

to modify or write
to the underlying JAR file using this class.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

---

### Field Details

#### protected
URLConnection
jarFileURLConnection

The connection to the JAR file URL, if the connection has been
initiated. This should be set by connect.

---

### Constructor Details

#### protected JarURLConnection​(
URL
url)
throws
MalformedURLException

Creates the new JarURLConnection to the specified URL.

**Parameters:**
- url

- the URL

**Throws:**
- MalformedURLException

- if no legal protocol
could be found in a specification string or the
string could not be parsed.

---

### Method Details

#### public
URL
getJarFileURL()

Returns the URL for the Jar file for this connection.

**Returns:**
- the URL for the Jar file for this connection.

---

#### public
String
getEntryName()

Return the entry name for this connection. This method
returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

**Returns:**
- the entry name for this connection, if any.

---

#### public abstract
JarFile
getJarFile()
throws
IOException

Return the JAR file for this connection.

**Returns:**
- the JAR file for this connection. If the connection is
a connection to an entry of a JAR file, the JAR file object is
returned

**Throws:**
- IOException

- if an IOException occurs while trying to
connect to the JAR file for this connection.

**See Also:**
- URLConnection.connect()

---

#### public
Manifest
getManifest()
throws
IOException

Returns the Manifest for this connection, or null if none.

**Returns:**
- the manifest object corresponding to the JAR file object
for this connection.

**Throws:**
- IOException

- if getting the JAR file for this
connection causes an IOException to be thrown.

**See Also:**
- getJarFile()

---

#### public
JarEntry
getJarEntry()
throws
IOException

Return the JAR entry object for this connection, if any. This
method returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

**Returns:**
- the JAR entry object for this connection, or null if
the JAR URL for this connection points to a JAR file.

**Throws:**
- IOException

- if getting the JAR file for this
connection causes an IOException to be thrown.

**See Also:**
- getJarFile()

,

getJarEntry()

---

#### public
Attributes
getAttributes()
throws
IOException

Return the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.

**Returns:**
- the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.

**Throws:**
- IOException

- if getting the JAR entry causes an
IOException to be thrown.

**See Also:**
- getJarEntry()

---

#### public
Attributes
getMainAttributes()
throws
IOException

Returns the main Attributes for the JAR file for this
connection.

**Returns:**
- the main Attributes for the JAR file for this
connection.

**Throws:**
- IOException

- if getting the manifest causes an
IOException to be thrown.

**See Also:**
- getJarFile()

,

getManifest()

---

#### public
Certificate
[] getCertificates()
throws
IOException

Return the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise. This method
can only be called once
the connection has been completely verified by reading
from the input stream until the end of the stream has been
reached. Otherwise, this method will return

null

**Returns:**
- the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise.

**Throws:**
- IOException

- if getting the JAR entry causes an
IOException to be thrown.

**See Also:**
- getJarEntry()

---

### Additional Sections

#### Class JarURLConnection

java.lang.Object

- java.net.URLConnection
- - java.net.JarURLConnection

java.net.URLConnection

- java.net.JarURLConnection

java.net.JarURLConnection

```java
public abstract class
JarURLConnection

extends
URLConnection
```

A URL Connection to a Java ARchive (JAR) file or an entry in a JAR
file.

The syntax of a JAR URL is:

```java
jar:<url>!/{entry}
```

for example:

jar:http://www.foo.com/bar/baz.jar!/COM/foo/Quux.class

Jar URLs should be used to refer to a JAR file or entries in
a JAR file. The example above is a JAR URL which refers to a JAR
entry. If the entry name is omitted, the URL refers to the whole
JAR file:

jar:http://www.foo.com/bar/baz.jar!/

Users should cast the generic URLConnection to a
JarURLConnection when they know that the URL they created is a JAR
URL, and they need JAR-specific functionality. For example:

```java
URL url = new URL("jar:file:/home/duke/duke.jar!/");
JarURLConnection jarConnection = (JarURLConnection)url.openConnection();
Manifest manifest = jarConnection.getManifest();
```

JarURLConnection instances can only be used to read from JAR files.
It is not possible to get a

OutputStream

to modify or write
to the underlying JAR file using this class.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

**Since:** 1.2
**See Also:** URL

,

URLConnection

,

JarFile

,

JarInputStream

,

Manifest

,

ZipEntry

public abstract class

JarURLConnection

extends

URLConnection

A URL Connection to a Java ARchive (JAR) file or an entry in a JAR
file.

The syntax of a JAR URL is:

```java
jar:<url>!/{entry}
```

for example:

jar:http://www.foo.com/bar/baz.jar!/COM/foo/Quux.class

Jar URLs should be used to refer to a JAR file or entries in
a JAR file. The example above is a JAR URL which refers to a JAR
entry. If the entry name is omitted, the URL refers to the whole
JAR file:

jar:http://www.foo.com/bar/baz.jar!/

Users should cast the generic URLConnection to a
JarURLConnection when they know that the URL they created is a JAR
URL, and they need JAR-specific functionality. For example:

```java
URL url = new URL("jar:file:/home/duke/duke.jar!/");
JarURLConnection jarConnection = (JarURLConnection)url.openConnection();
Manifest manifest = jarConnection.getManifest();
```

JarURLConnection instances can only be used to read from JAR files.
It is not possible to get a

OutputStream

to modify or write
to the underlying JAR file using this class.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

The syntax of a JAR URL is:

```java
jar:<url>!/{entry}
```

for example:

jar:http://www.foo.com/bar/baz.jar!/COM/foo/Quux.class

Jar URLs should be used to refer to a JAR file or entries in
a JAR file. The example above is a JAR URL which refers to a JAR
entry. If the entry name is omitted, the URL refers to the whole
JAR file:

jar:http://www.foo.com/bar/baz.jar!/

Users should cast the generic URLConnection to a
JarURLConnection when they know that the URL they created is a JAR
URL, and they need JAR-specific functionality. For example:

```java
URL url = new URL("jar:file:/home/duke/duke.jar!/");
JarURLConnection jarConnection = (JarURLConnection)url.openConnection();
Manifest manifest = jarConnection.getManifest();
```

JarURLConnection instances can only be used to read from JAR files.
It is not possible to get a

OutputStream

to modify or write
to the underlying JAR file using this class.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

jar:<url>!/{entry}

for example:

jar:http://www.foo.com/bar/baz.jar!/COM/foo/Quux.class

Jar URLs should be used to refer to a JAR file or entries in
a JAR file. The example above is a JAR URL which refers to a JAR
entry. If the entry name is omitted, the URL refers to the whole
JAR file:

jar:http://www.foo.com/bar/baz.jar!/

Users should cast the generic URLConnection to a
JarURLConnection when they know that the URL they created is a JAR
URL, and they need JAR-specific functionality. For example:

```java
URL url = new URL("jar:file:/home/duke/duke.jar!/");
JarURLConnection jarConnection = (JarURLConnection)url.openConnection();
Manifest manifest = jarConnection.getManifest();
```

JarURLConnection instances can only be used to read from JAR files.
It is not possible to get a

OutputStream

to modify or write
to the underlying JAR file using this class.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

jar:http://www.foo.com/bar/baz.jar!/COM/foo/Quux.class

Jar URLs should be used to refer to a JAR file or entries in
a JAR file. The example above is a JAR URL which refers to a JAR
entry. If the entry name is omitted, the URL refers to the whole
JAR file:

jar:http://www.foo.com/bar/baz.jar!/

Users should cast the generic URLConnection to a
JarURLConnection when they know that the URL they created is a JAR
URL, and they need JAR-specific functionality. For example:

```java
URL url = new URL("jar:file:/home/duke/duke.jar!/");
JarURLConnection jarConnection = (JarURLConnection)url.openConnection();
Manifest manifest = jarConnection.getManifest();
```

JarURLConnection instances can only be used to read from JAR files.
It is not possible to get a

OutputStream

to modify or write
to the underlying JAR file using this class.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

Jar URLs should be used to refer to a JAR file or entries in
a JAR file. The example above is a JAR URL which refers to a JAR
entry. If the entry name is omitted, the URL refers to the whole
JAR file:

jar:http://www.foo.com/bar/baz.jar!/

Users should cast the generic URLConnection to a
JarURLConnection when they know that the URL they created is a JAR
URL, and they need JAR-specific functionality. For example:

```java
URL url = new URL("jar:file:/home/duke/duke.jar!/");
JarURLConnection jarConnection = (JarURLConnection)url.openConnection();
Manifest manifest = jarConnection.getManifest();
```

JarURLConnection instances can only be used to read from JAR files.
It is not possible to get a

OutputStream

to modify or write
to the underlying JAR file using this class.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

Users should cast the generic URLConnection to a
JarURLConnection when they know that the URL they created is a JAR
URL, and they need JAR-specific functionality. For example:

```java
URL url = new URL("jar:file:/home/duke/duke.jar!/");
JarURLConnection jarConnection = (JarURLConnection)url.openConnection();
Manifest manifest = jarConnection.getManifest();
```

JarURLConnection instances can only be used to read from JAR files.
It is not possible to get a

OutputStream

to modify or write
to the underlying JAR file using this class.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

URL url = new URL("jar:file:/home/duke/duke.jar!/");
JarURLConnection jarConnection = (JarURLConnection)url.openConnection();
Manifest manifest = jarConnection.getManifest();

JarURLConnection instances can only be used to read from JAR files.
It is not possible to get a

OutputStream

to modify or write
to the underlying JAR file using this class.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

!/

is referred to as the

separator

.

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

When constructing a JAR url via

new URL(context, spec)

,
the following rules apply:

- if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

if there is no context URL and the specification passed to the
URL constructor doesn't contain a separator, the URL is considered
to refer to a JarFile.

if there is a context URL, the context URL is assumed to refer
to a JAR file or a Jar directory.

if the specification begins with a '/', the Jar directory is
ignored, and the spec is considered to be at the root of the Jar
file.

Examples:

Examples:

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

URLConnection

jarFileURLConnection

The connection to the JAR file URL, if the connection has been
initiated.

- Fields declared in class java.net.

URLConnection

allowUserInteraction

,

connected

,

doInput

,

doOutput

,

ifModifiedSince

,

url

,

useCaches

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JarURLConnection

​(

URL

url)

Creates the new JarURLConnection to the specified URL.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Attributes

getAttributes

()

Return the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.

Certificate

[]

getCertificates

()

Return the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise.

String

getEntryName

()

Return the entry name for this connection.

JarEntry

getJarEntry

()

Return the JAR entry object for this connection, if any.

abstract

JarFile

getJarFile

()

Return the JAR file for this connection.

URL

getJarFileURL

()

Returns the URL for the Jar file for this connection.

Attributes

getMainAttributes

()

Returns the main Attributes for the JAR file for this
connection.

Manifest

getManifest

()

Returns the Manifest for this connection, or null if none.

- Methods declared in class java.net.

URLConnection

addRequestProperty

,

connect

,

getAllowUserInteraction

,

getConnectTimeout

,

getContent

,

getContent

,

getContentEncoding

,

getContentLength

,

getContentLengthLong

,

getContentType

,

getDate

,

getDefaultAllowUserInteraction

,

getDefaultRequestProperty

,

getDefaultUseCaches

,

getDefaultUseCaches

,

getDoInput

,

getDoOutput

,

getExpiration

,

getFileNameMap

,

getHeaderField

,

getHeaderField

,

getHeaderFieldDate

,

getHeaderFieldInt

,

getHeaderFieldKey

,

getHeaderFieldLong

,

getHeaderFields

,

getIfModifiedSince

,

getInputStream

,

getLastModified

,

getOutputStream

,

getPermission

,

getReadTimeout

,

getRequestProperties

,

getRequestProperty

,

getURL

,

getUseCaches

,

guessContentTypeFromName

,

guessContentTypeFromStream

,

setAllowUserInteraction

,

setConnectTimeout

,

setContentHandlerFactory

,

setDefaultAllowUserInteraction

,

setDefaultRequestProperty

,

setDefaultUseCaches

,

setDefaultUseCaches

,

setDoInput

,

setDoOutput

,

setFileNameMap

,

setIfModifiedSince

,

setReadTimeout

,

setRequestProperty

,

setUseCaches

,

toString

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

protected

URLConnection

jarFileURLConnection

The connection to the JAR file URL, if the connection has been
initiated.

- Fields declared in class java.net.

URLConnection

allowUserInteraction

,

connected

,

doInput

,

doOutput

,

ifModifiedSince

,

url

,

useCaches

---

#### Field Summary

The connection to the JAR file URL, if the connection has been
initiated.

Fields declared in class java.net.

URLConnection

allowUserInteraction

,

connected

,

doInput

,

doOutput

,

ifModifiedSince

,

url

,

useCaches

---

#### Fields declared in class java.net. URLConnection

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JarURLConnection

​(

URL

url)

Creates the new JarURLConnection to the specified URL.

---

#### Constructor Summary

Creates the new JarURLConnection to the specified URL.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Attributes

getAttributes

()

Return the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.

Certificate

[]

getCertificates

()

Return the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise.

String

getEntryName

()

Return the entry name for this connection.

JarEntry

getJarEntry

()

Return the JAR entry object for this connection, if any.

abstract

JarFile

getJarFile

()

Return the JAR file for this connection.

URL

getJarFileURL

()

Returns the URL for the Jar file for this connection.

Attributes

getMainAttributes

()

Returns the main Attributes for the JAR file for this
connection.

Manifest

getManifest

()

Returns the Manifest for this connection, or null if none.

- Methods declared in class java.net.

URLConnection

addRequestProperty

,

connect

,

getAllowUserInteraction

,

getConnectTimeout

,

getContent

,

getContent

,

getContentEncoding

,

getContentLength

,

getContentLengthLong

,

getContentType

,

getDate

,

getDefaultAllowUserInteraction

,

getDefaultRequestProperty

,

getDefaultUseCaches

,

getDefaultUseCaches

,

getDoInput

,

getDoOutput

,

getExpiration

,

getFileNameMap

,

getHeaderField

,

getHeaderField

,

getHeaderFieldDate

,

getHeaderFieldInt

,

getHeaderFieldKey

,

getHeaderFieldLong

,

getHeaderFields

,

getIfModifiedSince

,

getInputStream

,

getLastModified

,

getOutputStream

,

getPermission

,

getReadTimeout

,

getRequestProperties

,

getRequestProperty

,

getURL

,

getUseCaches

,

guessContentTypeFromName

,

guessContentTypeFromStream

,

setAllowUserInteraction

,

setConnectTimeout

,

setContentHandlerFactory

,

setDefaultAllowUserInteraction

,

setDefaultRequestProperty

,

setDefaultUseCaches

,

setDefaultUseCaches

,

setDoInput

,

setDoOutput

,

setFileNameMap

,

setIfModifiedSince

,

setReadTimeout

,

setRequestProperty

,

setUseCaches

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Return the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.

Return the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise.

Return the entry name for this connection.

Return the JAR entry object for this connection, if any.

Return the JAR file for this connection.

Returns the URL for the Jar file for this connection.

Returns the main Attributes for the JAR file for this
connection.

Returns the Manifest for this connection, or null if none.

Methods declared in class java.net.

URLConnection

addRequestProperty

,

connect

,

getAllowUserInteraction

,

getConnectTimeout

,

getContent

,

getContent

,

getContentEncoding

,

getContentLength

,

getContentLengthLong

,

getContentType

,

getDate

,

getDefaultAllowUserInteraction

,

getDefaultRequestProperty

,

getDefaultUseCaches

,

getDefaultUseCaches

,

getDoInput

,

getDoOutput

,

getExpiration

,

getFileNameMap

,

getHeaderField

,

getHeaderField

,

getHeaderFieldDate

,

getHeaderFieldInt

,

getHeaderFieldKey

,

getHeaderFieldLong

,

getHeaderFields

,

getIfModifiedSince

,

getInputStream

,

getLastModified

,

getOutputStream

,

getPermission

,

getReadTimeout

,

getRequestProperties

,

getRequestProperty

,

getURL

,

getUseCaches

,

guessContentTypeFromName

,

guessContentTypeFromStream

,

setAllowUserInteraction

,

setConnectTimeout

,

setContentHandlerFactory

,

setDefaultAllowUserInteraction

,

setDefaultRequestProperty

,

setDefaultUseCaches

,

setDefaultUseCaches

,

setDoInput

,

setDoOutput

,

setFileNameMap

,

setIfModifiedSince

,

setReadTimeout

,

setRequestProperty

,

setUseCaches

,

toString

---

#### Methods declared in class java.net. URLConnection

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- jarFileURLConnection

```java
protected
URLConnection
jarFileURLConnection
```

The connection to the JAR file URL, if the connection has been
initiated. This should be set by connect.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JarURLConnection

```java
protected JarURLConnection​(
URL
url)
throws
MalformedURLException
```

Creates the new JarURLConnection to the specified URL.

**Parameters:** url

- the URL
**Throws:** MalformedURLException

- if no legal protocol
could be found in a specification string or the
string could not be parsed.

============ METHOD DETAIL ==========

- Method Detail

- getJarFileURL

```java
public
URL
getJarFileURL()
```

Returns the URL for the Jar file for this connection.

**Returns:** the URL for the Jar file for this connection.

- getEntryName

```java
public
String
getEntryName()
```

Return the entry name for this connection. This method
returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

**Returns:** the entry name for this connection, if any.

- getJarFile

```java
public abstract
JarFile
getJarFile()
throws
IOException
```

Return the JAR file for this connection.

**Returns:** the JAR file for this connection. If the connection is
a connection to an entry of a JAR file, the JAR file object is
returned
**Throws:** IOException

- if an IOException occurs while trying to
connect to the JAR file for this connection.
**See Also:** URLConnection.connect()

- getManifest

```java
public
Manifest
getManifest()
throws
IOException
```

Returns the Manifest for this connection, or null if none.

**Returns:** the manifest object corresponding to the JAR file object
for this connection.
**Throws:** IOException

- if getting the JAR file for this
connection causes an IOException to be thrown.
**See Also:** getJarFile()

- getJarEntry

```java
public
JarEntry
getJarEntry()
throws
IOException
```

Return the JAR entry object for this connection, if any. This
method returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

**Returns:** the JAR entry object for this connection, or null if
the JAR URL for this connection points to a JAR file.
**Throws:** IOException

- if getting the JAR file for this
connection causes an IOException to be thrown.
**See Also:** getJarFile()

,

getJarEntry()

- getAttributes

```java
public
Attributes
getAttributes()
throws
IOException
```

Return the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.

**Returns:** the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.
**Throws:** IOException

- if getting the JAR entry causes an
IOException to be thrown.
**See Also:** getJarEntry()

- getMainAttributes

```java
public
Attributes
getMainAttributes()
throws
IOException
```

Returns the main Attributes for the JAR file for this
connection.

**Returns:** the main Attributes for the JAR file for this
connection.
**Throws:** IOException

- if getting the manifest causes an
IOException to be thrown.
**See Also:** getJarFile()

,

getManifest()

- getCertificates

```java
public
Certificate
[] getCertificates()
throws
IOException
```

Return the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise. This method
can only be called once
the connection has been completely verified by reading
from the input stream until the end of the stream has been
reached. Otherwise, this method will return

null

**Returns:** the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise.
**Throws:** IOException

- if getting the JAR entry causes an
IOException to be thrown.
**See Also:** getJarEntry()

Field Detail

- jarFileURLConnection

```java
protected
URLConnection
jarFileURLConnection
```

The connection to the JAR file URL, if the connection has been
initiated. This should be set by connect.

---

#### Field Detail

jarFileURLConnection

```java
protected
URLConnection
jarFileURLConnection
```

The connection to the JAR file URL, if the connection has been
initiated. This should be set by connect.

---

#### jarFileURLConnection

protected

URLConnection

jarFileURLConnection

The connection to the JAR file URL, if the connection has been
initiated. This should be set by connect.

Constructor Detail

- JarURLConnection

```java
protected JarURLConnection​(
URL
url)
throws
MalformedURLException
```

Creates the new JarURLConnection to the specified URL.

**Parameters:** url

- the URL
**Throws:** MalformedURLException

- if no legal protocol
could be found in a specification string or the
string could not be parsed.

---

#### Constructor Detail

JarURLConnection

```java
protected JarURLConnection​(
URL
url)
throws
MalformedURLException
```

Creates the new JarURLConnection to the specified URL.

**Parameters:** url

- the URL
**Throws:** MalformedURLException

- if no legal protocol
could be found in a specification string or the
string could not be parsed.

---

#### JarURLConnection

protected JarURLConnection​(

URL

url)
throws

MalformedURLException

Creates the new JarURLConnection to the specified URL.

Method Detail

- getJarFileURL

```java
public
URL
getJarFileURL()
```

Returns the URL for the Jar file for this connection.

**Returns:** the URL for the Jar file for this connection.

- getEntryName

```java
public
String
getEntryName()
```

Return the entry name for this connection. This method
returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

**Returns:** the entry name for this connection, if any.

- getJarFile

```java
public abstract
JarFile
getJarFile()
throws
IOException
```

Return the JAR file for this connection.

**Returns:** the JAR file for this connection. If the connection is
a connection to an entry of a JAR file, the JAR file object is
returned
**Throws:** IOException

- if an IOException occurs while trying to
connect to the JAR file for this connection.
**See Also:** URLConnection.connect()

- getManifest

```java
public
Manifest
getManifest()
throws
IOException
```

Returns the Manifest for this connection, or null if none.

**Returns:** the manifest object corresponding to the JAR file object
for this connection.
**Throws:** IOException

- if getting the JAR file for this
connection causes an IOException to be thrown.
**See Also:** getJarFile()

- getJarEntry

```java
public
JarEntry
getJarEntry()
throws
IOException
```

Return the JAR entry object for this connection, if any. This
method returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

**Returns:** the JAR entry object for this connection, or null if
the JAR URL for this connection points to a JAR file.
**Throws:** IOException

- if getting the JAR file for this
connection causes an IOException to be thrown.
**See Also:** getJarFile()

,

getJarEntry()

- getAttributes

```java
public
Attributes
getAttributes()
throws
IOException
```

Return the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.

**Returns:** the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.
**Throws:** IOException

- if getting the JAR entry causes an
IOException to be thrown.
**See Also:** getJarEntry()

- getMainAttributes

```java
public
Attributes
getMainAttributes()
throws
IOException
```

Returns the main Attributes for the JAR file for this
connection.

**Returns:** the main Attributes for the JAR file for this
connection.
**Throws:** IOException

- if getting the manifest causes an
IOException to be thrown.
**See Also:** getJarFile()

,

getManifest()

- getCertificates

```java
public
Certificate
[] getCertificates()
throws
IOException
```

Return the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise. This method
can only be called once
the connection has been completely verified by reading
from the input stream until the end of the stream has been
reached. Otherwise, this method will return

null

**Returns:** the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise.
**Throws:** IOException

- if getting the JAR entry causes an
IOException to be thrown.
**See Also:** getJarEntry()

---

#### Method Detail

getJarFileURL

```java
public
URL
getJarFileURL()
```

Returns the URL for the Jar file for this connection.

**Returns:** the URL for the Jar file for this connection.

---

#### getJarFileURL

public

URL

getJarFileURL()

Returns the URL for the Jar file for this connection.

getEntryName

```java
public
String
getEntryName()
```

Return the entry name for this connection. This method
returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

**Returns:** the entry name for this connection, if any.

---

#### getEntryName

public

String

getEntryName()

Return the entry name for this connection. This method
returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

getJarFile

```java
public abstract
JarFile
getJarFile()
throws
IOException
```

Return the JAR file for this connection.

**Returns:** the JAR file for this connection. If the connection is
a connection to an entry of a JAR file, the JAR file object is
returned
**Throws:** IOException

- if an IOException occurs while trying to
connect to the JAR file for this connection.
**See Also:** URLConnection.connect()

---

#### getJarFile

public abstract

JarFile

getJarFile()
throws

IOException

Return the JAR file for this connection.

getManifest

```java
public
Manifest
getManifest()
throws
IOException
```

Returns the Manifest for this connection, or null if none.

**Returns:** the manifest object corresponding to the JAR file object
for this connection.
**Throws:** IOException

- if getting the JAR file for this
connection causes an IOException to be thrown.
**See Also:** getJarFile()

---

#### getManifest

public

Manifest

getManifest()
throws

IOException

Returns the Manifest for this connection, or null if none.

getJarEntry

```java
public
JarEntry
getJarEntry()
throws
IOException
```

Return the JAR entry object for this connection, if any. This
method returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

**Returns:** the JAR entry object for this connection, or null if
the JAR URL for this connection points to a JAR file.
**Throws:** IOException

- if getting the JAR file for this
connection causes an IOException to be thrown.
**See Also:** getJarFile()

,

getJarEntry()

---

#### getJarEntry

public

JarEntry

getJarEntry()
throws

IOException

Return the JAR entry object for this connection, if any. This
method returns null if the JAR file URL corresponding to this
connection points to a JAR file and not a JAR file entry.

getAttributes

```java
public
Attributes
getAttributes()
throws
IOException
```

Return the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.

**Returns:** the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.
**Throws:** IOException

- if getting the JAR entry causes an
IOException to be thrown.
**See Also:** getJarEntry()

---

#### getAttributes

public

Attributes

getAttributes()
throws

IOException

Return the Attributes object for this connection if the URL
for it points to a JAR file entry, null otherwise.

getMainAttributes

```java
public
Attributes
getMainAttributes()
throws
IOException
```

Returns the main Attributes for the JAR file for this
connection.

**Returns:** the main Attributes for the JAR file for this
connection.
**Throws:** IOException

- if getting the manifest causes an
IOException to be thrown.
**See Also:** getJarFile()

,

getManifest()

---

#### getMainAttributes

public

Attributes

getMainAttributes()
throws

IOException

Returns the main Attributes for the JAR file for this
connection.

getCertificates

```java
public
Certificate
[] getCertificates()
throws
IOException
```

Return the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise. This method
can only be called once
the connection has been completely verified by reading
from the input stream until the end of the stream has been
reached. Otherwise, this method will return

null

**Returns:** the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise.
**Throws:** IOException

- if getting the JAR entry causes an
IOException to be thrown.
**See Also:** getJarEntry()

---

#### getCertificates

public

Certificate

[] getCertificates()
throws

IOException

Return the Certificate object for this connection if the URL
for it points to a JAR file entry, null otherwise. This method
can only be called once
the connection has been completely verified by reading
from the input stream until the end of the stream has been
reached. Otherwise, this method will return

null

---

