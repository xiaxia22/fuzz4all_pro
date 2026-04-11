# Interface StandardJavaFileManager

**Source:** `java.compiler\javax\tools\StandardJavaFileManager.html`

### Class Description

```java
public interface
StandardJavaFileManager

extends
JavaFileManager
```

File manager based on

java.io.File

and

java.nio.file.Path

.

A common way to obtain an instance of this class is using

getStandardFileManager

, for example:

```java
JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();

DiagnosticCollector<JavaFileObject>
diagnostics =
new
DiagnosticCollector<JavaFileObject>()
;
StandardJavaFileManager fm = compiler.getStandardFileManager(diagnostics, null, null);
```

This file manager creates file objects representing regular

files

,

zip file entries

, or entries in
similar file system based containers. Any file object returned
from a file manager implementing this interface must observe the
following behavior:

- File names need not be canonical.
- For file objects representing regular files

- the method

FileObject.delete()

is equivalent to

File.delete()

,
- the method

FileObject.getLastModified()

is equivalent to

File.lastModified()

,
- the methods

FileObject.getCharContent(boolean)

,

FileObject.openInputStream()

, and

FileObject.openReader(boolean)

must succeed if the following would succeed (ignoring
encoding issues):

```java
new
FileInputStream
(new
File
(
fileObject
.
toUri
()))
```
- and the methods

FileObject.openOutputStream()

, and

FileObject.openWriter()

must
succeed if the following would succeed (ignoring encoding
issues):

```java
new
FileOutputStream
(new
File
(
fileObject
.
toUri
()))
```
- The

URI

returned from

FileObject.toUri()

- must be

absolute

(have a schema), and
- must have a

normalized

path component

which
can be resolved without any process-specific context such
as the current directory (file names must be absolute).

According to these rules, the following URIs, for example, are
allowed:

- file:///C:/Documents%20and%20Settings/UncleBob/BobsApp/Test.java
- jar:///C:/Documents%20and%20Settings/UncleBob/lib/vendorA.jar!/com/vendora/LibraryClass.class

Whereas these are not (reason in parentheses):

- file:BobsApp/Test.java

(the file name is relative
and depend on the current directory)
- jar:lib/vendorA.jar!/com/vendora/LibraryClass.class

(the first half of the path depends on the current directory,
whereas the component after ! is legal)
- Test.java

(this URI depends on the current
directory and does not have a schema)
- jar:///C:/Documents%20and%20Settings/UncleBob/BobsApp/../lib/vendorA.jar!com/vendora/LibraryClass.class

(the path is not normalized)

All implementations of this interface must support Path objects representing
files in the

default file system.

It is recommended that implementations should support Path objects from any filesystem.

**All Superinterfaces:** AutoCloseable

,

Closeable

,

Flushable

,

JavaFileManager

,

OptionChecker

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isSameFile​(
FileObject
a,

FileObject
b)

Compares two file objects and return true if they represent the
same canonical file, zip file entry, or entry in any file
system based container.

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
canonical file, zip file entry or path; false otherwise

**Throws:**
- IllegalArgumentException

- if either of the arguments
were created with another file manager implementation

---

#### Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromFiles​(
Iterable
<? extends
File
> files)

Returns file objects representing the given files.

**Parameters:**
- files

- a list of files

**Returns:**
- a list of file objects

**Throws:**
- IllegalArgumentException

- if the list of files includes
a directory

---

#### default
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromPaths​(
Iterable
<? extends
Path
> paths)

Returns file objects representing the given paths.

**Parameters:**
- paths

- a list of paths

**Returns:**
- a list of file objects

**Throws:**
- IllegalArgumentException

- if the list of paths includes
a directory or if this file manager does not support any of the
given paths.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation converts each path to a file and calls

getJavaObjectsFromFiles

.
IllegalArgumentException will be thrown if any of the paths
cannot be converted to a file.

---

#### Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
File
... files)

Returns file objects representing the given files.
Convenience method equivalent to:

```java
getJavaFileObjectsFromFiles(
Arrays.asList
(files))
```

**Parameters:**
- files

- an array of files

**Returns:**
- a list of file objects

**Throws:**
- IllegalArgumentException

- if the array of files includes
a directory
- NullPointerException

- if the given array contains null
elements

---

#### default
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
Path
... paths)

Returns file objects representing the given paths.
Convenience method equivalent to:

```java
getJavaFileObjectsFromPaths(
Arrays.asList
(paths))
```

**Parameters:**
- paths

- an array of paths

**Returns:**
- a list of file objects

**Throws:**
- IllegalArgumentException

- if the array of files includes
a directory
- NullPointerException

- if the given array contains null
elements

**Since:**
- 9

---

#### Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromStrings​(
Iterable
<
String
> names)

Returns file objects representing the given file names.

**Parameters:**
- names

- a list of file names

**Returns:**
- a list of file objects

**Throws:**
- IllegalArgumentException

- if the list of file names
includes a directory

---

#### Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
String
... names)

Returns file objects representing the given file names.
Convenience method equivalent to:

```java
getJavaFileObjectsFromStrings(
Arrays.asList
(names))
```

**Parameters:**
- names

- a list of file names

**Returns:**
- a list of file objects

**Throws:**
- IllegalArgumentException

- if the array of file names
includes a directory
- NullPointerException

- if the given array contains null
elements

---

#### void setLocation​(
JavaFileManager.Location
location,

Iterable
<? extends
File
> files)
throws
IOException

Associates the given search path with the given location. Any
previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

**Parameters:**
- location

- a location
- files

- a list of files, if

null

use the default
search path for this location

**Throws:**
- IllegalArgumentException

- if

location

is an output
location and

files

does not contain exactly one element
- IOException

- if

location

is an output location and
does not represent an existing directory

**See Also:**
- getLocation(javax.tools.JavaFileManager.Location)

---

#### default void setLocationFromPaths​(
JavaFileManager.Location
location,

Collection
<? extends
Path
> paths)
throws
IOException

Associates the given search path with the given location.
Any previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

**Parameters:**
- location

- a location
- paths

- a list of paths, if

null

use the default
search path for this location

**Throws:**
- IllegalArgumentException

- if

location

is an output
location and

paths

does not contain exactly one element
or if this file manager does not support any of the given paths
- IOException

- if

location

is an output location and

paths

does not represent an existing directory

**See Also:**
- getLocation(javax.tools.JavaFileManager.Location)

**Since:**
- 9

**Implementation Requirements:**
- The default implementation converts each path to a file and calls

getJavaObjectsFromFiles

.

IllegalArgumentException

will be thrown if any of the paths cannot be converted to a file.

---

#### default void setLocationForModule​(
JavaFileManager.Location
location,

String
moduleName,

Collection
<? extends
Path
> paths)
throws
IOException

Associates the given search path with the given module and location,
which must be a module-oriented or output location.
Any previous value will be discarded.
This overrides any default association derived from the search path
associated with the location itself.

All such module-specific associations will be cancelled if a
new search path is associated with the location by calling

setLocation

or

setLocationFromPaths

.

**Parameters:**
- location

- the location
- moduleName

- the name of the module
- paths

- the search path to associate with the location and module.

**Throws:**
- IllegalStateException

- if the location is not a module-oriented
or output location.
- UnsupportedOperationException

- if this operation is not supported by
this file manager.
- IOException

- if

location

is an output location and

paths

does not represent an existing directory

**See Also:**
- setLocation(javax.tools.JavaFileManager.Location,java.lang.Iterable<? extends java.io.File>)

,

setLocationFromPaths(javax.tools.JavaFileManager.Location,java.util.Collection<? extends java.nio.file.Path>)

**Since:**
- 9

---

#### Iterable
<? extends
File
> getLocation​(
JavaFileManager.Location
location)

Returns the search path associated with the given location.

**Parameters:**
- location

- a location

**Returns:**
- a list of files or

null

if this location has no
associated search path

**Throws:**
- IllegalStateException

- if any element of the search path
cannot be converted to a

File

, or if the search path
cannot be represented as a simple series of files.

**See Also:**
- setLocation(javax.tools.JavaFileManager.Location, java.lang.Iterable<? extends java.io.File>)

,

Path.toFile()

---

#### default
Iterable
<? extends
Path
> getLocationAsPaths​(
JavaFileManager.Location
location)

Returns the search path associated with the given location.

**Parameters:**
- location

- a location

**Returns:**
- a list of paths or

null

if this location has no
associated search path

**Throws:**
- IllegalStateException

- if the search path cannot be represented
as a simple series of paths.

**See Also:**
- setLocationFromPaths(javax.tools.JavaFileManager.Location, java.util.Collection<? extends java.nio.file.Path>)

**Since:**
- 9

**Implementation Requirements:**
- The default implementation calls

getLocation

and then returns an

Iterable

formed by calling

toPath()

on each

File

returned from

getLocation

.

---

#### default
Path
asPath​(
FileObject
file)

Returns the path, if any, underlying this file object (optional operation).
File objects derived from a

FileSystem

,
including the default file system, typically have a corresponding underlying

Path

object. In such cases, this method may be
used to access that object.

**Parameters:**
- file

- a file object

**Returns:**
- a path representing the same underlying file system artifact

**Throws:**
- IllegalArgumentException

- if the file object does not have an underlying path
- UnsupportedOperationException

- if the operation is not supported by this file manager

**Since:**
- 9

**Implementation Requirements:**
- The default implementation throws

UnsupportedOperationException

for all files.

---

#### default void setPathFactory​(
StandardJavaFileManager.PathFactory
f)

Specify a factory that can be used to generate a path from a string, or series of strings.

If this method is not called, a factory whose

getPath

method is
equivalent to calling

java.nio.file.Paths.get(first, more)

will be used.

**Parameters:**
- f

- the factory

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method ignores the factory that is provided.

---

### Additional Sections

#### Interface StandardJavaFileManager

**All Superinterfaces:** AutoCloseable

,

Closeable

,

Flushable

,

JavaFileManager

,

OptionChecker

```java
public interface
StandardJavaFileManager

extends
JavaFileManager
```

File manager based on

java.io.File

and

java.nio.file.Path

.

A common way to obtain an instance of this class is using

getStandardFileManager

, for example:

```java
JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();

DiagnosticCollector<JavaFileObject>
diagnostics =
new
DiagnosticCollector<JavaFileObject>()
;
StandardJavaFileManager fm = compiler.getStandardFileManager(diagnostics, null, null);
```

This file manager creates file objects representing regular

files

,

zip file entries

, or entries in
similar file system based containers. Any file object returned
from a file manager implementing this interface must observe the
following behavior:

- File names need not be canonical.
- For file objects representing regular files

- the method

FileObject.delete()

is equivalent to

File.delete()

,
- the method

FileObject.getLastModified()

is equivalent to

File.lastModified()

,
- the methods

FileObject.getCharContent(boolean)

,

FileObject.openInputStream()

, and

FileObject.openReader(boolean)

must succeed if the following would succeed (ignoring
encoding issues):

```java
new
FileInputStream
(new
File
(
fileObject
.
toUri
()))
```
- and the methods

FileObject.openOutputStream()

, and

FileObject.openWriter()

must
succeed if the following would succeed (ignoring encoding
issues):

```java
new
FileOutputStream
(new
File
(
fileObject
.
toUri
()))
```
- The

URI

returned from

FileObject.toUri()

- must be

absolute

(have a schema), and
- must have a

normalized

path component

which
can be resolved without any process-specific context such
as the current directory (file names must be absolute).

According to these rules, the following URIs, for example, are
allowed:

- file:///C:/Documents%20and%20Settings/UncleBob/BobsApp/Test.java
- jar:///C:/Documents%20and%20Settings/UncleBob/lib/vendorA.jar!/com/vendora/LibraryClass.class

Whereas these are not (reason in parentheses):

- file:BobsApp/Test.java

(the file name is relative
and depend on the current directory)
- jar:lib/vendorA.jar!/com/vendora/LibraryClass.class

(the first half of the path depends on the current directory,
whereas the component after ! is legal)
- Test.java

(this URI depends on the current
directory and does not have a schema)
- jar:///C:/Documents%20and%20Settings/UncleBob/BobsApp/../lib/vendorA.jar!com/vendora/LibraryClass.class

(the path is not normalized)

All implementations of this interface must support Path objects representing
files in the

default file system.

It is recommended that implementations should support Path objects from any filesystem.

**API Note:** Some methods on this interface take a

Collection<? extends Path>

instead of

Iterable<? extends Path>

.
This is to prevent the possibility of accidentally calling the method
with a single

Path

as such an argument, because although

Path

implements

Iterable<Path>

, it would almost never be
correct to call these methods with a single

Path

and have it be treated as
an

Iterable

of its components.
**Since:** 1.6

public interface

StandardJavaFileManager

extends

JavaFileManager

File manager based on

java.io.File

and

java.nio.file.Path

.

A common way to obtain an instance of this class is using

getStandardFileManager

, for example:

```java
JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();

DiagnosticCollector<JavaFileObject>
diagnostics =
new
DiagnosticCollector<JavaFileObject>()
;
StandardJavaFileManager fm = compiler.getStandardFileManager(diagnostics, null, null);
```

This file manager creates file objects representing regular

files

,

zip file entries

, or entries in
similar file system based containers. Any file object returned
from a file manager implementing this interface must observe the
following behavior:

- File names need not be canonical.
- For file objects representing regular files

- the method

FileObject.delete()

is equivalent to

File.delete()

,
- the method

FileObject.getLastModified()

is equivalent to

File.lastModified()

,
- the methods

FileObject.getCharContent(boolean)

,

FileObject.openInputStream()

, and

FileObject.openReader(boolean)

must succeed if the following would succeed (ignoring
encoding issues):

```java
new
FileInputStream
(new
File
(
fileObject
.
toUri
()))
```
- and the methods

FileObject.openOutputStream()

, and

FileObject.openWriter()

must
succeed if the following would succeed (ignoring encoding
issues):

```java
new
FileOutputStream
(new
File
(
fileObject
.
toUri
()))
```
- The

URI

returned from

FileObject.toUri()

- must be

absolute

(have a schema), and
- must have a

normalized

path component

which
can be resolved without any process-specific context such
as the current directory (file names must be absolute).

According to these rules, the following URIs, for example, are
allowed:

- file:///C:/Documents%20and%20Settings/UncleBob/BobsApp/Test.java
- jar:///C:/Documents%20and%20Settings/UncleBob/lib/vendorA.jar!/com/vendora/LibraryClass.class

Whereas these are not (reason in parentheses):

- file:BobsApp/Test.java

(the file name is relative
and depend on the current directory)
- jar:lib/vendorA.jar!/com/vendora/LibraryClass.class

(the first half of the path depends on the current directory,
whereas the component after ! is legal)
- Test.java

(this URI depends on the current
directory and does not have a schema)
- jar:///C:/Documents%20and%20Settings/UncleBob/BobsApp/../lib/vendorA.jar!com/vendora/LibraryClass.class

(the path is not normalized)

All implementations of this interface must support Path objects representing
files in the

default file system.

It is recommended that implementations should support Path objects from any filesystem.

JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();

DiagnosticCollector<JavaFileObject>

diagnostics =
new

DiagnosticCollector<JavaFileObject>()

;
StandardJavaFileManager fm = compiler.getStandardFileManager(diagnostics, null, null);

File names need not be canonical.

For file objects representing regular files

- the method

FileObject.delete()

is equivalent to

File.delete()

,
- the method

FileObject.getLastModified()

is equivalent to

File.lastModified()

,
- the methods

FileObject.getCharContent(boolean)

,

FileObject.openInputStream()

, and

FileObject.openReader(boolean)

must succeed if the following would succeed (ignoring
encoding issues):

```java
new
FileInputStream
(new
File
(
fileObject
.
toUri
()))
```
- and the methods

FileObject.openOutputStream()

, and

FileObject.openWriter()

must
succeed if the following would succeed (ignoring encoding
issues):

```java
new
FileOutputStream
(new
File
(
fileObject
.
toUri
()))
```

The

URI

returned from

FileObject.toUri()

- must be

absolute

(have a schema), and
- must have a

normalized

path component

which
can be resolved without any process-specific context such
as the current directory (file names must be absolute).

the method

FileObject.delete()

is equivalent to

File.delete()

,

the method

FileObject.getLastModified()

is equivalent to

File.lastModified()

,

the methods

FileObject.getCharContent(boolean)

,

FileObject.openInputStream()

, and

FileObject.openReader(boolean)

must succeed if the following would succeed (ignoring
encoding issues):

```java
new
FileInputStream
(new
File
(
fileObject
.
toUri
()))
```

and the methods

FileObject.openOutputStream()

, and

FileObject.openWriter()

must
succeed if the following would succeed (ignoring encoding
issues):

```java
new
FileOutputStream
(new
File
(
fileObject
.
toUri
()))
```

new

FileInputStream

(new

File

(

fileObject

.

toUri

()))

new

FileOutputStream

(new

File

(

fileObject

.

toUri

()))

must be

absolute

(have a schema), and

must have a

normalized

path component

which
can be resolved without any process-specific context such
as the current directory (file names must be absolute).

file:///C:/Documents%20and%20Settings/UncleBob/BobsApp/Test.java

jar:///C:/Documents%20and%20Settings/UncleBob/lib/vendorA.jar!/com/vendora/LibraryClass.class

file:BobsApp/Test.java

(the file name is relative
and depend on the current directory)

jar:lib/vendorA.jar!/com/vendora/LibraryClass.class

(the first half of the path depends on the current directory,
whereas the component after ! is legal)

Test.java

(this URI depends on the current
directory and does not have a schema)

jar:///C:/Documents%20and%20Settings/UncleBob/BobsApp/../lib/vendorA.jar!com/vendora/LibraryClass.class

(the path is not normalized)

All implementations of this interface must support Path objects representing
files in the

default file system.

It is recommended that implementations should support Path objects from any filesystem.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

StandardJavaFileManager.PathFactory

Factory to create

Path

objects from strings.

- Nested classes/interfaces declared in interface javax.tools.

JavaFileManager

JavaFileManager.Location

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

Path

asPath

​(

FileObject

file)

Returns the path, if any, underlying this file object (optional operation).

Iterable

<? extends

JavaFileObject

>

getJavaFileObjects

​(

File

... files)

Returns file objects representing the given files.

Iterable

<? extends

JavaFileObject

>

getJavaFileObjects

​(

String

... names)

Returns file objects representing the given file names.

default

Iterable

<? extends

JavaFileObject

>

getJavaFileObjects

​(

Path

... paths)

Returns file objects representing the given paths.

Iterable

<? extends

JavaFileObject

>

getJavaFileObjectsFromFiles

​(

Iterable

<? extends

File

> files)

Returns file objects representing the given files.

default

Iterable

<? extends

JavaFileObject

>

getJavaFileObjectsFromPaths

​(

Iterable

<? extends

Path

> paths)

Returns file objects representing the given paths.

Iterable

<? extends

JavaFileObject

>

getJavaFileObjectsFromStrings

​(

Iterable

<

String

> names)

Returns file objects representing the given file names.

Iterable

<? extends

File

>

getLocation

​(

JavaFileManager.Location

location)

Returns the search path associated with the given location.

default

Iterable

<? extends

Path

>

getLocationAsPaths

​(

JavaFileManager.Location

location)

Returns the search path associated with the given location.

boolean

isSameFile

​(

FileObject

a,

FileObject

b)

Compares two file objects and return true if they represent the
same canonical file, zip file entry, or entry in any file
system based container.

void

setLocation

​(

JavaFileManager.Location

location,

Iterable

<? extends

File

> files)

Associates the given search path with the given location.

default void

setLocationForModule

​(

JavaFileManager.Location

location,

String

moduleName,

Collection

<? extends

Path

> paths)

Associates the given search path with the given module and location,
which must be a module-oriented or output location.

default void

setLocationFromPaths

​(

JavaFileManager.Location

location,

Collection

<? extends

Path

> paths)

Associates the given search path with the given location.

default void

setPathFactory

​(

StandardJavaFileManager.PathFactory

f)

Specify a factory that can be used to generate a path from a string, or series of strings.

- Methods declared in interface javax.tools.

JavaFileManager

close

,

contains

,

flush

,

getClassLoader

,

getFileForInput

,

getFileForOutput

,

getJavaFileForInput

,

getJavaFileForOutput

,

getLocationForModule

,

getLocationForModule

,

getServiceLoader

,

handleOption

,

hasLocation

,

inferBinaryName

,

inferModuleName

,

list

,

listLocationsForModules

- Methods declared in interface javax.tools.

OptionChecker

isSupportedOption

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

StandardJavaFileManager.PathFactory

Factory to create

Path

objects from strings.

- Nested classes/interfaces declared in interface javax.tools.

JavaFileManager

JavaFileManager.Location

---

#### Nested Class Summary

Factory to create

Path

objects from strings.

Nested classes/interfaces declared in interface javax.tools.

JavaFileManager

JavaFileManager.Location

---

#### Nested classes/interfaces declared in interface javax.tools. JavaFileManager

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

Path

asPath

​(

FileObject

file)

Returns the path, if any, underlying this file object (optional operation).

Iterable

<? extends

JavaFileObject

>

getJavaFileObjects

​(

File

... files)

Returns file objects representing the given files.

Iterable

<? extends

JavaFileObject

>

getJavaFileObjects

​(

String

... names)

Returns file objects representing the given file names.

default

Iterable

<? extends

JavaFileObject

>

getJavaFileObjects

​(

Path

... paths)

Returns file objects representing the given paths.

Iterable

<? extends

JavaFileObject

>

getJavaFileObjectsFromFiles

​(

Iterable

<? extends

File

> files)

Returns file objects representing the given files.

default

Iterable

<? extends

JavaFileObject

>

getJavaFileObjectsFromPaths

​(

Iterable

<? extends

Path

> paths)

Returns file objects representing the given paths.

Iterable

<? extends

JavaFileObject

>

getJavaFileObjectsFromStrings

​(

Iterable

<

String

> names)

Returns file objects representing the given file names.

Iterable

<? extends

File

>

getLocation

​(

JavaFileManager.Location

location)

Returns the search path associated with the given location.

default

Iterable

<? extends

Path

>

getLocationAsPaths

​(

JavaFileManager.Location

location)

Returns the search path associated with the given location.

boolean

isSameFile

​(

FileObject

a,

FileObject

b)

Compares two file objects and return true if they represent the
same canonical file, zip file entry, or entry in any file
system based container.

void

setLocation

​(

JavaFileManager.Location

location,

Iterable

<? extends

File

> files)

Associates the given search path with the given location.

default void

setLocationForModule

​(

JavaFileManager.Location

location,

String

moduleName,

Collection

<? extends

Path

> paths)

Associates the given search path with the given module and location,
which must be a module-oriented or output location.

default void

setLocationFromPaths

​(

JavaFileManager.Location

location,

Collection

<? extends

Path

> paths)

Associates the given search path with the given location.

default void

setPathFactory

​(

StandardJavaFileManager.PathFactory

f)

Specify a factory that can be used to generate a path from a string, or series of strings.

- Methods declared in interface javax.tools.

JavaFileManager

close

,

contains

,

flush

,

getClassLoader

,

getFileForInput

,

getFileForOutput

,

getJavaFileForInput

,

getJavaFileForOutput

,

getLocationForModule

,

getLocationForModule

,

getServiceLoader

,

handleOption

,

hasLocation

,

inferBinaryName

,

inferModuleName

,

list

,

listLocationsForModules

- Methods declared in interface javax.tools.

OptionChecker

isSupportedOption

---

#### Method Summary

Returns the path, if any, underlying this file object (optional operation).

Returns file objects representing the given files.

Returns file objects representing the given file names.

Returns file objects representing the given paths.

Returns the search path associated with the given location.

Compares two file objects and return true if they represent the
same canonical file, zip file entry, or entry in any file
system based container.

Associates the given search path with the given location.

Associates the given search path with the given module and location,
which must be a module-oriented or output location.

Specify a factory that can be used to generate a path from a string, or series of strings.

Methods declared in interface javax.tools.

JavaFileManager

close

,

contains

,

flush

,

getClassLoader

,

getFileForInput

,

getFileForOutput

,

getJavaFileForInput

,

getJavaFileForOutput

,

getLocationForModule

,

getLocationForModule

,

getServiceLoader

,

handleOption

,

hasLocation

,

inferBinaryName

,

inferModuleName

,

list

,

listLocationsForModules

---

#### Methods declared in interface javax.tools. JavaFileManager

Methods declared in interface javax.tools.

OptionChecker

isSupportedOption

---

#### Methods declared in interface javax.tools. OptionChecker

============ METHOD DETAIL ==========

- Method Detail

- isSameFile

```java
boolean isSameFile​(
FileObject
a,

FileObject
b)
```

Compares two file objects and return true if they represent the
same canonical file, zip file entry, or entry in any file
system based container.

**Specified by:** isSameFile

in interface

JavaFileManager
**Parameters:** a

- a file object
**Parameters:** b

- a file object
**Returns:** true if the given file objects represent the same
canonical file, zip file entry or path; false otherwise
**Throws:** IllegalArgumentException

- if either of the arguments
were created with another file manager implementation

- getJavaFileObjectsFromFiles

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromFiles​(
Iterable
<? extends
File
> files)
```

Returns file objects representing the given files.

**Parameters:** files

- a list of files
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the list of files includes
a directory

- getJavaFileObjectsFromPaths

```java
default
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromPaths​(
Iterable
<? extends
Path
> paths)
```

Returns file objects representing the given paths.

**Implementation Requirements:** The default implementation converts each path to a file and calls

getJavaObjectsFromFiles

.
IllegalArgumentException will be thrown if any of the paths
cannot be converted to a file.
**Parameters:** paths

- a list of paths
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the list of paths includes
a directory or if this file manager does not support any of the
given paths.
**Since:** 9

- getJavaFileObjects

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
File
... files)
```

Returns file objects representing the given files.
Convenience method equivalent to:

```java
getJavaFileObjectsFromFiles(
Arrays.asList
(files))
```

**Parameters:** files

- an array of files
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the array of files includes
a directory
**Throws:** NullPointerException

- if the given array contains null
elements

- getJavaFileObjects

```java
default
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
Path
... paths)
```

Returns file objects representing the given paths.
Convenience method equivalent to:

```java
getJavaFileObjectsFromPaths(
Arrays.asList
(paths))
```

**Parameters:** paths

- an array of paths
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the array of files includes
a directory
**Throws:** NullPointerException

- if the given array contains null
elements
**Since:** 9

- getJavaFileObjectsFromStrings

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromStrings​(
Iterable
<
String
> names)
```

Returns file objects representing the given file names.

**Parameters:** names

- a list of file names
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the list of file names
includes a directory

- getJavaFileObjects

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
String
... names)
```

Returns file objects representing the given file names.
Convenience method equivalent to:

```java
getJavaFileObjectsFromStrings(
Arrays.asList
(names))
```

**Parameters:** names

- a list of file names
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the array of file names
includes a directory
**Throws:** NullPointerException

- if the given array contains null
elements

- setLocation

```java
void setLocation​(
JavaFileManager.Location
location,

Iterable
<? extends
File
> files)
throws
IOException
```

Associates the given search path with the given location. Any
previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

**Parameters:** location

- a location
**Parameters:** files

- a list of files, if

null

use the default
search path for this location
**Throws:** IllegalArgumentException

- if

location

is an output
location and

files

does not contain exactly one element
**Throws:** IOException

- if

location

is an output location and
does not represent an existing directory
**See Also:** getLocation(javax.tools.JavaFileManager.Location)

- setLocationFromPaths

```java
default void setLocationFromPaths​(
JavaFileManager.Location
location,

Collection
<? extends
Path
> paths)
throws
IOException
```

Associates the given search path with the given location.
Any previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

**Implementation Requirements:** The default implementation converts each path to a file and calls

getJavaObjectsFromFiles

.

IllegalArgumentException

will be thrown if any of the paths cannot be converted to a file.
**Parameters:** location

- a location
**Parameters:** paths

- a list of paths, if

null

use the default
search path for this location
**Throws:** IllegalArgumentException

- if

location

is an output
location and

paths

does not contain exactly one element
or if this file manager does not support any of the given paths
**Throws:** IOException

- if

location

is an output location and

paths

does not represent an existing directory
**Since:** 9
**See Also:** getLocation(javax.tools.JavaFileManager.Location)

- setLocationForModule

```java
default void setLocationForModule​(
JavaFileManager.Location
location,

String
moduleName,

Collection
<? extends
Path
> paths)
throws
IOException
```

Associates the given search path with the given module and location,
which must be a module-oriented or output location.
Any previous value will be discarded.
This overrides any default association derived from the search path
associated with the location itself.

All such module-specific associations will be cancelled if a
new search path is associated with the location by calling

setLocation

or

setLocationFromPaths

.

**Parameters:** location

- the location
**Parameters:** moduleName

- the name of the module
**Parameters:** paths

- the search path to associate with the location and module.
**Throws:** IllegalStateException

- if the location is not a module-oriented
or output location.
**Throws:** UnsupportedOperationException

- if this operation is not supported by
this file manager.
**Throws:** IOException

- if

location

is an output location and

paths

does not represent an existing directory
**Since:** 9
**See Also:** setLocation(javax.tools.JavaFileManager.Location,java.lang.Iterable<? extends java.io.File>)

,

setLocationFromPaths(javax.tools.JavaFileManager.Location,java.util.Collection<? extends java.nio.file.Path>)

- getLocation

```java
Iterable
<? extends
File
> getLocation​(
JavaFileManager.Location
location)
```

Returns the search path associated with the given location.

**Parameters:** location

- a location
**Returns:** a list of files or

null

if this location has no
associated search path
**Throws:** IllegalStateException

- if any element of the search path
cannot be converted to a

File

, or if the search path
cannot be represented as a simple series of files.
**See Also:** setLocation(javax.tools.JavaFileManager.Location, java.lang.Iterable<? extends java.io.File>)

,

Path.toFile()

- getLocationAsPaths

```java
default
Iterable
<? extends
Path
> getLocationAsPaths​(
JavaFileManager.Location
location)
```

Returns the search path associated with the given location.

**Implementation Requirements:** The default implementation calls

getLocation

and then returns an

Iterable

formed by calling

toPath()

on each

File

returned from

getLocation

.
**Parameters:** location

- a location
**Returns:** a list of paths or

null

if this location has no
associated search path
**Throws:** IllegalStateException

- if the search path cannot be represented
as a simple series of paths.
**Since:** 9
**See Also:** setLocationFromPaths(javax.tools.JavaFileManager.Location, java.util.Collection<? extends java.nio.file.Path>)

- asPath

```java
default
Path
asPath​(
FileObject
file)
```

Returns the path, if any, underlying this file object (optional operation).
File objects derived from a

FileSystem

,
including the default file system, typically have a corresponding underlying

Path

object. In such cases, this method may be
used to access that object.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

for all files.
**Parameters:** file

- a file object
**Returns:** a path representing the same underlying file system artifact
**Throws:** IllegalArgumentException

- if the file object does not have an underlying path
**Throws:** UnsupportedOperationException

- if the operation is not supported by this file manager
**Since:** 9

- setPathFactory

```java
default void setPathFactory​(
StandardJavaFileManager.PathFactory
f)
```

Specify a factory that can be used to generate a path from a string, or series of strings.

If this method is not called, a factory whose

getPath

method is
equivalent to calling

java.nio.file.Paths.get(first, more)

will be used.

**Implementation Requirements:** The default implementation of this method ignores the factory that is provided.
**Parameters:** f

- the factory
**Since:** 9

Method Detail

- isSameFile

```java
boolean isSameFile​(
FileObject
a,

FileObject
b)
```

Compares two file objects and return true if they represent the
same canonical file, zip file entry, or entry in any file
system based container.

**Specified by:** isSameFile

in interface

JavaFileManager
**Parameters:** a

- a file object
**Parameters:** b

- a file object
**Returns:** true if the given file objects represent the same
canonical file, zip file entry or path; false otherwise
**Throws:** IllegalArgumentException

- if either of the arguments
were created with another file manager implementation

- getJavaFileObjectsFromFiles

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromFiles​(
Iterable
<? extends
File
> files)
```

Returns file objects representing the given files.

**Parameters:** files

- a list of files
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the list of files includes
a directory

- getJavaFileObjectsFromPaths

```java
default
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromPaths​(
Iterable
<? extends
Path
> paths)
```

Returns file objects representing the given paths.

**Implementation Requirements:** The default implementation converts each path to a file and calls

getJavaObjectsFromFiles

.
IllegalArgumentException will be thrown if any of the paths
cannot be converted to a file.
**Parameters:** paths

- a list of paths
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the list of paths includes
a directory or if this file manager does not support any of the
given paths.
**Since:** 9

- getJavaFileObjects

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
File
... files)
```

Returns file objects representing the given files.
Convenience method equivalent to:

```java
getJavaFileObjectsFromFiles(
Arrays.asList
(files))
```

**Parameters:** files

- an array of files
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the array of files includes
a directory
**Throws:** NullPointerException

- if the given array contains null
elements

- getJavaFileObjects

```java
default
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
Path
... paths)
```

Returns file objects representing the given paths.
Convenience method equivalent to:

```java
getJavaFileObjectsFromPaths(
Arrays.asList
(paths))
```

**Parameters:** paths

- an array of paths
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the array of files includes
a directory
**Throws:** NullPointerException

- if the given array contains null
elements
**Since:** 9

- getJavaFileObjectsFromStrings

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromStrings​(
Iterable
<
String
> names)
```

Returns file objects representing the given file names.

**Parameters:** names

- a list of file names
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the list of file names
includes a directory

- getJavaFileObjects

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
String
... names)
```

Returns file objects representing the given file names.
Convenience method equivalent to:

```java
getJavaFileObjectsFromStrings(
Arrays.asList
(names))
```

**Parameters:** names

- a list of file names
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the array of file names
includes a directory
**Throws:** NullPointerException

- if the given array contains null
elements

- setLocation

```java
void setLocation​(
JavaFileManager.Location
location,

Iterable
<? extends
File
> files)
throws
IOException
```

Associates the given search path with the given location. Any
previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

**Parameters:** location

- a location
**Parameters:** files

- a list of files, if

null

use the default
search path for this location
**Throws:** IllegalArgumentException

- if

location

is an output
location and

files

does not contain exactly one element
**Throws:** IOException

- if

location

is an output location and
does not represent an existing directory
**See Also:** getLocation(javax.tools.JavaFileManager.Location)

- setLocationFromPaths

```java
default void setLocationFromPaths​(
JavaFileManager.Location
location,

Collection
<? extends
Path
> paths)
throws
IOException
```

Associates the given search path with the given location.
Any previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

**Implementation Requirements:** The default implementation converts each path to a file and calls

getJavaObjectsFromFiles

.

IllegalArgumentException

will be thrown if any of the paths cannot be converted to a file.
**Parameters:** location

- a location
**Parameters:** paths

- a list of paths, if

null

use the default
search path for this location
**Throws:** IllegalArgumentException

- if

location

is an output
location and

paths

does not contain exactly one element
or if this file manager does not support any of the given paths
**Throws:** IOException

- if

location

is an output location and

paths

does not represent an existing directory
**Since:** 9
**See Also:** getLocation(javax.tools.JavaFileManager.Location)

- setLocationForModule

```java
default void setLocationForModule​(
JavaFileManager.Location
location,

String
moduleName,

Collection
<? extends
Path
> paths)
throws
IOException
```

Associates the given search path with the given module and location,
which must be a module-oriented or output location.
Any previous value will be discarded.
This overrides any default association derived from the search path
associated with the location itself.

All such module-specific associations will be cancelled if a
new search path is associated with the location by calling

setLocation

or

setLocationFromPaths

.

**Parameters:** location

- the location
**Parameters:** moduleName

- the name of the module
**Parameters:** paths

- the search path to associate with the location and module.
**Throws:** IllegalStateException

- if the location is not a module-oriented
or output location.
**Throws:** UnsupportedOperationException

- if this operation is not supported by
this file manager.
**Throws:** IOException

- if

location

is an output location and

paths

does not represent an existing directory
**Since:** 9
**See Also:** setLocation(javax.tools.JavaFileManager.Location,java.lang.Iterable<? extends java.io.File>)

,

setLocationFromPaths(javax.tools.JavaFileManager.Location,java.util.Collection<? extends java.nio.file.Path>)

- getLocation

```java
Iterable
<? extends
File
> getLocation​(
JavaFileManager.Location
location)
```

Returns the search path associated with the given location.

**Parameters:** location

- a location
**Returns:** a list of files or

null

if this location has no
associated search path
**Throws:** IllegalStateException

- if any element of the search path
cannot be converted to a

File

, or if the search path
cannot be represented as a simple series of files.
**See Also:** setLocation(javax.tools.JavaFileManager.Location, java.lang.Iterable<? extends java.io.File>)

,

Path.toFile()

- getLocationAsPaths

```java
default
Iterable
<? extends
Path
> getLocationAsPaths​(
JavaFileManager.Location
location)
```

Returns the search path associated with the given location.

**Implementation Requirements:** The default implementation calls

getLocation

and then returns an

Iterable

formed by calling

toPath()

on each

File

returned from

getLocation

.
**Parameters:** location

- a location
**Returns:** a list of paths or

null

if this location has no
associated search path
**Throws:** IllegalStateException

- if the search path cannot be represented
as a simple series of paths.
**Since:** 9
**See Also:** setLocationFromPaths(javax.tools.JavaFileManager.Location, java.util.Collection<? extends java.nio.file.Path>)

- asPath

```java
default
Path
asPath​(
FileObject
file)
```

Returns the path, if any, underlying this file object (optional operation).
File objects derived from a

FileSystem

,
including the default file system, typically have a corresponding underlying

Path

object. In such cases, this method may be
used to access that object.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

for all files.
**Parameters:** file

- a file object
**Returns:** a path representing the same underlying file system artifact
**Throws:** IllegalArgumentException

- if the file object does not have an underlying path
**Throws:** UnsupportedOperationException

- if the operation is not supported by this file manager
**Since:** 9

- setPathFactory

```java
default void setPathFactory​(
StandardJavaFileManager.PathFactory
f)
```

Specify a factory that can be used to generate a path from a string, or series of strings.

If this method is not called, a factory whose

getPath

method is
equivalent to calling

java.nio.file.Paths.get(first, more)

will be used.

**Implementation Requirements:** The default implementation of this method ignores the factory that is provided.
**Parameters:** f

- the factory
**Since:** 9

---

#### Method Detail

isSameFile

```java
boolean isSameFile​(
FileObject
a,

FileObject
b)
```

Compares two file objects and return true if they represent the
same canonical file, zip file entry, or entry in any file
system based container.

**Specified by:** isSameFile

in interface

JavaFileManager
**Parameters:** a

- a file object
**Parameters:** b

- a file object
**Returns:** true if the given file objects represent the same
canonical file, zip file entry or path; false otherwise
**Throws:** IllegalArgumentException

- if either of the arguments
were created with another file manager implementation

---

#### isSameFile

boolean isSameFile​(

FileObject

a,

FileObject

b)

Compares two file objects and return true if they represent the
same canonical file, zip file entry, or entry in any file
system based container.

getJavaFileObjectsFromFiles

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromFiles​(
Iterable
<? extends
File
> files)
```

Returns file objects representing the given files.

**Parameters:** files

- a list of files
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the list of files includes
a directory

---

#### getJavaFileObjectsFromFiles

Iterable

<? extends

JavaFileObject

> getJavaFileObjectsFromFiles​(

Iterable

<? extends

File

> files)

Returns file objects representing the given files.

getJavaFileObjectsFromPaths

```java
default
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromPaths​(
Iterable
<? extends
Path
> paths)
```

Returns file objects representing the given paths.

**Implementation Requirements:** The default implementation converts each path to a file and calls

getJavaObjectsFromFiles

.
IllegalArgumentException will be thrown if any of the paths
cannot be converted to a file.
**Parameters:** paths

- a list of paths
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the list of paths includes
a directory or if this file manager does not support any of the
given paths.
**Since:** 9

---

#### getJavaFileObjectsFromPaths

default

Iterable

<? extends

JavaFileObject

> getJavaFileObjectsFromPaths​(

Iterable

<? extends

Path

> paths)

Returns file objects representing the given paths.

getJavaFileObjects

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
File
... files)
```

Returns file objects representing the given files.
Convenience method equivalent to:

```java
getJavaFileObjectsFromFiles(
Arrays.asList
(files))
```

**Parameters:** files

- an array of files
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the array of files includes
a directory
**Throws:** NullPointerException

- if the given array contains null
elements

---

#### getJavaFileObjects

Iterable

<? extends

JavaFileObject

> getJavaFileObjects​(

File

... files)

Returns file objects representing the given files.
Convenience method equivalent to:

```java
getJavaFileObjectsFromFiles(
Arrays.asList
(files))
```

getJavaFileObjectsFromFiles(

Arrays.asList

(files))

getJavaFileObjects

```java
default
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
Path
... paths)
```

Returns file objects representing the given paths.
Convenience method equivalent to:

```java
getJavaFileObjectsFromPaths(
Arrays.asList
(paths))
```

**Parameters:** paths

- an array of paths
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the array of files includes
a directory
**Throws:** NullPointerException

- if the given array contains null
elements
**Since:** 9

---

#### getJavaFileObjects

default

Iterable

<? extends

JavaFileObject

> getJavaFileObjects​(

Path

... paths)

Returns file objects representing the given paths.
Convenience method equivalent to:

```java
getJavaFileObjectsFromPaths(
Arrays.asList
(paths))
```

getJavaFileObjectsFromPaths(

Arrays.asList

(paths))

getJavaFileObjectsFromStrings

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjectsFromStrings​(
Iterable
<
String
> names)
```

Returns file objects representing the given file names.

**Parameters:** names

- a list of file names
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the list of file names
includes a directory

---

#### getJavaFileObjectsFromStrings

Iterable

<? extends

JavaFileObject

> getJavaFileObjectsFromStrings​(

Iterable

<

String

> names)

Returns file objects representing the given file names.

getJavaFileObjects

```java
Iterable
<? extends
JavaFileObject
> getJavaFileObjects​(
String
... names)
```

Returns file objects representing the given file names.
Convenience method equivalent to:

```java
getJavaFileObjectsFromStrings(
Arrays.asList
(names))
```

**Parameters:** names

- a list of file names
**Returns:** a list of file objects
**Throws:** IllegalArgumentException

- if the array of file names
includes a directory
**Throws:** NullPointerException

- if the given array contains null
elements

---

#### getJavaFileObjects

Iterable

<? extends

JavaFileObject

> getJavaFileObjects​(

String

... names)

Returns file objects representing the given file names.
Convenience method equivalent to:

```java
getJavaFileObjectsFromStrings(
Arrays.asList
(names))
```

getJavaFileObjectsFromStrings(

Arrays.asList

(names))

setLocation

```java
void setLocation​(
JavaFileManager.Location
location,

Iterable
<? extends
File
> files)
throws
IOException
```

Associates the given search path with the given location. Any
previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

**Parameters:** location

- a location
**Parameters:** files

- a list of files, if

null

use the default
search path for this location
**Throws:** IllegalArgumentException

- if

location

is an output
location and

files

does not contain exactly one element
**Throws:** IOException

- if

location

is an output location and
does not represent an existing directory
**See Also:** getLocation(javax.tools.JavaFileManager.Location)

---

#### setLocation

void setLocation​(

JavaFileManager.Location

location,

Iterable

<? extends

File

> files)
throws

IOException

Associates the given search path with the given location. Any
previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

setLocationFromPaths

```java
default void setLocationFromPaths​(
JavaFileManager.Location
location,

Collection
<? extends
Path
> paths)
throws
IOException
```

Associates the given search path with the given location.
Any previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

**Implementation Requirements:** The default implementation converts each path to a file and calls

getJavaObjectsFromFiles

.

IllegalArgumentException

will be thrown if any of the paths cannot be converted to a file.
**Parameters:** location

- a location
**Parameters:** paths

- a list of paths, if

null

use the default
search path for this location
**Throws:** IllegalArgumentException

- if

location

is an output
location and

paths

does not contain exactly one element
or if this file manager does not support any of the given paths
**Throws:** IOException

- if

location

is an output location and

paths

does not represent an existing directory
**Since:** 9
**See Also:** getLocation(javax.tools.JavaFileManager.Location)

---

#### setLocationFromPaths

default void setLocationFromPaths​(

JavaFileManager.Location

location,

Collection

<? extends

Path

> paths)
throws

IOException

Associates the given search path with the given location.
Any previous value will be discarded.

If the location is a module-oriented or output location, any module-specific
associations set up by

setLocationForModule

will be cancelled.

setLocationForModule

```java
default void setLocationForModule​(
JavaFileManager.Location
location,

String
moduleName,

Collection
<? extends
Path
> paths)
throws
IOException
```

Associates the given search path with the given module and location,
which must be a module-oriented or output location.
Any previous value will be discarded.
This overrides any default association derived from the search path
associated with the location itself.

All such module-specific associations will be cancelled if a
new search path is associated with the location by calling

setLocation

or

setLocationFromPaths

.

**Parameters:** location

- the location
**Parameters:** moduleName

- the name of the module
**Parameters:** paths

- the search path to associate with the location and module.
**Throws:** IllegalStateException

- if the location is not a module-oriented
or output location.
**Throws:** UnsupportedOperationException

- if this operation is not supported by
this file manager.
**Throws:** IOException

- if

location

is an output location and

paths

does not represent an existing directory
**Since:** 9
**See Also:** setLocation(javax.tools.JavaFileManager.Location,java.lang.Iterable<? extends java.io.File>)

,

setLocationFromPaths(javax.tools.JavaFileManager.Location,java.util.Collection<? extends java.nio.file.Path>)

---

#### setLocationForModule

default void setLocationForModule​(

JavaFileManager.Location

location,

String

moduleName,

Collection

<? extends

Path

> paths)
throws

IOException

Associates the given search path with the given module and location,
which must be a module-oriented or output location.
Any previous value will be discarded.
This overrides any default association derived from the search path
associated with the location itself.

All such module-specific associations will be cancelled if a
new search path is associated with the location by calling

setLocation

or

setLocationFromPaths

.

getLocation

```java
Iterable
<? extends
File
> getLocation​(
JavaFileManager.Location
location)
```

Returns the search path associated with the given location.

**Parameters:** location

- a location
**Returns:** a list of files or

null

if this location has no
associated search path
**Throws:** IllegalStateException

- if any element of the search path
cannot be converted to a

File

, or if the search path
cannot be represented as a simple series of files.
**See Also:** setLocation(javax.tools.JavaFileManager.Location, java.lang.Iterable<? extends java.io.File>)

,

Path.toFile()

---

#### getLocation

Iterable

<? extends

File

> getLocation​(

JavaFileManager.Location

location)

Returns the search path associated with the given location.

getLocationAsPaths

```java
default
Iterable
<? extends
Path
> getLocationAsPaths​(
JavaFileManager.Location
location)
```

Returns the search path associated with the given location.

**Implementation Requirements:** The default implementation calls

getLocation

and then returns an

Iterable

formed by calling

toPath()

on each

File

returned from

getLocation

.
**Parameters:** location

- a location
**Returns:** a list of paths or

null

if this location has no
associated search path
**Throws:** IllegalStateException

- if the search path cannot be represented
as a simple series of paths.
**Since:** 9
**See Also:** setLocationFromPaths(javax.tools.JavaFileManager.Location, java.util.Collection<? extends java.nio.file.Path>)

---

#### getLocationAsPaths

default

Iterable

<? extends

Path

> getLocationAsPaths​(

JavaFileManager.Location

location)

Returns the search path associated with the given location.

asPath

```java
default
Path
asPath​(
FileObject
file)
```

Returns the path, if any, underlying this file object (optional operation).
File objects derived from a

FileSystem

,
including the default file system, typically have a corresponding underlying

Path

object. In such cases, this method may be
used to access that object.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

for all files.
**Parameters:** file

- a file object
**Returns:** a path representing the same underlying file system artifact
**Throws:** IllegalArgumentException

- if the file object does not have an underlying path
**Throws:** UnsupportedOperationException

- if the operation is not supported by this file manager
**Since:** 9

---

#### asPath

default

Path

asPath​(

FileObject

file)

Returns the path, if any, underlying this file object (optional operation).
File objects derived from a

FileSystem

,
including the default file system, typically have a corresponding underlying

Path

object. In such cases, this method may be
used to access that object.

setPathFactory

```java
default void setPathFactory​(
StandardJavaFileManager.PathFactory
f)
```

Specify a factory that can be used to generate a path from a string, or series of strings.

If this method is not called, a factory whose

getPath

method is
equivalent to calling

java.nio.file.Paths.get(first, more)

will be used.

**Implementation Requirements:** The default implementation of this method ignores the factory that is provided.
**Parameters:** f

- the factory
**Since:** 9

---

#### setPathFactory

default void setPathFactory​(

StandardJavaFileManager.PathFactory

f)

Specify a factory that can be used to generate a path from a string, or series of strings.

If this method is not called, a factory whose

getPath

method is
equivalent to calling

java.nio.file.Paths.get(first, more)

will be used.

---

