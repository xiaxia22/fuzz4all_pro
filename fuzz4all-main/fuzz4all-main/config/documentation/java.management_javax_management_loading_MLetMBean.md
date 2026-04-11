# Interface MLetMBean

**Source:** `java.management\javax\management\loading\MLetMBean.html`

### Class Description

```java
public interface
MLetMBean
```

Exposes the remote management interface of the MLet
MBean.

**All Known Implementing Classes:** MLet

,

PrivateMLet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Set
<
Object
> getMBeansFromURL​(
String
url)
throws
ServiceNotFoundException

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

**Parameters:**
- url

- The URL of the text file to be loaded as String object.

**Returns:**
- A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.

**Throws:**
- ServiceNotFoundException

- One of the following errors
has occurred: The m-let text file does not contain an MLET tag,
the m-let text file is not found, a mandatory attribute of the
MLET tag is not specified, the value of url is malformed.

---

#### Set
<
Object
> getMBeansFromURL​(
URL
url)
throws
ServiceNotFoundException

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

**Parameters:**
- url

- The URL of the text file to be loaded as URL object.

**Returns:**
- A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.

**Throws:**
- ServiceNotFoundException

- One of the following errors
has occurred: The m-let text file does not contain an MLET tag,
the m-let text file is not found, a mandatory attribute of the
MLET tag is not specified, the value of url is null.

---

#### void addURL​(
URL
url)

Appends the specified URL to the list of URLs to search for classes and
resources.

**Parameters:**
- url

- the URL to add.

---

#### void addURL​(
String
url)
throws
ServiceNotFoundException

Appends the specified URL to the list of URLs to search for classes and
resources.

**Parameters:**
- url

- the URL to add.

**Throws:**
- ServiceNotFoundException

- The specified URL is malformed.

---

#### URL
[] getURLs()

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

**Returns:**
- the list of URLs.

---

#### URL
getResource​(
String
name)

Finds the resource with the given name.
A resource is some data (images, audio, text, etc) that can be accessed by class code in a way that is
independent of the location of the code.
The name of a resource is a "/"-separated path name that identifies the resource.

**Parameters:**
- name

- The resource name

**Returns:**
- An URL for reading the resource, or null if the resource could not be found or the caller doesn't have adequate privileges to get the
resource.

---

#### InputStream
getResourceAsStream​(
String
name)

Returns an input stream for reading the specified resource. The search order is described in the documentation for
getResource(String).

**Parameters:**
- name

- The resource name

**Returns:**
- An input stream for reading the resource, or null if the resource could not be found

---

#### Enumeration
<
URL
> getResources​(
String
name)
throws
IOException

Finds all the resources with the given name. A resource is some
data (images, audio, text, etc) that can be accessed by class
code in a way that is independent of the location of the code.
The name of a resource is a "/"-separated path name that
identifies the resource.

**Parameters:**
- name

- The resource name.

**Returns:**
- An enumeration of URL to the resource. If no resources
could be found, the enumeration will be empty. Resources that
cannot be accessed will not be in the enumeration.

**Throws:**
- IOException

- if an I/O exception occurs when
searching for resources.

---

#### String
getLibraryDirectory()

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

**Returns:**
- The current directory used by the library loader.

**Throws:**
- UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.

**See Also:**
- setLibraryDirectory(java.lang.String)

---

#### void setLibraryDirectory​(
String
libdir)

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

**Parameters:**
- libdir

- The directory used by the library loader.

**Throws:**
- UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.

**See Also:**
- getLibraryDirectory()

---

### Additional Sections

#### Interface MLetMBean

**All Known Implementing Classes:** MLet

,

PrivateMLet

```java
public interface
MLetMBean
```

Exposes the remote management interface of the MLet
MBean.

**Since:** 1.5

public interface

MLetMBean

Exposes the remote management interface of the MLet
MBean.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addURL

​(

String

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

void

addURL

​(

URL

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

String

getLibraryDirectory

()

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

Set

<

Object

>

getMBeansFromURL

​(

String

url)

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server.

Set

<

Object

>

getMBeansFromURL

​(

URL

url)

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server.

URL

getResource

​(

String

name)

Finds the resource with the given name.

InputStream

getResourceAsStream

​(

String

name)

Returns an input stream for reading the specified resource.

Enumeration

<

URL

>

getResources

​(

String

name)

Finds all the resources with the given name.

URL

[]

getURLs

()

Returns the search path of URLs for loading classes and resources.

void

setLibraryDirectory

​(

String

libdir)

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addURL

​(

String

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

void

addURL

​(

URL

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

String

getLibraryDirectory

()

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

Set

<

Object

>

getMBeansFromURL

​(

String

url)

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server.

Set

<

Object

>

getMBeansFromURL

​(

URL

url)

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server.

URL

getResource

​(

String

name)

Finds the resource with the given name.

InputStream

getResourceAsStream

​(

String

name)

Returns an input stream for reading the specified resource.

Enumeration

<

URL

>

getResources

​(

String

name)

Finds all the resources with the given name.

URL

[]

getURLs

()

Returns the search path of URLs for loading classes and resources.

void

setLibraryDirectory

​(

String

libdir)

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

---

#### Method Summary

Appends the specified URL to the list of URLs to search for classes and
resources.

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server.

Finds the resource with the given name.

Returns an input stream for reading the specified resource.

Finds all the resources with the given name.

Returns the search path of URLs for loading classes and resources.

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

============ METHOD DETAIL ==========

- Method Detail

- getMBeansFromURL

```java
Set
<
Object
> getMBeansFromURL​(
String
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

**Parameters:** url

- The URL of the text file to be loaded as String object.
**Returns:** A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.
**Throws:** ServiceNotFoundException

- One of the following errors
has occurred: The m-let text file does not contain an MLET tag,
the m-let text file is not found, a mandatory attribute of the
MLET tag is not specified, the value of url is malformed.

- getMBeansFromURL

```java
Set
<
Object
> getMBeansFromURL​(
URL
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

**Parameters:** url

- The URL of the text file to be loaded as URL object.
**Returns:** A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.
**Throws:** ServiceNotFoundException

- One of the following errors
has occurred: The m-let text file does not contain an MLET tag,
the m-let text file is not found, a mandatory attribute of the
MLET tag is not specified, the value of url is null.

- addURL

```java
void addURL​(
URL
url)
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Parameters:** url

- the URL to add.

- addURL

```java
void addURL​(
String
url)
throws
ServiceNotFoundException
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Parameters:** url

- the URL to add.
**Throws:** ServiceNotFoundException

- The specified URL is malformed.

- getURLs

```java
URL
[] getURLs()
```

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

**Returns:** the list of URLs.

- getResource

```java
URL
getResource​(
String
name)
```

Finds the resource with the given name.
A resource is some data (images, audio, text, etc) that can be accessed by class code in a way that is
independent of the location of the code.
The name of a resource is a "/"-separated path name that identifies the resource.

**Parameters:** name

- The resource name
**Returns:** An URL for reading the resource, or null if the resource could not be found or the caller doesn't have adequate privileges to get the
resource.

- getResourceAsStream

```java
InputStream
getResourceAsStream​(
String
name)
```

Returns an input stream for reading the specified resource. The search order is described in the documentation for
getResource(String).

**Parameters:** name

- The resource name
**Returns:** An input stream for reading the resource, or null if the resource could not be found

- getResources

```java
Enumeration
<
URL
> getResources​(
String
name)
throws
IOException
```

Finds all the resources with the given name. A resource is some
data (images, audio, text, etc) that can be accessed by class
code in a way that is independent of the location of the code.
The name of a resource is a "/"-separated path name that
identifies the resource.

**Parameters:** name

- The resource name.
**Returns:** An enumeration of URL to the resource. If no resources
could be found, the enumeration will be empty. Resources that
cannot be accessed will not be in the enumeration.
**Throws:** IOException

- if an I/O exception occurs when
searching for resources.

- getLibraryDirectory

```java
String
getLibraryDirectory()
```

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

**Returns:** The current directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** setLibraryDirectory(java.lang.String)

- setLibraryDirectory

```java
void setLibraryDirectory​(
String
libdir)
```

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

**Parameters:** libdir

- The directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** getLibraryDirectory()

Method Detail

- getMBeansFromURL

```java
Set
<
Object
> getMBeansFromURL​(
String
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

**Parameters:** url

- The URL of the text file to be loaded as String object.
**Returns:** A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.
**Throws:** ServiceNotFoundException

- One of the following errors
has occurred: The m-let text file does not contain an MLET tag,
the m-let text file is not found, a mandatory attribute of the
MLET tag is not specified, the value of url is malformed.

- getMBeansFromURL

```java
Set
<
Object
> getMBeansFromURL​(
URL
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

**Parameters:** url

- The URL of the text file to be loaded as URL object.
**Returns:** A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.
**Throws:** ServiceNotFoundException

- One of the following errors
has occurred: The m-let text file does not contain an MLET tag,
the m-let text file is not found, a mandatory attribute of the
MLET tag is not specified, the value of url is null.

- addURL

```java
void addURL​(
URL
url)
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Parameters:** url

- the URL to add.

- addURL

```java
void addURL​(
String
url)
throws
ServiceNotFoundException
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Parameters:** url

- the URL to add.
**Throws:** ServiceNotFoundException

- The specified URL is malformed.

- getURLs

```java
URL
[] getURLs()
```

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

**Returns:** the list of URLs.

- getResource

```java
URL
getResource​(
String
name)
```

Finds the resource with the given name.
A resource is some data (images, audio, text, etc) that can be accessed by class code in a way that is
independent of the location of the code.
The name of a resource is a "/"-separated path name that identifies the resource.

**Parameters:** name

- The resource name
**Returns:** An URL for reading the resource, or null if the resource could not be found or the caller doesn't have adequate privileges to get the
resource.

- getResourceAsStream

```java
InputStream
getResourceAsStream​(
String
name)
```

Returns an input stream for reading the specified resource. The search order is described in the documentation for
getResource(String).

**Parameters:** name

- The resource name
**Returns:** An input stream for reading the resource, or null if the resource could not be found

- getResources

```java
Enumeration
<
URL
> getResources​(
String
name)
throws
IOException
```

Finds all the resources with the given name. A resource is some
data (images, audio, text, etc) that can be accessed by class
code in a way that is independent of the location of the code.
The name of a resource is a "/"-separated path name that
identifies the resource.

**Parameters:** name

- The resource name.
**Returns:** An enumeration of URL to the resource. If no resources
could be found, the enumeration will be empty. Resources that
cannot be accessed will not be in the enumeration.
**Throws:** IOException

- if an I/O exception occurs when
searching for resources.

- getLibraryDirectory

```java
String
getLibraryDirectory()
```

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

**Returns:** The current directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** setLibraryDirectory(java.lang.String)

- setLibraryDirectory

```java
void setLibraryDirectory​(
String
libdir)
```

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

**Parameters:** libdir

- The directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** getLibraryDirectory()

---

#### Method Detail

getMBeansFromURL

```java
Set
<
Object
> getMBeansFromURL​(
String
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

**Parameters:** url

- The URL of the text file to be loaded as String object.
**Returns:** A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.
**Throws:** ServiceNotFoundException

- One of the following errors
has occurred: The m-let text file does not contain an MLET tag,
the m-let text file is not found, a mandatory attribute of the
MLET tag is not specified, the value of url is malformed.

---

#### getMBeansFromURL

Set

<

Object

> getMBeansFromURL​(

String

url)
throws

ServiceNotFoundException

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

getMBeansFromURL

```java
Set
<
Object
> getMBeansFromURL​(
URL
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

**Parameters:** url

- The URL of the text file to be loaded as URL object.
**Returns:** A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.
**Throws:** ServiceNotFoundException

- One of the following errors
has occurred: The m-let text file does not contain an MLET tag,
the m-let text file is not found, a mandatory attribute of the
MLET tag is not specified, the value of url is null.

---

#### getMBeansFromURL

Set

<

Object

> getMBeansFromURL​(

URL

url)
throws

ServiceNotFoundException

Loads a text file containing MLET tags that define the MBeans
to be added to the MBean server. The location of the text file is
specified by a URL. The text file is read using the UTF-8
encoding. The MBeans specified in the MLET file will be
instantiated and registered in the MBean server.

addURL

```java
void addURL​(
URL
url)
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Parameters:** url

- the URL to add.

---

#### addURL

void addURL​(

URL

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

addURL

```java
void addURL​(
String
url)
throws
ServiceNotFoundException
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Parameters:** url

- the URL to add.
**Throws:** ServiceNotFoundException

- The specified URL is malformed.

---

#### addURL

void addURL​(

String

url)
throws

ServiceNotFoundException

Appends the specified URL to the list of URLs to search for classes and
resources.

getURLs

```java
URL
[] getURLs()
```

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

**Returns:** the list of URLs.

---

#### getURLs

URL

[] getURLs()

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

getResource

```java
URL
getResource​(
String
name)
```

Finds the resource with the given name.
A resource is some data (images, audio, text, etc) that can be accessed by class code in a way that is
independent of the location of the code.
The name of a resource is a "/"-separated path name that identifies the resource.

**Parameters:** name

- The resource name
**Returns:** An URL for reading the resource, or null if the resource could not be found or the caller doesn't have adequate privileges to get the
resource.

---

#### getResource

URL

getResource​(

String

name)

Finds the resource with the given name.
A resource is some data (images, audio, text, etc) that can be accessed by class code in a way that is
independent of the location of the code.
The name of a resource is a "/"-separated path name that identifies the resource.

getResourceAsStream

```java
InputStream
getResourceAsStream​(
String
name)
```

Returns an input stream for reading the specified resource. The search order is described in the documentation for
getResource(String).

**Parameters:** name

- The resource name
**Returns:** An input stream for reading the resource, or null if the resource could not be found

---

#### getResourceAsStream

InputStream

getResourceAsStream​(

String

name)

Returns an input stream for reading the specified resource. The search order is described in the documentation for
getResource(String).

getResources

```java
Enumeration
<
URL
> getResources​(
String
name)
throws
IOException
```

Finds all the resources with the given name. A resource is some
data (images, audio, text, etc) that can be accessed by class
code in a way that is independent of the location of the code.
The name of a resource is a "/"-separated path name that
identifies the resource.

**Parameters:** name

- The resource name.
**Returns:** An enumeration of URL to the resource. If no resources
could be found, the enumeration will be empty. Resources that
cannot be accessed will not be in the enumeration.
**Throws:** IOException

- if an I/O exception occurs when
searching for resources.

---

#### getResources

Enumeration

<

URL

> getResources​(

String

name)
throws

IOException

Finds all the resources with the given name. A resource is some
data (images, audio, text, etc) that can be accessed by class
code in a way that is independent of the location of the code.
The name of a resource is a "/"-separated path name that
identifies the resource.

getLibraryDirectory

```java
String
getLibraryDirectory()
```

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

**Returns:** The current directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** setLibraryDirectory(java.lang.String)

---

#### getLibraryDirectory

String

getLibraryDirectory()

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

setLibraryDirectory

```java
void setLibraryDirectory​(
String
libdir)
```

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

**Parameters:** libdir

- The directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** getLibraryDirectory()

---

#### setLibraryDirectory

void setLibraryDirectory​(

String

libdir)

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

---

