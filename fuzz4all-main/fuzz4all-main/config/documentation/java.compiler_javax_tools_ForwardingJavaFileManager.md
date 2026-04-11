# Class ForwardingJavaFileManager<M extends JavaFileManager >

**Source:** `java.compiler\javax\tools\ForwardingJavaFileManager.html`

### Class Description

```java
public class
ForwardingJavaFileManager<M extends
JavaFileManager
>

extends
Object

implements
JavaFileManager
```

Forwards calls to a given file manager. Subclasses of this class
might override some of these methods and might also provide
additional fields and methods.

**Type Parameters:** M

- the kind of file manager forwarded to by this object

---

### Field Details

#### protected final
M
extends
JavaFileManager
fileManager

The file manager which all methods are delegated to.

---

### Constructor Details

#### protected ForwardingJavaFileManager​(
M
fileManager)

Creates a new instance of ForwardingJavaFileManager.

**Parameters:**
- fileManager

- delegate to this file manager

---

### Method Details

#### public
ClassLoader
getClassLoader​(
JavaFileManager.Location
location)

Description copied from interface:

JavaFileManager

**Specified by:**
- getClassLoader

in interface

JavaFileManager

**Parameters:**
- location

- a location

**Returns:**
- a class loader for the given location; or

null

if loading plug-ins from the given location is disabled or if
the location is not known

**Throws:**
- SecurityException

- if a class loader can not be created
in the current security context
- IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

---

#### public
Iterable
<
JavaFileObject
> list​(
JavaFileManager.Location
location,

String
packageName,

Set
<
JavaFileObject.Kind
> kinds,
boolean recurse)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- list

in interface

JavaFileManager

**Parameters:**
- location

- a location
- packageName

- a package name
- kinds

- return objects only of these kinds
- recurse

- if true include "subpackages"

**Returns:**
- an Iterable of file objects matching the given criteria

**Throws:**
- IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened
- IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

---

#### public
String
inferBinaryName​(
JavaFileManager.Location
location,

JavaFileObject
file)

Description copied from interface:

JavaFileManager

**Specified by:**
- inferBinaryName

in interface

JavaFileManager

**Parameters:**
- location

- a location
- file

- a file object

**Returns:**
- a binary name or

null

the file object is not
found in the given location

**Throws:**
- IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

---

#### public boolean isSameFile​(
FileObject
a,

FileObject
b)

Description copied from interface:

JavaFileManager

**Specified by:**
- isSameFile

in interface

JavaFileManager

**Parameters:**
- a

- a file object
- b

- a file object

**Returns:**
- true if the given file objects represent the same
underlying object

**Throws:**
- IllegalArgumentException

- if either of the arguments
were created with another file manager and this file manager
does not support foreign file objects

---

#### public boolean handleOption​(
String
current,

Iterator
<
String
> remaining)

Description copied from interface:

JavaFileManager

**Specified by:**
- handleOption

in interface

JavaFileManager

**Parameters:**
- current

- current option
- remaining

- remaining options

**Returns:**
- true if this option was handled by this file manager,
false otherwise

**Throws:**
- IllegalArgumentException

- if this option to this file
manager is used incorrectly
- IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

---

#### public
JavaFileObject
getJavaFileForInput​(
JavaFileManager.Location
location,

String
className,

JavaFileObject.Kind
kind)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- getJavaFileForInput

in interface

JavaFileManager

**Parameters:**
- location

- a location
- className

- the name of a class
- kind

- the kind of file, must be one of

SOURCE

or

CLASS

**Returns:**
- a file object, might return

null

if the
file does not exist

**Throws:**
- IllegalArgumentException

- if the location is not known
to this file manager and the file manager does not support
unknown locations, or if the kind is not valid, or if the
location is a module-oriented location
- IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
- IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

---

#### public
JavaFileObject
getJavaFileForOutput​(
JavaFileManager.Location
location,

String
className,

JavaFileObject.Kind
kind,

FileObject
sibling)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- getJavaFileForOutput

in interface

JavaFileManager

**Parameters:**
- location

- a package-oriented location
- className

- the name of a class
- kind

- the kind of file, must be one of

SOURCE

or

CLASS
- sibling

- a file object to be used as hint for placement;
might be

null

**Returns:**
- a file object for output

**Throws:**
- IllegalArgumentException

- if sibling is not known to
this file manager, or if the location is not known to this file
manager and the file manager does not support unknown
locations, or if the kind is not valid, or if the location is
not an output location
- IllegalStateException

-

JavaFileManager.close()

has been called
and this file manager cannot be reopened
- IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

---

#### public
FileObject
getFileForInput​(
JavaFileManager.Location
location,

String
packageName,

String
relativeName)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- getFileForInput

in interface

JavaFileManager

**Parameters:**
- location

- a package-oriented location
- packageName

- a package name
- relativeName

- a relative name

**Returns:**
- a file object, might return

null

if the file
does not exist

**Throws:**
- IllegalArgumentException

- if the location is not known
to this file manager and the file manager does not support
unknown locations, or if

relativeName

is not valid,
or if the location is a module-oriented location
- IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
- IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

---

#### public
FileObject
getFileForOutput​(
JavaFileManager.Location
location,

String
packageName,

String
relativeName,

FileObject
sibling)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- getFileForOutput

in interface

JavaFileManager

**Parameters:**
- location

- an output location
- packageName

- a package name
- relativeName

- a relative name
- sibling

- a file object to be used as hint for placement;
might be

null

**Returns:**
- a file object

**Throws:**
- IllegalArgumentException

- if sibling is not known to
this file manager, or if the location is not known to this file
manager and the file manager does not support unknown
locations, or if

relativeName

is not valid,
or if the location is not an output location
- IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
- IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

---

#### public
JavaFileManager.Location
getLocationForModule​(
JavaFileManager.Location
location,

String
moduleName)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- getLocationForModule

in interface

JavaFileManager

**Parameters:**
- location

- the module-oriented location
- moduleName

- the name of the module to be found

**Returns:**
- the location for the named module

**Throws:**
- IOException

- if an I/O error occurred

**Since:**
- 9

---

#### public
JavaFileManager.Location
getLocationForModule​(
JavaFileManager.Location
location,

JavaFileObject
fo)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- getLocationForModule

in interface

JavaFileManager

**Parameters:**
- location

- the module-oriented location
- fo

- the file

**Returns:**
- the module containing the file

**Throws:**
- IOException

- if an I/O error occurred

**Since:**
- 9

---

#### public <S>
ServiceLoader
<S> getServiceLoader​(
JavaFileManager.Location
location,

Class
<S> service)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- getServiceLoader

in interface

JavaFileManager

**Parameters:**
- location

- the module-oriented location
- service

- the

Class

object of the service class

**Returns:**
- a service loader for the given service class

**Throws:**
- IOException

- if an I/O error occurred

**Since:**
- 9

**Type Parameters:**
- S

- the service class

---

#### public
String
inferModuleName​(
JavaFileManager.Location
location)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- inferModuleName

in interface

JavaFileManager

**Parameters:**
- location

- a package-oriented location representing a module

**Returns:**
- the name of the module

**Throws:**
- IOException

- if an I/O error occurred

**Since:**
- 9

---

#### public
Iterable
<
Set
<
JavaFileManager.Location
>> listLocationsForModules​(
JavaFileManager.Location
location)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- listLocationsForModules

in interface

JavaFileManager

**Parameters:**
- location

- the module-oriented location for which to list the modules

**Returns:**
- a series of sets of locations containing modules

**Throws:**
- IOException

- if an I/O error occurred

**Since:**
- 9

---

#### public boolean contains​(
JavaFileManager.Location
location,

FileObject
fo)
throws
IOException

Description copied from interface:

JavaFileManager

**Specified by:**
- contains

in interface

JavaFileManager

**Parameters:**
- location

- the location
- fo

- the file object

**Returns:**
- whether or not the file is contained in the location

**Throws:**
- IOException

- if there is a problem determining the result

**Since:**
- 9

---

### Additional Sections

#### Class ForwardingJavaFileManager<M extends JavaFileManager >

java.lang.Object

- javax.tools.ForwardingJavaFileManager<M>

javax.tools.ForwardingJavaFileManager<M>

**Type Parameters:** M

- the kind of file manager forwarded to by this object

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

,

JavaFileManager

,

OptionChecker

```java
public class
ForwardingJavaFileManager<M extends
JavaFileManager
>

extends
Object

implements
JavaFileManager
```

Forwards calls to a given file manager. Subclasses of this class
might override some of these methods and might also provide
additional fields and methods.

**Since:** 1.6

public class

ForwardingJavaFileManager<M extends

JavaFileManager

>

extends

Object

implements

JavaFileManager

Forwards calls to a given file manager. Subclasses of this class
might override some of these methods and might also provide
additional fields and methods.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface javax.tools.

JavaFileManager

JavaFileManager.Location

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

M

fileManager

The file manager which all methods are delegated to.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ForwardingJavaFileManager

​(

M

fileManager)

Creates a new instance of ForwardingJavaFileManager.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(

JavaFileManager.Location

location,

FileObject

fo)

Determines whether or not a given file object is "contained in" a specified location.

ClassLoader

getClassLoader

​(

JavaFileManager.Location

location)

Returns a class loader for loading plug-ins from the given
package-oriented location.

FileObject

getFileForInput

​(

JavaFileManager.Location

location,

String

packageName,

String

relativeName)

Returns a

file object

for input
representing the specified

relative
name

in the specified package in the given package-oriented location.

FileObject

getFileForOutput

​(

JavaFileManager.Location

location,

String

packageName,

String

relativeName,

FileObject

sibling)

Returns a

file object

for output
representing the specified

relative
name

in the specified package in the given location.

JavaFileObject

getJavaFileForInput

​(

JavaFileManager.Location

location,

String

className,

JavaFileObject.Kind

kind)

Returns a

file object

for input
representing the specified class of the specified kind in the
given package-oriented location.

JavaFileObject

getJavaFileForOutput

​(

JavaFileManager.Location

location,

String

className,

JavaFileObject.Kind

kind,

FileObject

sibling)

Returns a

file object

for output
representing the specified class of the specified kind in the
given package-oriented location.

JavaFileManager.Location

getLocationForModule

​(

JavaFileManager.Location

location,

String

moduleName)

Gets a location for a named module within a location, which may be either
a module-oriented location or an output location.

JavaFileManager.Location

getLocationForModule

​(

JavaFileManager.Location

location,

JavaFileObject

fo)

Gets a location for the module containing a specific file
to be found within a location, which may be either
a module-oriented location or an output location.

<S>

ServiceLoader

<S>

getServiceLoader

​(

JavaFileManager.Location

location,

Class

<S> service)

Get a service loader for a specific service class from a given location.

boolean

handleOption

​(

String

current,

Iterator

<

String

> remaining)

Handles one option.

String

inferBinaryName

​(

JavaFileManager.Location

location,

JavaFileObject

file)

Infers a binary name of a file object based on a package-oriented location.

String

inferModuleName

​(

JavaFileManager.Location

location)

Infer the name of the module from its location, as returned by

getLocationForModule

or

listModuleLocations

.

boolean

isSameFile

​(

FileObject

a,

FileObject

b)

Compares two file objects and return true if they represent the
same underlying object.

Iterable

<

JavaFileObject

>

list

​(

JavaFileManager.Location

location,

String

packageName,

Set

<

JavaFileObject.Kind

> kinds,
boolean recurse)

Lists all file objects matching the given criteria in the given
package-oriented location.

Iterable

<

Set

<

JavaFileManager.Location

>>

listLocationsForModules

​(

JavaFileManager.Location

location)

Lists the locations for all the modules in a module-oriented location or an output location.

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

- Methods declared in interface javax.tools.

JavaFileManager

close

,

flush

,

hasLocation

- Methods declared in interface javax.tools.

OptionChecker

isSupportedOption

Nested Class Summary

- Nested classes/interfaces declared in interface javax.tools.

JavaFileManager

JavaFileManager.Location

---

#### Nested Class Summary

Nested classes/interfaces declared in interface javax.tools.

JavaFileManager

JavaFileManager.Location

---

#### Nested classes/interfaces declared in interface javax.tools. JavaFileManager

Field Summary

Fields

Modifier and Type

Field

Description

protected

M

fileManager

The file manager which all methods are delegated to.

---

#### Field Summary

The file manager which all methods are delegated to.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ForwardingJavaFileManager

​(

M

fileManager)

Creates a new instance of ForwardingJavaFileManager.

---

#### Constructor Summary

Creates a new instance of ForwardingJavaFileManager.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(

JavaFileManager.Location

location,

FileObject

fo)

Determines whether or not a given file object is "contained in" a specified location.

ClassLoader

getClassLoader

​(

JavaFileManager.Location

location)

Returns a class loader for loading plug-ins from the given
package-oriented location.

FileObject

getFileForInput

​(

JavaFileManager.Location

location,

String

packageName,

String

relativeName)

Returns a

file object

for input
representing the specified

relative
name

in the specified package in the given package-oriented location.

FileObject

getFileForOutput

​(

JavaFileManager.Location

location,

String

packageName,

String

relativeName,

FileObject

sibling)

Returns a

file object

for output
representing the specified

relative
name

in the specified package in the given location.

JavaFileObject

getJavaFileForInput

​(

JavaFileManager.Location

location,

String

className,

JavaFileObject.Kind

kind)

Returns a

file object

for input
representing the specified class of the specified kind in the
given package-oriented location.

JavaFileObject

getJavaFileForOutput

​(

JavaFileManager.Location

location,

String

className,

JavaFileObject.Kind

kind,

FileObject

sibling)

Returns a

file object

for output
representing the specified class of the specified kind in the
given package-oriented location.

JavaFileManager.Location

getLocationForModule

​(

JavaFileManager.Location

location,

String

moduleName)

Gets a location for a named module within a location, which may be either
a module-oriented location or an output location.

JavaFileManager.Location

getLocationForModule

​(

JavaFileManager.Location

location,

JavaFileObject

fo)

Gets a location for the module containing a specific file
to be found within a location, which may be either
a module-oriented location or an output location.

<S>

ServiceLoader

<S>

getServiceLoader

​(

JavaFileManager.Location

location,

Class

<S> service)

Get a service loader for a specific service class from a given location.

boolean

handleOption

​(

String

current,

Iterator

<

String

> remaining)

Handles one option.

String

inferBinaryName

​(

JavaFileManager.Location

location,

JavaFileObject

file)

Infers a binary name of a file object based on a package-oriented location.

String

inferModuleName

​(

JavaFileManager.Location

location)

Infer the name of the module from its location, as returned by

getLocationForModule

or

listModuleLocations

.

boolean

isSameFile

​(

FileObject

a,

FileObject

b)

Compares two file objects and return true if they represent the
same underlying object.

Iterable

<

JavaFileObject

>

list

​(

JavaFileManager.Location

location,

String

packageName,

Set

<

JavaFileObject.Kind

> kinds,
boolean recurse)

Lists all file objects matching the given criteria in the given
package-oriented location.

Iterable

<

Set

<

JavaFileManager.Location

>>

listLocationsForModules

​(

JavaFileManager.Location

location)

Lists the locations for all the modules in a module-oriented location or an output location.

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

- Methods declared in interface javax.tools.

JavaFileManager

close

,

flush

,

hasLocation

- Methods declared in interface javax.tools.

OptionChecker

isSupportedOption

---

#### Method Summary

Determines whether or not a given file object is "contained in" a specified location.

Returns a class loader for loading plug-ins from the given
package-oriented location.

Returns a

file object

for input
representing the specified

relative
name

in the specified package in the given package-oriented location.

Returns a

file object

for output
representing the specified

relative
name

in the specified package in the given location.

Returns a

file object

for input
representing the specified class of the specified kind in the
given package-oriented location.

Returns a

file object

for output
representing the specified class of the specified kind in the
given package-oriented location.

Gets a location for a named module within a location, which may be either
a module-oriented location or an output location.

Gets a location for the module containing a specific file
to be found within a location, which may be either
a module-oriented location or an output location.

Get a service loader for a specific service class from a given location.

Handles one option.

Infers a binary name of a file object based on a package-oriented location.

Infer the name of the module from its location, as returned by

getLocationForModule

or

listModuleLocations

.

Compares two file objects and return true if they represent the
same underlying object.

Lists all file objects matching the given criteria in the given
package-oriented location.

Lists the locations for all the modules in a module-oriented location or an output location.

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

Methods declared in interface javax.tools.

JavaFileManager

close

,

flush

,

hasLocation

---

#### Methods declared in interface javax.tools. JavaFileManager

Methods declared in interface javax.tools.

OptionChecker

isSupportedOption

---

#### Methods declared in interface javax.tools. OptionChecker

============ FIELD DETAIL ===========

- Field Detail

- fileManager

```java
protected final
M
extends
JavaFileManager
fileManager
```

The file manager which all methods are delegated to.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ForwardingJavaFileManager

```java
protected ForwardingJavaFileManager​(
M
fileManager)
```

Creates a new instance of ForwardingJavaFileManager.

**Parameters:** fileManager

- delegate to this file manager

============ METHOD DETAIL ==========

- Method Detail

- getClassLoader

```java
public
ClassLoader
getClassLoader​(
JavaFileManager.Location
location)
```

Description copied from interface:

JavaFileManager

Returns a class loader for loading plug-ins from the given
package-oriented location.
For example, to load annotation processors,
a compiler will request a class loader for the

ANNOTATION_PROCESSOR_PATH

location.

**Specified by:** getClassLoader

in interface

JavaFileManager
**Parameters:** location

- a location
**Returns:** a class loader for the given location; or

null

if loading plug-ins from the given location is disabled or if
the location is not known
**Throws:** SecurityException

- if a class loader can not be created
in the current security context
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

- list

```java
public
Iterable
<
JavaFileObject
> list​(
JavaFileManager.Location
location,

String
packageName,

Set
<
JavaFileObject.Kind
> kinds,
boolean recurse)
throws
IOException
```

Description copied from interface:

JavaFileManager

Lists all file objects matching the given criteria in the given
package-oriented location.
List file objects in "subpackages" if recurse is true.

Note: even if the given location is unknown to this file
manager, it may not return

null

. Also, an unknown
location may not cause an exception.

**Specified by:** list

in interface

JavaFileManager
**Parameters:** location

- a location
**Parameters:** packageName

- a package name
**Parameters:** kinds

- return objects only of these kinds
**Parameters:** recurse

- if true include "subpackages"
**Returns:** an Iterable of file objects matching the given criteria
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

- inferBinaryName

```java
public
String
inferBinaryName​(
JavaFileManager.Location
location,

JavaFileObject
file)
```

Description copied from interface:

JavaFileManager

Infers a binary name of a file object based on a package-oriented location.
The binary name returned might not be a valid binary name according to

The Java™ Language Specification

.

**Specified by:** inferBinaryName

in interface

JavaFileManager
**Parameters:** location

- a location
**Parameters:** file

- a file object
**Returns:** a binary name or

null

the file object is not
found in the given location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

- isSameFile

```java
public boolean isSameFile​(
FileObject
a,

FileObject
b)
```

Description copied from interface:

JavaFileManager

Compares two file objects and return true if they represent the
same underlying object.

**Specified by:** isSameFile

in interface

JavaFileManager
**Parameters:** a

- a file object
**Parameters:** b

- a file object
**Returns:** true if the given file objects represent the same
underlying object
**Throws:** IllegalArgumentException

- if either of the arguments
were created with another file manager and this file manager
does not support foreign file objects

- handleOption

```java
public boolean handleOption​(
String
current,

Iterator
<
String
> remaining)
```

Description copied from interface:

JavaFileManager

Handles one option. If

current

is an option to this
file manager it will consume any arguments to that option from

remaining

and return true, otherwise return false.

**Specified by:** handleOption

in interface

JavaFileManager
**Parameters:** current

- current option
**Parameters:** remaining

- remaining options
**Returns:** true if this option was handled by this file manager,
false otherwise
**Throws:** IllegalArgumentException

- if this option to this file
manager is used incorrectly
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

- getJavaFileForInput

```java
public
JavaFileObject
getJavaFileForInput​(
JavaFileManager.Location
location,

String
className,

JavaFileObject.Kind
kind)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for input
representing the specified class of the specified kind in the
given package-oriented location.

**Specified by:** getJavaFileForInput

in interface

JavaFileManager
**Parameters:** location

- a location
**Parameters:** className

- the name of a class
**Parameters:** kind

- the kind of file, must be one of

SOURCE

or

CLASS
**Returns:** a file object, might return

null

if the
file does not exist
**Throws:** IllegalArgumentException

- if the location is not known
to this file manager and the file manager does not support
unknown locations, or if the kind is not valid, or if the
location is a module-oriented location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

- getJavaFileForOutput

```java
public
JavaFileObject
getJavaFileForOutput​(
JavaFileManager.Location
location,

String
className,

JavaFileObject.Kind
kind,

FileObject
sibling)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for output
representing the specified class of the specified kind in the
given package-oriented location.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

**Specified by:** getJavaFileForOutput

in interface

JavaFileManager
**Parameters:** location

- a package-oriented location
**Parameters:** className

- the name of a class
**Parameters:** kind

- the kind of file, must be one of

SOURCE

or

CLASS
**Parameters:** sibling

- a file object to be used as hint for placement;
might be

null
**Returns:** a file object for output
**Throws:** IllegalArgumentException

- if sibling is not known to
this file manager, or if the location is not known to this file
manager and the file manager does not support unknown
locations, or if the kind is not valid, or if the location is
not an output location
**Throws:** IllegalStateException

-

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

- getFileForInput

```java
public
FileObject
getFileForInput​(
JavaFileManager.Location
location,

String
packageName,

String
relativeName)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for input
representing the specified

relative
name

in the specified package in the given package-oriented location.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name. For example, to locate the properties file
"resources/compiler.properties" in the package
"com.sun.tools.javac" in the

SOURCE_PATH

location, this method
might be called like so:

```java
getFileForInput(SOURCE_PATH, "com.sun.tools.javac", "resources/compiler.properties");
```

If the call was executed on Windows, with SOURCE_PATH set to

"C:\Documents and Settings\UncleBob\src\share\classes"

,
a valid result would be a file object representing the file

"C:\Documents and Settings\UncleBob\src\share\classes\com\sun\tools\javac\resources\compiler.properties"

.

**Specified by:** getFileForInput

in interface

JavaFileManager
**Parameters:** location

- a package-oriented location
**Parameters:** packageName

- a package name
**Parameters:** relativeName

- a relative name
**Returns:** a file object, might return

null

if the file
does not exist
**Throws:** IllegalArgumentException

- if the location is not known
to this file manager and the file manager does not support
unknown locations, or if

relativeName

is not valid,
or if the location is a module-oriented location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

- getFileForOutput

```java
public
FileObject
getFileForOutput​(
JavaFileManager.Location
location,

String
packageName,

String
relativeName,

FileObject
sibling)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for output
representing the specified

relative
name

in the specified package in the given location.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name or next to the sibling argument. See

getFileForInput

for an example.

**Specified by:** getFileForOutput

in interface

JavaFileManager
**Parameters:** location

- an output location
**Parameters:** packageName

- a package name
**Parameters:** relativeName

- a relative name
**Parameters:** sibling

- a file object to be used as hint for placement;
might be

null
**Returns:** a file object
**Throws:** IllegalArgumentException

- if sibling is not known to
this file manager, or if the location is not known to this file
manager and the file manager does not support unknown
locations, or if

relativeName

is not valid,
or if the location is not an output location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

- getLocationForModule

```java
public
JavaFileManager.Location
getLocationForModule​(
JavaFileManager.Location
location,

String
moduleName)
throws
IOException
```

Description copied from interface:

JavaFileManager

Gets a location for a named module within a location, which may be either
a module-oriented location or an output location.
The result will be an output location if the given location is
an output location, or it will be a package-oriented location.

**Specified by:** getLocationForModule

in interface

JavaFileManager
**Parameters:** location

- the module-oriented location
**Parameters:** moduleName

- the name of the module to be found
**Returns:** the location for the named module
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- getLocationForModule

```java
public
JavaFileManager.Location
getLocationForModule​(
JavaFileManager.Location
location,

JavaFileObject
fo)
throws
IOException
```

Description copied from interface:

JavaFileManager

Gets a location for the module containing a specific file
to be found within a location, which may be either
a module-oriented location or an output location.
The result will be an output location if the given location is
an output location, or it will be a package-oriented location.

**Specified by:** getLocationForModule

in interface

JavaFileManager
**Parameters:** location

- the module-oriented location
**Parameters:** fo

- the file
**Returns:** the module containing the file
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- getServiceLoader

```java
public <S>
ServiceLoader
<S> getServiceLoader​(
JavaFileManager.Location
location,

Class
<S> service)
throws
IOException
```

Description copied from interface:

JavaFileManager

Get a service loader for a specific service class from a given location.

If the location is a module-oriented location, the service loader will use the
service declarations in the modules found in that location. Otherwise, a service loader
is created using the package-oriented location, in which case, the services are
determined using the provider-configuration files in

META-INF/services

.

**Specified by:** getServiceLoader

in interface

JavaFileManager
**Type Parameters:** S

- the service class
**Parameters:** location

- the module-oriented location
**Parameters:** service

- the

Class

object of the service class
**Returns:** a service loader for the given service class
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- inferModuleName

```java
public
String
inferModuleName​(
JavaFileManager.Location
location)
throws
IOException
```

Description copied from interface:

JavaFileManager

Infer the name of the module from its location, as returned by

getLocationForModule

or

listModuleLocations

.

**Specified by:** inferModuleName

in interface

JavaFileManager
**Parameters:** location

- a package-oriented location representing a module
**Returns:** the name of the module
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- listLocationsForModules

```java
public
Iterable
<
Set
<
JavaFileManager.Location
>> listLocationsForModules​(
JavaFileManager.Location
location)
throws
IOException
```

Description copied from interface:

JavaFileManager

Lists the locations for all the modules in a module-oriented location or an output location.
The locations that are returned will be output locations if the given location is an output,
or it will be a package-oriented locations.

**Specified by:** listLocationsForModules

in interface

JavaFileManager
**Parameters:** location

- the module-oriented location for which to list the modules
**Returns:** a series of sets of locations containing modules
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- contains

```java
public boolean contains​(
JavaFileManager.Location
location,

FileObject
fo)
throws
IOException
```

Description copied from interface:

JavaFileManager

Determines whether or not a given file object is "contained in" a specified location.

For a package-oriented location, a file object is contained in the location if there exist
values for

packageName

and

relativeName

such that either of the following
calls would return the

same

file object:

```java
getFileForInput(location,
packageName
,
relativeName
)
getFileForOutput(location,
packageName
,
relativeName
, null)
```

For a module-oriented location, a file object is contained in the location if there exists
a module that may be obtained by the call:

```java
getLocationForModule(location,
moduleName
)
```

such that the file object is contained in the (package-oriented) location for that module.

**Specified by:** contains

in interface

JavaFileManager
**Parameters:** location

- the location
**Parameters:** fo

- the file object
**Returns:** whether or not the file is contained in the location
**Throws:** IOException

- if there is a problem determining the result
**Since:** 9

Field Detail

- fileManager

```java
protected final
M
extends
JavaFileManager
fileManager
```

The file manager which all methods are delegated to.

---

#### Field Detail

fileManager

```java
protected final
M
extends
JavaFileManager
fileManager
```

The file manager which all methods are delegated to.

---

#### fileManager

protected final

M

extends

JavaFileManager

fileManager

The file manager which all methods are delegated to.

Constructor Detail

- ForwardingJavaFileManager

```java
protected ForwardingJavaFileManager​(
M
fileManager)
```

Creates a new instance of ForwardingJavaFileManager.

**Parameters:** fileManager

- delegate to this file manager

---

#### Constructor Detail

ForwardingJavaFileManager

```java
protected ForwardingJavaFileManager​(
M
fileManager)
```

Creates a new instance of ForwardingJavaFileManager.

**Parameters:** fileManager

- delegate to this file manager

---

#### ForwardingJavaFileManager

protected ForwardingJavaFileManager​(

M

fileManager)

Creates a new instance of ForwardingJavaFileManager.

Method Detail

- getClassLoader

```java
public
ClassLoader
getClassLoader​(
JavaFileManager.Location
location)
```

Description copied from interface:

JavaFileManager

Returns a class loader for loading plug-ins from the given
package-oriented location.
For example, to load annotation processors,
a compiler will request a class loader for the

ANNOTATION_PROCESSOR_PATH

location.

**Specified by:** getClassLoader

in interface

JavaFileManager
**Parameters:** location

- a location
**Returns:** a class loader for the given location; or

null

if loading plug-ins from the given location is disabled or if
the location is not known
**Throws:** SecurityException

- if a class loader can not be created
in the current security context
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

- list

```java
public
Iterable
<
JavaFileObject
> list​(
JavaFileManager.Location
location,

String
packageName,

Set
<
JavaFileObject.Kind
> kinds,
boolean recurse)
throws
IOException
```

Description copied from interface:

JavaFileManager

Lists all file objects matching the given criteria in the given
package-oriented location.
List file objects in "subpackages" if recurse is true.

Note: even if the given location is unknown to this file
manager, it may not return

null

. Also, an unknown
location may not cause an exception.

**Specified by:** list

in interface

JavaFileManager
**Parameters:** location

- a location
**Parameters:** packageName

- a package name
**Parameters:** kinds

- return objects only of these kinds
**Parameters:** recurse

- if true include "subpackages"
**Returns:** an Iterable of file objects matching the given criteria
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

- inferBinaryName

```java
public
String
inferBinaryName​(
JavaFileManager.Location
location,

JavaFileObject
file)
```

Description copied from interface:

JavaFileManager

Infers a binary name of a file object based on a package-oriented location.
The binary name returned might not be a valid binary name according to

The Java™ Language Specification

.

**Specified by:** inferBinaryName

in interface

JavaFileManager
**Parameters:** location

- a location
**Parameters:** file

- a file object
**Returns:** a binary name or

null

the file object is not
found in the given location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

- isSameFile

```java
public boolean isSameFile​(
FileObject
a,

FileObject
b)
```

Description copied from interface:

JavaFileManager

Compares two file objects and return true if they represent the
same underlying object.

**Specified by:** isSameFile

in interface

JavaFileManager
**Parameters:** a

- a file object
**Parameters:** b

- a file object
**Returns:** true if the given file objects represent the same
underlying object
**Throws:** IllegalArgumentException

- if either of the arguments
were created with another file manager and this file manager
does not support foreign file objects

- handleOption

```java
public boolean handleOption​(
String
current,

Iterator
<
String
> remaining)
```

Description copied from interface:

JavaFileManager

Handles one option. If

current

is an option to this
file manager it will consume any arguments to that option from

remaining

and return true, otherwise return false.

**Specified by:** handleOption

in interface

JavaFileManager
**Parameters:** current

- current option
**Parameters:** remaining

- remaining options
**Returns:** true if this option was handled by this file manager,
false otherwise
**Throws:** IllegalArgumentException

- if this option to this file
manager is used incorrectly
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

- getJavaFileForInput

```java
public
JavaFileObject
getJavaFileForInput​(
JavaFileManager.Location
location,

String
className,

JavaFileObject.Kind
kind)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for input
representing the specified class of the specified kind in the
given package-oriented location.

**Specified by:** getJavaFileForInput

in interface

JavaFileManager
**Parameters:** location

- a location
**Parameters:** className

- the name of a class
**Parameters:** kind

- the kind of file, must be one of

SOURCE

or

CLASS
**Returns:** a file object, might return

null

if the
file does not exist
**Throws:** IllegalArgumentException

- if the location is not known
to this file manager and the file manager does not support
unknown locations, or if the kind is not valid, or if the
location is a module-oriented location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

- getJavaFileForOutput

```java
public
JavaFileObject
getJavaFileForOutput​(
JavaFileManager.Location
location,

String
className,

JavaFileObject.Kind
kind,

FileObject
sibling)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for output
representing the specified class of the specified kind in the
given package-oriented location.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

**Specified by:** getJavaFileForOutput

in interface

JavaFileManager
**Parameters:** location

- a package-oriented location
**Parameters:** className

- the name of a class
**Parameters:** kind

- the kind of file, must be one of

SOURCE

or

CLASS
**Parameters:** sibling

- a file object to be used as hint for placement;
might be

null
**Returns:** a file object for output
**Throws:** IllegalArgumentException

- if sibling is not known to
this file manager, or if the location is not known to this file
manager and the file manager does not support unknown
locations, or if the kind is not valid, or if the location is
not an output location
**Throws:** IllegalStateException

-

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

- getFileForInput

```java
public
FileObject
getFileForInput​(
JavaFileManager.Location
location,

String
packageName,

String
relativeName)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for input
representing the specified

relative
name

in the specified package in the given package-oriented location.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name. For example, to locate the properties file
"resources/compiler.properties" in the package
"com.sun.tools.javac" in the

SOURCE_PATH

location, this method
might be called like so:

```java
getFileForInput(SOURCE_PATH, "com.sun.tools.javac", "resources/compiler.properties");
```

If the call was executed on Windows, with SOURCE_PATH set to

"C:\Documents and Settings\UncleBob\src\share\classes"

,
a valid result would be a file object representing the file

"C:\Documents and Settings\UncleBob\src\share\classes\com\sun\tools\javac\resources\compiler.properties"

.

**Specified by:** getFileForInput

in interface

JavaFileManager
**Parameters:** location

- a package-oriented location
**Parameters:** packageName

- a package name
**Parameters:** relativeName

- a relative name
**Returns:** a file object, might return

null

if the file
does not exist
**Throws:** IllegalArgumentException

- if the location is not known
to this file manager and the file manager does not support
unknown locations, or if

relativeName

is not valid,
or if the location is a module-oriented location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

- getFileForOutput

```java
public
FileObject
getFileForOutput​(
JavaFileManager.Location
location,

String
packageName,

String
relativeName,

FileObject
sibling)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for output
representing the specified

relative
name

in the specified package in the given location.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name or next to the sibling argument. See

getFileForInput

for an example.

**Specified by:** getFileForOutput

in interface

JavaFileManager
**Parameters:** location

- an output location
**Parameters:** packageName

- a package name
**Parameters:** relativeName

- a relative name
**Parameters:** sibling

- a file object to be used as hint for placement;
might be

null
**Returns:** a file object
**Throws:** IllegalArgumentException

- if sibling is not known to
this file manager, or if the location is not known to this file
manager and the file manager does not support unknown
locations, or if

relativeName

is not valid,
or if the location is not an output location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

- getLocationForModule

```java
public
JavaFileManager.Location
getLocationForModule​(
JavaFileManager.Location
location,

String
moduleName)
throws
IOException
```

Description copied from interface:

JavaFileManager

Gets a location for a named module within a location, which may be either
a module-oriented location or an output location.
The result will be an output location if the given location is
an output location, or it will be a package-oriented location.

**Specified by:** getLocationForModule

in interface

JavaFileManager
**Parameters:** location

- the module-oriented location
**Parameters:** moduleName

- the name of the module to be found
**Returns:** the location for the named module
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- getLocationForModule

```java
public
JavaFileManager.Location
getLocationForModule​(
JavaFileManager.Location
location,

JavaFileObject
fo)
throws
IOException
```

Description copied from interface:

JavaFileManager

Gets a location for the module containing a specific file
to be found within a location, which may be either
a module-oriented location or an output location.
The result will be an output location if the given location is
an output location, or it will be a package-oriented location.

**Specified by:** getLocationForModule

in interface

JavaFileManager
**Parameters:** location

- the module-oriented location
**Parameters:** fo

- the file
**Returns:** the module containing the file
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- getServiceLoader

```java
public <S>
ServiceLoader
<S> getServiceLoader​(
JavaFileManager.Location
location,

Class
<S> service)
throws
IOException
```

Description copied from interface:

JavaFileManager

Get a service loader for a specific service class from a given location.

If the location is a module-oriented location, the service loader will use the
service declarations in the modules found in that location. Otherwise, a service loader
is created using the package-oriented location, in which case, the services are
determined using the provider-configuration files in

META-INF/services

.

**Specified by:** getServiceLoader

in interface

JavaFileManager
**Type Parameters:** S

- the service class
**Parameters:** location

- the module-oriented location
**Parameters:** service

- the

Class

object of the service class
**Returns:** a service loader for the given service class
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- inferModuleName

```java
public
String
inferModuleName​(
JavaFileManager.Location
location)
throws
IOException
```

Description copied from interface:

JavaFileManager

Infer the name of the module from its location, as returned by

getLocationForModule

or

listModuleLocations

.

**Specified by:** inferModuleName

in interface

JavaFileManager
**Parameters:** location

- a package-oriented location representing a module
**Returns:** the name of the module
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- listLocationsForModules

```java
public
Iterable
<
Set
<
JavaFileManager.Location
>> listLocationsForModules​(
JavaFileManager.Location
location)
throws
IOException
```

Description copied from interface:

JavaFileManager

Lists the locations for all the modules in a module-oriented location or an output location.
The locations that are returned will be output locations if the given location is an output,
or it will be a package-oriented locations.

**Specified by:** listLocationsForModules

in interface

JavaFileManager
**Parameters:** location

- the module-oriented location for which to list the modules
**Returns:** a series of sets of locations containing modules
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

- contains

```java
public boolean contains​(
JavaFileManager.Location
location,

FileObject
fo)
throws
IOException
```

Description copied from interface:

JavaFileManager

Determines whether or not a given file object is "contained in" a specified location.

For a package-oriented location, a file object is contained in the location if there exist
values for

packageName

and

relativeName

such that either of the following
calls would return the

same

file object:

```java
getFileForInput(location,
packageName
,
relativeName
)
getFileForOutput(location,
packageName
,
relativeName
, null)
```

For a module-oriented location, a file object is contained in the location if there exists
a module that may be obtained by the call:

```java
getLocationForModule(location,
moduleName
)
```

such that the file object is contained in the (package-oriented) location for that module.

**Specified by:** contains

in interface

JavaFileManager
**Parameters:** location

- the location
**Parameters:** fo

- the file object
**Returns:** whether or not the file is contained in the location
**Throws:** IOException

- if there is a problem determining the result
**Since:** 9

---

#### Method Detail

getClassLoader

```java
public
ClassLoader
getClassLoader​(
JavaFileManager.Location
location)
```

Description copied from interface:

JavaFileManager

Returns a class loader for loading plug-ins from the given
package-oriented location.
For example, to load annotation processors,
a compiler will request a class loader for the

ANNOTATION_PROCESSOR_PATH

location.

**Specified by:** getClassLoader

in interface

JavaFileManager
**Parameters:** location

- a location
**Returns:** a class loader for the given location; or

null

if loading plug-ins from the given location is disabled or if
the location is not known
**Throws:** SecurityException

- if a class loader can not be created
in the current security context
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

---

#### getClassLoader

public

ClassLoader

getClassLoader​(

JavaFileManager.Location

location)

Description copied from interface:

JavaFileManager

Returns a class loader for loading plug-ins from the given
package-oriented location.
For example, to load annotation processors,
a compiler will request a class loader for the

ANNOTATION_PROCESSOR_PATH

location.

list

```java
public
Iterable
<
JavaFileObject
> list​(
JavaFileManager.Location
location,

String
packageName,

Set
<
JavaFileObject.Kind
> kinds,
boolean recurse)
throws
IOException
```

Description copied from interface:

JavaFileManager

Lists all file objects matching the given criteria in the given
package-oriented location.
List file objects in "subpackages" if recurse is true.

Note: even if the given location is unknown to this file
manager, it may not return

null

. Also, an unknown
location may not cause an exception.

**Specified by:** list

in interface

JavaFileManager
**Parameters:** location

- a location
**Parameters:** packageName

- a package name
**Parameters:** kinds

- return objects only of these kinds
**Parameters:** recurse

- if true include "subpackages"
**Returns:** an Iterable of file objects matching the given criteria
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

---

#### list

public

Iterable

<

JavaFileObject

> list​(

JavaFileManager.Location

location,

String

packageName,

Set

<

JavaFileObject.Kind

> kinds,
boolean recurse)
throws

IOException

Description copied from interface:

JavaFileManager

Lists all file objects matching the given criteria in the given
package-oriented location.
List file objects in "subpackages" if recurse is true.

Note: even if the given location is unknown to this file
manager, it may not return

null

. Also, an unknown
location may not cause an exception.

Note: even if the given location is unknown to this file
manager, it may not return

null

. Also, an unknown
location may not cause an exception.

inferBinaryName

```java
public
String
inferBinaryName​(
JavaFileManager.Location
location,

JavaFileObject
file)
```

Description copied from interface:

JavaFileManager

Infers a binary name of a file object based on a package-oriented location.
The binary name returned might not be a valid binary name according to

The Java™ Language Specification

.

**Specified by:** inferBinaryName

in interface

JavaFileManager
**Parameters:** location

- a location
**Parameters:** file

- a file object
**Returns:** a binary name or

null

the file object is not
found in the given location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

---

#### inferBinaryName

public

String

inferBinaryName​(

JavaFileManager.Location

location,

JavaFileObject

file)

Description copied from interface:

JavaFileManager

Infers a binary name of a file object based on a package-oriented location.
The binary name returned might not be a valid binary name according to

The Java™ Language Specification

.

isSameFile

```java
public boolean isSameFile​(
FileObject
a,

FileObject
b)
```

Description copied from interface:

JavaFileManager

Compares two file objects and return true if they represent the
same underlying object.

**Specified by:** isSameFile

in interface

JavaFileManager
**Parameters:** a

- a file object
**Parameters:** b

- a file object
**Returns:** true if the given file objects represent the same
underlying object
**Throws:** IllegalArgumentException

- if either of the arguments
were created with another file manager and this file manager
does not support foreign file objects

---

#### isSameFile

public boolean isSameFile​(

FileObject

a,

FileObject

b)

Description copied from interface:

JavaFileManager

Compares two file objects and return true if they represent the
same underlying object.

handleOption

```java
public boolean handleOption​(
String
current,

Iterator
<
String
> remaining)
```

Description copied from interface:

JavaFileManager

Handles one option. If

current

is an option to this
file manager it will consume any arguments to that option from

remaining

and return true, otherwise return false.

**Specified by:** handleOption

in interface

JavaFileManager
**Parameters:** current

- current option
**Parameters:** remaining

- remaining options
**Returns:** true if this option was handled by this file manager,
false otherwise
**Throws:** IllegalArgumentException

- if this option to this file
manager is used incorrectly
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened

---

#### handleOption

public boolean handleOption​(

String

current,

Iterator

<

String

> remaining)

Description copied from interface:

JavaFileManager

Handles one option. If

current

is an option to this
file manager it will consume any arguments to that option from

remaining

and return true, otherwise return false.

getJavaFileForInput

```java
public
JavaFileObject
getJavaFileForInput​(
JavaFileManager.Location
location,

String
className,

JavaFileObject.Kind
kind)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for input
representing the specified class of the specified kind in the
given package-oriented location.

**Specified by:** getJavaFileForInput

in interface

JavaFileManager
**Parameters:** location

- a location
**Parameters:** className

- the name of a class
**Parameters:** kind

- the kind of file, must be one of

SOURCE

or

CLASS
**Returns:** a file object, might return

null

if the
file does not exist
**Throws:** IllegalArgumentException

- if the location is not known
to this file manager and the file manager does not support
unknown locations, or if the kind is not valid, or if the
location is a module-oriented location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

---

#### getJavaFileForInput

public

JavaFileObject

getJavaFileForInput​(

JavaFileManager.Location

location,

String

className,

JavaFileObject.Kind

kind)
throws

IOException

Description copied from interface:

JavaFileManager

Returns a

file object

for input
representing the specified class of the specified kind in the
given package-oriented location.

getJavaFileForOutput

```java
public
JavaFileObject
getJavaFileForOutput​(
JavaFileManager.Location
location,

String
className,

JavaFileObject.Kind
kind,

FileObject
sibling)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for output
representing the specified class of the specified kind in the
given package-oriented location.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

**Specified by:** getJavaFileForOutput

in interface

JavaFileManager
**Parameters:** location

- a package-oriented location
**Parameters:** className

- the name of a class
**Parameters:** kind

- the kind of file, must be one of

SOURCE

or

CLASS
**Parameters:** sibling

- a file object to be used as hint for placement;
might be

null
**Returns:** a file object for output
**Throws:** IllegalArgumentException

- if sibling is not known to
this file manager, or if the location is not known to this file
manager and the file manager does not support unknown
locations, or if the kind is not valid, or if the location is
not an output location
**Throws:** IllegalStateException

-

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

---

#### getJavaFileForOutput

public

JavaFileObject

getJavaFileForOutput​(

JavaFileManager.Location

location,

String

className,

JavaFileObject.Kind

kind,

FileObject

sibling)
throws

IOException

Description copied from interface:

JavaFileManager

Returns a

file object

for output
representing the specified class of the specified kind in the
given package-oriented location.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

getFileForInput

```java
public
FileObject
getFileForInput​(
JavaFileManager.Location
location,

String
packageName,

String
relativeName)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for input
representing the specified

relative
name

in the specified package in the given package-oriented location.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name. For example, to locate the properties file
"resources/compiler.properties" in the package
"com.sun.tools.javac" in the

SOURCE_PATH

location, this method
might be called like so:

```java
getFileForInput(SOURCE_PATH, "com.sun.tools.javac", "resources/compiler.properties");
```

If the call was executed on Windows, with SOURCE_PATH set to

"C:\Documents and Settings\UncleBob\src\share\classes"

,
a valid result would be a file object representing the file

"C:\Documents and Settings\UncleBob\src\share\classes\com\sun\tools\javac\resources\compiler.properties"

.

**Specified by:** getFileForInput

in interface

JavaFileManager
**Parameters:** location

- a package-oriented location
**Parameters:** packageName

- a package name
**Parameters:** relativeName

- a relative name
**Returns:** a file object, might return

null

if the file
does not exist
**Throws:** IllegalArgumentException

- if the location is not known
to this file manager and the file manager does not support
unknown locations, or if

relativeName

is not valid,
or if the location is a module-oriented location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

---

#### getFileForInput

public

FileObject

getFileForInput​(

JavaFileManager.Location

location,

String

packageName,

String

relativeName)
throws

IOException

Description copied from interface:

JavaFileManager

Returns a

file object

for input
representing the specified

relative
name

in the specified package in the given package-oriented location.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name. For example, to locate the properties file
"resources/compiler.properties" in the package
"com.sun.tools.javac" in the

SOURCE_PATH

location, this method
might be called like so:

```java
getFileForInput(SOURCE_PATH, "com.sun.tools.javac", "resources/compiler.properties");
```

If the call was executed on Windows, with SOURCE_PATH set to

"C:\Documents and Settings\UncleBob\src\share\classes"

,
a valid result would be a file object representing the file

"C:\Documents and Settings\UncleBob\src\share\classes\com\sun\tools\javac\resources\compiler.properties"

.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name. For example, to locate the properties file
"resources/compiler.properties" in the package
"com.sun.tools.javac" in the

SOURCE_PATH

location, this method
might be called like so:

```java
getFileForInput(SOURCE_PATH, "com.sun.tools.javac", "resources/compiler.properties");
```

If the call was executed on Windows, with SOURCE_PATH set to

"C:\Documents and Settings\UncleBob\src\share\classes"

,
a valid result would be a file object representing the file

"C:\Documents and Settings\UncleBob\src\share\classes\com\sun\tools\javac\resources\compiler.properties"

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name. For example, to locate the properties file
"resources/compiler.properties" in the package
"com.sun.tools.javac" in the

SOURCE_PATH

location, this method
might be called like so:

```java
getFileForInput(SOURCE_PATH, "com.sun.tools.javac", "resources/compiler.properties");
```

If the call was executed on Windows, with SOURCE_PATH set to

"C:\Documents and Settings\UncleBob\src\share\classes"

,
a valid result would be a file object representing the file

"C:\Documents and Settings\UncleBob\src\share\classes\com\sun\tools\javac\resources\compiler.properties"

.

getFileForInput(SOURCE_PATH, "com.sun.tools.javac", "resources/compiler.properties");

If the call was executed on Windows, with SOURCE_PATH set to

"C:\Documents and Settings\UncleBob\src\share\classes"

,
a valid result would be a file object representing the file

"C:\Documents and Settings\UncleBob\src\share\classes\com\sun\tools\javac\resources\compiler.properties"

.

getFileForOutput

```java
public
FileObject
getFileForOutput​(
JavaFileManager.Location
location,

String
packageName,

String
relativeName,

FileObject
sibling)
throws
IOException
```

Description copied from interface:

JavaFileManager

Returns a

file object

for output
representing the specified

relative
name

in the specified package in the given location.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name or next to the sibling argument. See

getFileForInput

for an example.

**Specified by:** getFileForOutput

in interface

JavaFileManager
**Parameters:** location

- an output location
**Parameters:** packageName

- a package name
**Parameters:** relativeName

- a relative name
**Parameters:** sibling

- a file object to be used as hint for placement;
might be

null
**Returns:** a file object
**Throws:** IllegalArgumentException

- if sibling is not known to
this file manager, or if the location is not known to this file
manager and the file manager does not support unknown
locations, or if

relativeName

is not valid,
or if the location is not an output location
**Throws:** IllegalStateException

- if

JavaFileManager.close()

has been called
and this file manager cannot be reopened
**Throws:** IOException

- if an I/O error occurred, or if

JavaFileManager.close()

has been called and this file manager cannot be
reopened

---

#### getFileForOutput

public

FileObject

getFileForOutput​(

JavaFileManager.Location

location,

String

packageName,

String

relativeName,

FileObject

sibling)
throws

IOException

Description copied from interface:

JavaFileManager

Returns a

file object

for output
representing the specified

relative
name

in the specified package in the given location.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name or next to the sibling argument. See

getFileForInput

for an example.

Optionally, this file manager might consider the sibling as
a hint for where to place the output. The exact semantics of
this hint is unspecified. The JDK compiler, javac, for
example, will place class files in the same directories as
originating source files unless a class file output directory
is provided. To facilitate this behavior, javac might provide
the originating source file as sibling when calling this
method.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name or next to the sibling argument. See

getFileForInput

for an example.

If the returned object represents a

source

or

class

file, it must be an instance
of

JavaFileObject

.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name or next to the sibling argument. See

getFileForInput

for an example.

Informally, the file object returned by this method is
located in the concatenation of the location, package name, and
relative name or next to the sibling argument. See

getFileForInput

for an example.

getLocationForModule

```java
public
JavaFileManager.Location
getLocationForModule​(
JavaFileManager.Location
location,

String
moduleName)
throws
IOException
```

Description copied from interface:

JavaFileManager

Gets a location for a named module within a location, which may be either
a module-oriented location or an output location.
The result will be an output location if the given location is
an output location, or it will be a package-oriented location.

**Specified by:** getLocationForModule

in interface

JavaFileManager
**Parameters:** location

- the module-oriented location
**Parameters:** moduleName

- the name of the module to be found
**Returns:** the location for the named module
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

---

#### getLocationForModule

public

JavaFileManager.Location

getLocationForModule​(

JavaFileManager.Location

location,

String

moduleName)
throws

IOException

Description copied from interface:

JavaFileManager

Gets a location for a named module within a location, which may be either
a module-oriented location or an output location.
The result will be an output location if the given location is
an output location, or it will be a package-oriented location.

getLocationForModule

```java
public
JavaFileManager.Location
getLocationForModule​(
JavaFileManager.Location
location,

JavaFileObject
fo)
throws
IOException
```

Description copied from interface:

JavaFileManager

Gets a location for the module containing a specific file
to be found within a location, which may be either
a module-oriented location or an output location.
The result will be an output location if the given location is
an output location, or it will be a package-oriented location.

**Specified by:** getLocationForModule

in interface

JavaFileManager
**Parameters:** location

- the module-oriented location
**Parameters:** fo

- the file
**Returns:** the module containing the file
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

---

#### getLocationForModule

public

JavaFileManager.Location

getLocationForModule​(

JavaFileManager.Location

location,

JavaFileObject

fo)
throws

IOException

Description copied from interface:

JavaFileManager

Gets a location for the module containing a specific file
to be found within a location, which may be either
a module-oriented location or an output location.
The result will be an output location if the given location is
an output location, or it will be a package-oriented location.

getServiceLoader

```java
public <S>
ServiceLoader
<S> getServiceLoader​(
JavaFileManager.Location
location,

Class
<S> service)
throws
IOException
```

Description copied from interface:

JavaFileManager

Get a service loader for a specific service class from a given location.

If the location is a module-oriented location, the service loader will use the
service declarations in the modules found in that location. Otherwise, a service loader
is created using the package-oriented location, in which case, the services are
determined using the provider-configuration files in

META-INF/services

.

**Specified by:** getServiceLoader

in interface

JavaFileManager
**Type Parameters:** S

- the service class
**Parameters:** location

- the module-oriented location
**Parameters:** service

- the

Class

object of the service class
**Returns:** a service loader for the given service class
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

---

#### getServiceLoader

public <S>

ServiceLoader

<S> getServiceLoader​(

JavaFileManager.Location

location,

Class

<S> service)
throws

IOException

Description copied from interface:

JavaFileManager

Get a service loader for a specific service class from a given location.

If the location is a module-oriented location, the service loader will use the
service declarations in the modules found in that location. Otherwise, a service loader
is created using the package-oriented location, in which case, the services are
determined using the provider-configuration files in

META-INF/services

.

inferModuleName

```java
public
String
inferModuleName​(
JavaFileManager.Location
location)
throws
IOException
```

Description copied from interface:

JavaFileManager

Infer the name of the module from its location, as returned by

getLocationForModule

or

listModuleLocations

.

**Specified by:** inferModuleName

in interface

JavaFileManager
**Parameters:** location

- a package-oriented location representing a module
**Returns:** the name of the module
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

---

#### inferModuleName

public

String

inferModuleName​(

JavaFileManager.Location

location)
throws

IOException

Description copied from interface:

JavaFileManager

Infer the name of the module from its location, as returned by

getLocationForModule

or

listModuleLocations

.

listLocationsForModules

```java
public
Iterable
<
Set
<
JavaFileManager.Location
>> listLocationsForModules​(
JavaFileManager.Location
location)
throws
IOException
```

Description copied from interface:

JavaFileManager

Lists the locations for all the modules in a module-oriented location or an output location.
The locations that are returned will be output locations if the given location is an output,
or it will be a package-oriented locations.

**Specified by:** listLocationsForModules

in interface

JavaFileManager
**Parameters:** location

- the module-oriented location for which to list the modules
**Returns:** a series of sets of locations containing modules
**Throws:** IOException

- if an I/O error occurred
**Since:** 9

---

#### listLocationsForModules

public

Iterable

<

Set

<

JavaFileManager.Location

>> listLocationsForModules​(

JavaFileManager.Location

location)
throws

IOException

Description copied from interface:

JavaFileManager

Lists the locations for all the modules in a module-oriented location or an output location.
The locations that are returned will be output locations if the given location is an output,
or it will be a package-oriented locations.

contains

```java
public boolean contains​(
JavaFileManager.Location
location,

FileObject
fo)
throws
IOException
```

Description copied from interface:

JavaFileManager

Determines whether or not a given file object is "contained in" a specified location.

For a package-oriented location, a file object is contained in the location if there exist
values for

packageName

and

relativeName

such that either of the following
calls would return the

same

file object:

```java
getFileForInput(location,
packageName
,
relativeName
)
getFileForOutput(location,
packageName
,
relativeName
, null)
```

For a module-oriented location, a file object is contained in the location if there exists
a module that may be obtained by the call:

```java
getLocationForModule(location,
moduleName
)
```

such that the file object is contained in the (package-oriented) location for that module.

**Specified by:** contains

in interface

JavaFileManager
**Parameters:** location

- the location
**Parameters:** fo

- the file object
**Returns:** whether or not the file is contained in the location
**Throws:** IOException

- if there is a problem determining the result
**Since:** 9

---

#### contains

public boolean contains​(

JavaFileManager.Location

location,

FileObject

fo)
throws

IOException

Description copied from interface:

JavaFileManager

Determines whether or not a given file object is "contained in" a specified location.

For a package-oriented location, a file object is contained in the location if there exist
values for

packageName

and

relativeName

such that either of the following
calls would return the

same

file object:

```java
getFileForInput(location,
packageName
,
relativeName
)
getFileForOutput(location,
packageName
,
relativeName
, null)
```

For a module-oriented location, a file object is contained in the location if there exists
a module that may be obtained by the call:

```java
getLocationForModule(location,
moduleName
)
```

such that the file object is contained in the (package-oriented) location for that module.

For a package-oriented location, a file object is contained in the location if there exist
values for

packageName

and

relativeName

such that either of the following
calls would return the

same

file object:

```java
getFileForInput(location,
packageName
,
relativeName
)
getFileForOutput(location,
packageName
,
relativeName
, null)
```

For a module-oriented location, a file object is contained in the location if there exists
a module that may be obtained by the call:

```java
getLocationForModule(location,
moduleName
)
```

such that the file object is contained in the (package-oriented) location for that module.

getFileForInput(location,

packageName

,

relativeName

)
getFileForOutput(location,

packageName

,

relativeName

, null)

For a module-oriented location, a file object is contained in the location if there exists
a module that may be obtained by the call:

```java
getLocationForModule(location,
moduleName
)
```

such that the file object is contained in the (package-oriented) location for that module.

getLocationForModule(location,

moduleName

)

---

