# Enum StandardLocation

**Source:** `java.compiler\javax\tools\StandardLocation.html`

### Class Description

```java
public enum
StandardLocation

extends
Enum
<
StandardLocation
>
implements
JavaFileManager.Location
```

Standard locations of file objects.

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardLocation

>

,

JavaFileManager.Location

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
StandardLocation
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardLocation c : StandardLocation.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
StandardLocation
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

#### public static
JavaFileManager.Location
locationFor​(
String
name)

Returns a location object with the given name. The following
property must hold:

locationFor(x) ==
locationFor(y)

if and only if

x.equals(y)

.
The returned location will be an output location if and only if
name ends with

"_OUTPUT"

. It will be considered to
be a module-oriented location if the name contains the word

"MODULE"

.

**Parameters:**
- name

- a name

**Returns:**
- a location

---

#### public boolean isModuleOrientedLocation()

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.
The result of this method is undefined if this is an output
location.

**Specified by:**
- isModuleOrientedLocation

in interface

JavaFileManager.Location

**Returns:**
- true if this location is expected to contain modules

**Since:**
- 9

---

### Additional Sections

#### Enum StandardLocation

java.lang.Object

- java.lang.Enum

<

StandardLocation

>
- - javax.tools.StandardLocation

java.lang.Enum

<

StandardLocation

>

- javax.tools.StandardLocation

javax.tools.StandardLocation

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardLocation

>

,

JavaFileManager.Location

```java
public enum
StandardLocation

extends
Enum
<
StandardLocation
>
implements
JavaFileManager.Location
```

Standard locations of file objects.

**Since:** 1.6

public enum

StandardLocation

extends

Enum

<

StandardLocation

>
implements

JavaFileManager.Location

Standard locations of file objects.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ANNOTATION_PROCESSOR_MODULE_PATH

Location to search for modules containing annotation processors.

ANNOTATION_PROCESSOR_PATH

Location to search for annotation processors.

CLASS_OUTPUT

Location of new class files.

CLASS_PATH

Location to search for user class files.

MODULE_PATH

Location to search for precompiled user modules.

MODULE_SOURCE_PATH

Location to search for the source code of modules.

NATIVE_HEADER_OUTPUT

Location of new native header files.

PATCH_MODULE_PATH

Location to search for module patches.

PLATFORM_CLASS_PATH

Location to search for platform classes.

SOURCE_OUTPUT

Location of new source files.

SOURCE_PATH

Location to search for existing source files.

SYSTEM_MODULES

Location to search for system modules.

UPGRADE_MODULE_PATH

Location to search for upgradeable system modules.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isModuleOrientedLocation

()

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.

static

JavaFileManager.Location

locationFor

​(

String

name)

Returns a location object with the given name.

static

StandardLocation

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardLocation

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

- Methods declared in interface javax.tools.

JavaFileManager.Location

getName

,

isOutputLocation

Enum Constant Summary

Enum Constants

Enum Constant

Description

ANNOTATION_PROCESSOR_MODULE_PATH

Location to search for modules containing annotation processors.

ANNOTATION_PROCESSOR_PATH

Location to search for annotation processors.

CLASS_OUTPUT

Location of new class files.

CLASS_PATH

Location to search for user class files.

MODULE_PATH

Location to search for precompiled user modules.

MODULE_SOURCE_PATH

Location to search for the source code of modules.

NATIVE_HEADER_OUTPUT

Location of new native header files.

PATCH_MODULE_PATH

Location to search for module patches.

PLATFORM_CLASS_PATH

Location to search for platform classes.

SOURCE_OUTPUT

Location of new source files.

SOURCE_PATH

Location to search for existing source files.

SYSTEM_MODULES

Location to search for system modules.

UPGRADE_MODULE_PATH

Location to search for upgradeable system modules.

---

#### Enum Constant Summary

Location to search for modules containing annotation processors.

Location to search for annotation processors.

Location of new class files.

Location to search for user class files.

Location to search for precompiled user modules.

Location to search for the source code of modules.

Location of new native header files.

Location to search for module patches.

Location to search for platform classes.

Location of new source files.

Location to search for existing source files.

Location to search for system modules.

Location to search for upgradeable system modules.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isModuleOrientedLocation

()

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.

static

JavaFileManager.Location

locationFor

​(

String

name)

Returns a location object with the given name.

static

StandardLocation

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardLocation

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

- Methods declared in interface javax.tools.

JavaFileManager.Location

getName

,

isOutputLocation

---

#### Method Summary

Indicates if this location is module-oriented location, and therefore
expected to contain classes in a

module/package/class

hierarchy, as compared to a package-oriented location, which
is expected to contain classes in a

package/class

hierarchy.

Returns a location object with the given name.

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

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

Methods declared in interface javax.tools.

JavaFileManager.Location

getName

,

isOutputLocation

---

#### Methods declared in interface javax.tools. JavaFileManager.Location

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- CLASS_OUTPUT

```java
public static final
StandardLocation
CLASS_OUTPUT
```

Location of new class files.

- SOURCE_OUTPUT

```java
public static final
StandardLocation
SOURCE_OUTPUT
```

Location of new source files.

- CLASS_PATH

```java
public static final
StandardLocation
CLASS_PATH
```

Location to search for user class files.

- SOURCE_PATH

```java
public static final
StandardLocation
SOURCE_PATH
```

Location to search for existing source files.

- ANNOTATION_PROCESSOR_PATH

```java
public static final
StandardLocation
ANNOTATION_PROCESSOR_PATH
```

Location to search for annotation processors.

- ANNOTATION_PROCESSOR_MODULE_PATH

```java
public static final
StandardLocation
ANNOTATION_PROCESSOR_MODULE_PATH
```

Location to search for modules containing annotation processors.

**Since:** 9

- PLATFORM_CLASS_PATH

```java
public static final
StandardLocation
PLATFORM_CLASS_PATH
```

Location to search for platform classes. Sometimes called
the boot class path.

- NATIVE_HEADER_OUTPUT

```java
public static final
StandardLocation
NATIVE_HEADER_OUTPUT
```

Location of new native header files.

**Since:** 1.8

- MODULE_SOURCE_PATH

```java
public static final
StandardLocation
MODULE_SOURCE_PATH
```

Location to search for the source code of modules.

**Since:** 9

- UPGRADE_MODULE_PATH

```java
public static final
StandardLocation
UPGRADE_MODULE_PATH
```

Location to search for upgradeable system modules.

**Since:** 9

- SYSTEM_MODULES

```java
public static final
StandardLocation
SYSTEM_MODULES
```

Location to search for system modules.

**Since:** 9

- MODULE_PATH

```java
public static final
StandardLocation
MODULE_PATH
```

Location to search for precompiled user modules.

**Since:** 9

- PATCH_MODULE_PATH

```java
public static final
StandardLocation
PATCH_MODULE_PATH
```

Location to search for module patches.

**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
StandardLocation
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardLocation c : StandardLocation.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardLocation
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- locationFor

```java
public static
JavaFileManager.Location
locationFor​(
String
name)
```

Returns a location object with the given name. The following
property must hold:

locationFor(x) ==
locationFor(y)

if and only if

x.equals(y)

.
The returned location will be an output location if and only if
name ends with

"_OUTPUT"

. It will be considered to
be a module-oriented location if the name contains the word

"MODULE"

.

**Parameters:** name

- a name
**Returns:** a location

- isModuleOrientedLocation

```java
public boolean isModuleOrientedLocation()
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

**Specified by:** isModuleOrientedLocation

in interface

JavaFileManager.Location
**Returns:** true if this location is expected to contain modules
**Since:** 9

Enum Constant Detail

- CLASS_OUTPUT

```java
public static final
StandardLocation
CLASS_OUTPUT
```

Location of new class files.

- SOURCE_OUTPUT

```java
public static final
StandardLocation
SOURCE_OUTPUT
```

Location of new source files.

- CLASS_PATH

```java
public static final
StandardLocation
CLASS_PATH
```

Location to search for user class files.

- SOURCE_PATH

```java
public static final
StandardLocation
SOURCE_PATH
```

Location to search for existing source files.

- ANNOTATION_PROCESSOR_PATH

```java
public static final
StandardLocation
ANNOTATION_PROCESSOR_PATH
```

Location to search for annotation processors.

- ANNOTATION_PROCESSOR_MODULE_PATH

```java
public static final
StandardLocation
ANNOTATION_PROCESSOR_MODULE_PATH
```

Location to search for modules containing annotation processors.

**Since:** 9

- PLATFORM_CLASS_PATH

```java
public static final
StandardLocation
PLATFORM_CLASS_PATH
```

Location to search for platform classes. Sometimes called
the boot class path.

- NATIVE_HEADER_OUTPUT

```java
public static final
StandardLocation
NATIVE_HEADER_OUTPUT
```

Location of new native header files.

**Since:** 1.8

- MODULE_SOURCE_PATH

```java
public static final
StandardLocation
MODULE_SOURCE_PATH
```

Location to search for the source code of modules.

**Since:** 9

- UPGRADE_MODULE_PATH

```java
public static final
StandardLocation
UPGRADE_MODULE_PATH
```

Location to search for upgradeable system modules.

**Since:** 9

- SYSTEM_MODULES

```java
public static final
StandardLocation
SYSTEM_MODULES
```

Location to search for system modules.

**Since:** 9

- MODULE_PATH

```java
public static final
StandardLocation
MODULE_PATH
```

Location to search for precompiled user modules.

**Since:** 9

- PATCH_MODULE_PATH

```java
public static final
StandardLocation
PATCH_MODULE_PATH
```

Location to search for module patches.

**Since:** 9

---

#### Enum Constant Detail

CLASS_OUTPUT

```java
public static final
StandardLocation
CLASS_OUTPUT
```

Location of new class files.

---

#### CLASS_OUTPUT

public static final

StandardLocation

CLASS_OUTPUT

Location of new class files.

SOURCE_OUTPUT

```java
public static final
StandardLocation
SOURCE_OUTPUT
```

Location of new source files.

---

#### SOURCE_OUTPUT

public static final

StandardLocation

SOURCE_OUTPUT

Location of new source files.

CLASS_PATH

```java
public static final
StandardLocation
CLASS_PATH
```

Location to search for user class files.

---

#### CLASS_PATH

public static final

StandardLocation

CLASS_PATH

Location to search for user class files.

SOURCE_PATH

```java
public static final
StandardLocation
SOURCE_PATH
```

Location to search for existing source files.

---

#### SOURCE_PATH

public static final

StandardLocation

SOURCE_PATH

Location to search for existing source files.

ANNOTATION_PROCESSOR_PATH

```java
public static final
StandardLocation
ANNOTATION_PROCESSOR_PATH
```

Location to search for annotation processors.

---

#### ANNOTATION_PROCESSOR_PATH

public static final

StandardLocation

ANNOTATION_PROCESSOR_PATH

Location to search for annotation processors.

ANNOTATION_PROCESSOR_MODULE_PATH

```java
public static final
StandardLocation
ANNOTATION_PROCESSOR_MODULE_PATH
```

Location to search for modules containing annotation processors.

**Since:** 9

---

#### ANNOTATION_PROCESSOR_MODULE_PATH

public static final

StandardLocation

ANNOTATION_PROCESSOR_MODULE_PATH

Location to search for modules containing annotation processors.

PLATFORM_CLASS_PATH

```java
public static final
StandardLocation
PLATFORM_CLASS_PATH
```

Location to search for platform classes. Sometimes called
the boot class path.

---

#### PLATFORM_CLASS_PATH

public static final

StandardLocation

PLATFORM_CLASS_PATH

Location to search for platform classes. Sometimes called
the boot class path.

NATIVE_HEADER_OUTPUT

```java
public static final
StandardLocation
NATIVE_HEADER_OUTPUT
```

Location of new native header files.

**Since:** 1.8

---

#### NATIVE_HEADER_OUTPUT

public static final

StandardLocation

NATIVE_HEADER_OUTPUT

Location of new native header files.

MODULE_SOURCE_PATH

```java
public static final
StandardLocation
MODULE_SOURCE_PATH
```

Location to search for the source code of modules.

**Since:** 9

---

#### MODULE_SOURCE_PATH

public static final

StandardLocation

MODULE_SOURCE_PATH

Location to search for the source code of modules.

UPGRADE_MODULE_PATH

```java
public static final
StandardLocation
UPGRADE_MODULE_PATH
```

Location to search for upgradeable system modules.

**Since:** 9

---

#### UPGRADE_MODULE_PATH

public static final

StandardLocation

UPGRADE_MODULE_PATH

Location to search for upgradeable system modules.

SYSTEM_MODULES

```java
public static final
StandardLocation
SYSTEM_MODULES
```

Location to search for system modules.

**Since:** 9

---

#### SYSTEM_MODULES

public static final

StandardLocation

SYSTEM_MODULES

Location to search for system modules.

MODULE_PATH

```java
public static final
StandardLocation
MODULE_PATH
```

Location to search for precompiled user modules.

**Since:** 9

---

#### MODULE_PATH

public static final

StandardLocation

MODULE_PATH

Location to search for precompiled user modules.

PATCH_MODULE_PATH

```java
public static final
StandardLocation
PATCH_MODULE_PATH
```

Location to search for module patches.

**Since:** 9

---

#### PATCH_MODULE_PATH

public static final

StandardLocation

PATCH_MODULE_PATH

Location to search for module patches.

Method Detail

- values

```java
public static
StandardLocation
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardLocation c : StandardLocation.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardLocation
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- locationFor

```java
public static
JavaFileManager.Location
locationFor​(
String
name)
```

Returns a location object with the given name. The following
property must hold:

locationFor(x) ==
locationFor(y)

if and only if

x.equals(y)

.
The returned location will be an output location if and only if
name ends with

"_OUTPUT"

. It will be considered to
be a module-oriented location if the name contains the word

"MODULE"

.

**Parameters:** name

- a name
**Returns:** a location

- isModuleOrientedLocation

```java
public boolean isModuleOrientedLocation()
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

**Specified by:** isModuleOrientedLocation

in interface

JavaFileManager.Location
**Returns:** true if this location is expected to contain modules
**Since:** 9

---

#### Method Detail

values

```java
public static
StandardLocation
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardLocation c : StandardLocation.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

StandardLocation

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardLocation c : StandardLocation.values())
System.out.println(c);
```

for (StandardLocation c : StandardLocation.values())
System.out.println(c);

valueOf

```java
public static
StandardLocation
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

StandardLocation

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

locationFor

```java
public static
JavaFileManager.Location
locationFor​(
String
name)
```

Returns a location object with the given name. The following
property must hold:

locationFor(x) ==
locationFor(y)

if and only if

x.equals(y)

.
The returned location will be an output location if and only if
name ends with

"_OUTPUT"

. It will be considered to
be a module-oriented location if the name contains the word

"MODULE"

.

**Parameters:** name

- a name
**Returns:** a location

---

#### locationFor

public static

JavaFileManager.Location

locationFor​(

String

name)

Returns a location object with the given name. The following
property must hold:

locationFor(x) ==
locationFor(y)

if and only if

x.equals(y)

.
The returned location will be an output location if and only if
name ends with

"_OUTPUT"

. It will be considered to
be a module-oriented location if the name contains the word

"MODULE"

.

isModuleOrientedLocation

```java
public boolean isModuleOrientedLocation()
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

**Specified by:** isModuleOrientedLocation

in interface

JavaFileManager.Location
**Returns:** true if this location is expected to contain modules
**Since:** 9

---

#### isModuleOrientedLocation

public boolean isModuleOrientedLocation()

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

