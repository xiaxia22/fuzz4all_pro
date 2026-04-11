# Interface JavaFileManager.Location

**Source:** `java.compiler\javax\tools\JavaFileManager.Location.html`

### Class Description

```java
public static interface
JavaFileManager.Location
```

Interface for locations of file objects. Used by file managers
to determine where to place or search for file objects.

Informally, a

Location

corresponds to a "search path", such as a class
path or module path, as used by command-line tools that use the default file system.

Some locations are typically used to identify a place in which
a tool can find files to be read; others are typically used to identify
a place where a tool can write files. If a location is used to identify
a place for reading files, those files may be organized in a simple

package/class

hierarchy: such locations are described as

package-oriented

.
Alternatively, the files may be organized in a

module/package/class

hierarchy: such locations are described as

module-oriented

.
If a location is typically used to identify a place where a tool can write files,
it is up to the tool that writes the files to specify how those files will be
organized.

You can access the classes in a package-oriented location using methods like

JavaFileManager.getJavaFileForInput(javax.tools.JavaFileManager.Location, java.lang.String, javax.tools.JavaFileObject.Kind)

or

JavaFileManager.list(javax.tools.JavaFileManager.Location, java.lang.String, java.util.Set<javax.tools.JavaFileObject.Kind>, boolean)

.
It is not possible to directly list the classes in a module-oriented
location. Instead, you can get a package-oriented location for any specific module
using methods like

JavaFileManager.getLocationForModule(javax.tools.JavaFileManager.Location, java.lang.String)

or

JavaFileManager.listLocationsForModules(javax.tools.JavaFileManager.Location)

.

**All Known Implementing Classes:** DocumentationTool.Location

,

StandardLocation

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the name of this location.

**Returns:**
- a name

---

#### boolean isOutputLocation()

Determines if this is an output location.
An output location is a location that is conventionally used for
output.

**Returns:**
- true if this is an output location, false otherwise

**API Note:**
- An output location may be used to write files in either
a package-oriented organization or in a module-oriented organization.

---

#### default boolean isModuleOrientedLocation()

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.
The result of this method is undefined if this is an output
location.

**Returns:**
- true if this location is expected to contain modules

**Since:**
- 9

**Implementation Note:**
- This implementation returns true if the name includes
the word "MODULE".

---

### Additional Sections

#### Interface JavaFileManager.Location

**All Known Implementing Classes:** DocumentationTool.Location

,

StandardLocation

**Enclosing interface:** JavaFileManager

```java
public static interface
JavaFileManager.Location
```

Interface for locations of file objects. Used by file managers
to determine where to place or search for file objects.

Informally, a

Location

corresponds to a "search path", such as a class
path or module path, as used by command-line tools that use the default file system.

Some locations are typically used to identify a place in which
a tool can find files to be read; others are typically used to identify
a place where a tool can write files. If a location is used to identify
a place for reading files, those files may be organized in a simple

package/class

hierarchy: such locations are described as

package-oriented

.
Alternatively, the files may be organized in a

module/package/class

hierarchy: such locations are described as

module-oriented

.
If a location is typically used to identify a place where a tool can write files,
it is up to the tool that writes the files to specify how those files will be
organized.

You can access the classes in a package-oriented location using methods like

JavaFileManager.getJavaFileForInput(javax.tools.JavaFileManager.Location, java.lang.String, javax.tools.JavaFileObject.Kind)

or

JavaFileManager.list(javax.tools.JavaFileManager.Location, java.lang.String, java.util.Set<javax.tools.JavaFileObject.Kind>, boolean)

.
It is not possible to directly list the classes in a module-oriented
location. Instead, you can get a package-oriented location for any specific module
using methods like

JavaFileManager.getLocationForModule(javax.tools.JavaFileManager.Location, java.lang.String)

or

JavaFileManager.listLocationsForModules(javax.tools.JavaFileManager.Location)

.

public static interface

JavaFileManager.Location

Interface for locations of file objects. Used by file managers
to determine where to place or search for file objects.

Informally, a

Location

corresponds to a "search path", such as a class
path or module path, as used by command-line tools that use the default file system.

Some locations are typically used to identify a place in which
a tool can find files to be read; others are typically used to identify
a place where a tool can write files. If a location is used to identify
a place for reading files, those files may be organized in a simple

package/class

hierarchy: such locations are described as

package-oriented

.
Alternatively, the files may be organized in a

module/package/class

hierarchy: such locations are described as

module-oriented

.
If a location is typically used to identify a place where a tool can write files,
it is up to the tool that writes the files to specify how those files will be
organized.

You can access the classes in a package-oriented location using methods like

JavaFileManager.getJavaFileForInput(javax.tools.JavaFileManager.Location, java.lang.String, javax.tools.JavaFileObject.Kind)

or

JavaFileManager.list(javax.tools.JavaFileManager.Location, java.lang.String, java.util.Set<javax.tools.JavaFileObject.Kind>, boolean)

.
It is not possible to directly list the classes in a module-oriented
location. Instead, you can get a package-oriented location for any specific module
using methods like

JavaFileManager.getLocationForModule(javax.tools.JavaFileManager.Location, java.lang.String)

or

JavaFileManager.listLocationsForModules(javax.tools.JavaFileManager.Location)

.

Informally, a

Location

corresponds to a "search path", such as a class
path or module path, as used by command-line tools that use the default file system.

Some locations are typically used to identify a place in which
a tool can find files to be read; others are typically used to identify
a place where a tool can write files. If a location is used to identify
a place for reading files, those files may be organized in a simple

package/class

hierarchy: such locations are described as

package-oriented

.
Alternatively, the files may be organized in a

module/package/class

hierarchy: such locations are described as

module-oriented

.
If a location is typically used to identify a place where a tool can write files,
it is up to the tool that writes the files to specify how those files will be
organized.

You can access the classes in a package-oriented location using methods like

JavaFileManager.getJavaFileForInput(javax.tools.JavaFileManager.Location, java.lang.String, javax.tools.JavaFileObject.Kind)

or

JavaFileManager.list(javax.tools.JavaFileManager.Location, java.lang.String, java.util.Set<javax.tools.JavaFileObject.Kind>, boolean)

.
It is not possible to directly list the classes in a module-oriented
location. Instead, you can get a package-oriented location for any specific module
using methods like

JavaFileManager.getLocationForModule(javax.tools.JavaFileManager.Location, java.lang.String)

or

JavaFileManager.listLocationsForModules(javax.tools.JavaFileManager.Location)

.

Some locations are typically used to identify a place in which
a tool can find files to be read; others are typically used to identify
a place where a tool can write files. If a location is used to identify
a place for reading files, those files may be organized in a simple

package/class

hierarchy: such locations are described as

package-oriented

.
Alternatively, the files may be organized in a

module/package/class

hierarchy: such locations are described as

module-oriented

.
If a location is typically used to identify a place where a tool can write files,
it is up to the tool that writes the files to specify how those files will be
organized.

You can access the classes in a package-oriented location using methods like

JavaFileManager.getJavaFileForInput(javax.tools.JavaFileManager.Location, java.lang.String, javax.tools.JavaFileObject.Kind)

or

JavaFileManager.list(javax.tools.JavaFileManager.Location, java.lang.String, java.util.Set<javax.tools.JavaFileObject.Kind>, boolean)

.
It is not possible to directly list the classes in a module-oriented
location. Instead, you can get a package-oriented location for any specific module
using methods like

JavaFileManager.getLocationForModule(javax.tools.JavaFileManager.Location, java.lang.String)

or

JavaFileManager.listLocationsForModules(javax.tools.JavaFileManager.Location)

.

You can access the classes in a package-oriented location using methods like

JavaFileManager.getJavaFileForInput(javax.tools.JavaFileManager.Location, java.lang.String, javax.tools.JavaFileObject.Kind)

or

JavaFileManager.list(javax.tools.JavaFileManager.Location, java.lang.String, java.util.Set<javax.tools.JavaFileObject.Kind>, boolean)

.
It is not possible to directly list the classes in a module-oriented
location. Instead, you can get a package-oriented location for any specific module
using methods like

JavaFileManager.getLocationForModule(javax.tools.JavaFileManager.Location, java.lang.String)

or

JavaFileManager.listLocationsForModules(javax.tools.JavaFileManager.Location)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of this location.

default boolean

isModuleOrientedLocation

()

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.

boolean

isOutputLocation

()

Determines if this is an output location.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of this location.

default boolean

isModuleOrientedLocation

()

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.

boolean

isOutputLocation

()

Determines if this is an output location.

---

#### Method Summary

Returns the name of this location.

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.

Determines if this is an output location.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Returns the name of this location.

**Returns:** a name

- isOutputLocation

```java
boolean isOutputLocation()
```

Determines if this is an output location.
An output location is a location that is conventionally used for
output.

**API Note:** An output location may be used to write files in either
a package-oriented organization or in a module-oriented organization.
**Returns:** true if this is an output location, false otherwise

- isModuleOrientedLocation

```java
default boolean isModuleOrientedLocation()
```

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.
The result of this method is undefined if this is an output
location.

**Implementation Note:** This implementation returns true if the name includes
the word "MODULE".
**Returns:** true if this location is expected to contain modules
**Since:** 9

Method Detail

- getName

```java
String
getName()
```

Returns the name of this location.

**Returns:** a name

- isOutputLocation

```java
boolean isOutputLocation()
```

Determines if this is an output location.
An output location is a location that is conventionally used for
output.

**API Note:** An output location may be used to write files in either
a package-oriented organization or in a module-oriented organization.
**Returns:** true if this is an output location, false otherwise

- isModuleOrientedLocation

```java
default boolean isModuleOrientedLocation()
```

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.
The result of this method is undefined if this is an output
location.

**Implementation Note:** This implementation returns true if the name includes
the word "MODULE".
**Returns:** true if this location is expected to contain modules
**Since:** 9

---

#### Method Detail

getName

```java
String
getName()
```

Returns the name of this location.

**Returns:** a name

---

#### getName

String

getName()

Returns the name of this location.

isOutputLocation

```java
boolean isOutputLocation()
```

Determines if this is an output location.
An output location is a location that is conventionally used for
output.

**API Note:** An output location may be used to write files in either
a package-oriented organization or in a module-oriented organization.
**Returns:** true if this is an output location, false otherwise

---

#### isOutputLocation

boolean isOutputLocation()

Determines if this is an output location.
An output location is a location that is conventionally used for
output.

isModuleOrientedLocation

```java
default boolean isModuleOrientedLocation()
```

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.
The result of this method is undefined if this is an output
location.

**Implementation Note:** This implementation returns true if the name includes
the word "MODULE".
**Returns:** true if this location is expected to contain modules
**Since:** 9

---

#### isModuleOrientedLocation

default boolean isModuleOrientedLocation()

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.
The result of this method is undefined if this is an output
location.

---

