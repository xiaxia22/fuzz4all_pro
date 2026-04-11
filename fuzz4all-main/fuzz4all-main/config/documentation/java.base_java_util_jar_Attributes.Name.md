# Class Attributes.Name

**Source:** `java.base\java\util\jar\Attributes.Name.html`

### Class Description

```java
public static class
Attributes.Name

extends
Object
```

The Attributes.Name class represents an attribute name stored in
this Map. Valid attribute names are case-insensitive, are restricted
to the ASCII characters in the set [0-9a-zA-Z_-], and cannot exceed
70 characters in length. Attribute values can contain any characters
and will be UTF8-encoded when written to the output stream. See the

JAR File Specification

for more information about valid attribute names and values.

**Enclosing class:** Attributes

---

### Field Details

#### public static final
Attributes.Name
MANIFEST_VERSION

Name

object for

Manifest-Version

manifest attribute. This attribute indicates the version number
of the manifest standard to which a JAR file's manifest conforms.

**See Also:**
- Manifest and Signature Specification

---

#### public static final
Attributes.Name
SIGNATURE_VERSION

Name

object for

Signature-Version

manifest attribute used when signing JAR files.

**See Also:**
- Manifest and Signature Specification

---

#### public static final
Attributes.Name
CONTENT_TYPE

Name

object for

Content-Type

manifest attribute.

---

#### public static final
Attributes.Name
CLASS_PATH

Name

object for

Class-Path

manifest attribute.

**See Also:**
- JAR file specification

---

#### public static final
Attributes.Name
MAIN_CLASS

Name

object for

Main-Class

manifest
attribute used for launching applications packaged in JAR files.
The

Main-Class

attribute is used in conjunction
with the

-jar

command-line option of the

java

application launcher.

---

#### public static final
Attributes.Name
SEALED

Name

object for

Sealed

manifest attribute
used for sealing.

**See Also:**
- Package Sealing

---

#### public static final
Attributes.Name
EXTENSION_LIST

Name

object for

Extension-List

manifest attribute
used for the extension mechanism that is no longer supported.

---

#### public static final
Attributes.Name
EXTENSION_NAME

Name

object for

Extension-Name

manifest attribute.
used for the extension mechanism that is no longer supported.

---

#### @Deprecated

public static final
Attributes.Name
EXTENSION_INSTALLATION

Name

object for

Extension-Installation

manifest attribute.

---

#### public static final
Attributes.Name
IMPLEMENTATION_TITLE

Name

object for

Implementation-Title

manifest attribute used for package versioning.

---

#### public static final
Attributes.Name
IMPLEMENTATION_VERSION

Name

object for

Implementation-Version

manifest attribute used for package versioning.

---

#### public static final
Attributes.Name
IMPLEMENTATION_VENDOR

Name

object for

Implementation-Vendor

manifest attribute used for package versioning.

---

#### @Deprecated

public static final
Attributes.Name
IMPLEMENTATION_VENDOR_ID

Name

object for

Implementation-Vendor-Id

manifest attribute.

---

#### @Deprecated

public static final
Attributes.Name
IMPLEMENTATION_URL

Name

object for

Implementation-URL

manifest attribute.

---

#### public static final
Attributes.Name
SPECIFICATION_TITLE

Name

object for

Specification-Title

manifest attribute used for package versioning.

---

#### public static final
Attributes.Name
SPECIFICATION_VERSION

Name

object for

Specification-Version

manifest attribute used for package versioning.

---

#### public static final
Attributes.Name
SPECIFICATION_VENDOR

Name

object for

Specification-Vendor

manifest attribute used for package versioning.

---

#### public static final
Attributes.Name
MULTI_RELEASE

Name

object for

Multi-Release

manifest attribute that indicates this is a multi-release JAR file.

**Since:**
- 9

---

### Constructor Details

#### public Name​(
String
name)

Constructs a new attribute name using the given string name.

**Parameters:**
- name

- the attribute string name

**Throws:**
- IllegalArgumentException

- if the attribute name was
invalid
- NullPointerException

- if the attribute name was null

---

### Method Details

#### public boolean equals​(
Object
o)

Compares this attribute name to another for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the object to compare

**Returns:**
- true if this attribute name is equal to the
specified attribute object

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Computes the hash value for this attribute name.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns the attribute name as a String.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class Attributes.Name

java.lang.Object

- java.util.jar.Attributes.Name

java.util.jar.Attributes.Name

**Enclosing class:** Attributes

```java
public static class
Attributes.Name

extends
Object
```

The Attributes.Name class represents an attribute name stored in
this Map. Valid attribute names are case-insensitive, are restricted
to the ASCII characters in the set [0-9a-zA-Z_-], and cannot exceed
70 characters in length. Attribute values can contain any characters
and will be UTF8-encoded when written to the output stream. See the

JAR File Specification

for more information about valid attribute names and values.

public static class

Attributes.Name

extends

Object

The Attributes.Name class represents an attribute name stored in
this Map. Valid attribute names are case-insensitive, are restricted
to the ASCII characters in the set [0-9a-zA-Z_-], and cannot exceed
70 characters in length. Attribute values can contain any characters
and will be UTF8-encoded when written to the output stream. See the

JAR File Specification

for more information about valid attribute names and values.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Attributes.Name

CLASS_PATH

Name

object for

Class-Path

manifest attribute.

static

Attributes.Name

CONTENT_TYPE

Name

object for

Content-Type

manifest attribute.

static

Attributes.Name

EXTENSION_INSTALLATION

Deprecated.

Extension mechanism is no longer supported.

static

Attributes.Name

EXTENSION_LIST

Name

object for

Extension-List

manifest attribute
used for the extension mechanism that is no longer supported.

static

Attributes.Name

EXTENSION_NAME

Name

object for

Extension-Name

manifest attribute.

static

Attributes.Name

IMPLEMENTATION_TITLE

Name

object for

Implementation-Title

manifest attribute used for package versioning.

static

Attributes.Name

IMPLEMENTATION_URL

Deprecated.

Extension mechanism is no longer supported.

static

Attributes.Name

IMPLEMENTATION_VENDOR

Name

object for

Implementation-Vendor

manifest attribute used for package versioning.

static

Attributes.Name

IMPLEMENTATION_VENDOR_ID

Deprecated.

Extension mechanism is no longer supported.

static

Attributes.Name

IMPLEMENTATION_VERSION

Name

object for

Implementation-Version

manifest attribute used for package versioning.

static

Attributes.Name

MAIN_CLASS

Name

object for

Main-Class

manifest
attribute used for launching applications packaged in JAR files.

static

Attributes.Name

MANIFEST_VERSION

Name

object for

Manifest-Version

manifest attribute.

static

Attributes.Name

MULTI_RELEASE

Name

object for

Multi-Release

manifest attribute that indicates this is a multi-release JAR file.

static

Attributes.Name

SEALED

Name

object for

Sealed

manifest attribute
used for sealing.

static

Attributes.Name

SIGNATURE_VERSION

Name

object for

Signature-Version

manifest attribute used when signing JAR files.

static

Attributes.Name

SPECIFICATION_TITLE

Name

object for

Specification-Title

manifest attribute used for package versioning.

static

Attributes.Name

SPECIFICATION_VENDOR

Name

object for

Specification-Vendor

manifest attribute used for package versioning.

static

Attributes.Name

SPECIFICATION_VERSION

Name

object for

Specification-Version

manifest attribute used for package versioning.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Name

​(

String

name)

Constructs a new attribute name using the given string name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Compares this attribute name to another for equality.

int

hashCode

()

Computes the hash value for this attribute name.

String

toString

()

Returns the attribute name as a String.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Field Summary

Fields

Modifier and Type

Field

Description

static

Attributes.Name

CLASS_PATH

Name

object for

Class-Path

manifest attribute.

static

Attributes.Name

CONTENT_TYPE

Name

object for

Content-Type

manifest attribute.

static

Attributes.Name

EXTENSION_INSTALLATION

Deprecated.

Extension mechanism is no longer supported.

static

Attributes.Name

EXTENSION_LIST

Name

object for

Extension-List

manifest attribute
used for the extension mechanism that is no longer supported.

static

Attributes.Name

EXTENSION_NAME

Name

object for

Extension-Name

manifest attribute.

static

Attributes.Name

IMPLEMENTATION_TITLE

Name

object for

Implementation-Title

manifest attribute used for package versioning.

static

Attributes.Name

IMPLEMENTATION_URL

Deprecated.

Extension mechanism is no longer supported.

static

Attributes.Name

IMPLEMENTATION_VENDOR

Name

object for

Implementation-Vendor

manifest attribute used for package versioning.

static

Attributes.Name

IMPLEMENTATION_VENDOR_ID

Deprecated.

Extension mechanism is no longer supported.

static

Attributes.Name

IMPLEMENTATION_VERSION

Name

object for

Implementation-Version

manifest attribute used for package versioning.

static

Attributes.Name

MAIN_CLASS

Name

object for

Main-Class

manifest
attribute used for launching applications packaged in JAR files.

static

Attributes.Name

MANIFEST_VERSION

Name

object for

Manifest-Version

manifest attribute.

static

Attributes.Name

MULTI_RELEASE

Name

object for

Multi-Release

manifest attribute that indicates this is a multi-release JAR file.

static

Attributes.Name

SEALED

Name

object for

Sealed

manifest attribute
used for sealing.

static

Attributes.Name

SIGNATURE_VERSION

Name

object for

Signature-Version

manifest attribute used when signing JAR files.

static

Attributes.Name

SPECIFICATION_TITLE

Name

object for

Specification-Title

manifest attribute used for package versioning.

static

Attributes.Name

SPECIFICATION_VENDOR

Name

object for

Specification-Vendor

manifest attribute used for package versioning.

static

Attributes.Name

SPECIFICATION_VERSION

Name

object for

Specification-Version

manifest attribute used for package versioning.

---

#### Field Summary

Name

object for

Class-Path

manifest attribute.

Name

object for

Content-Type

manifest attribute.

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Extension-List

manifest attribute
used for the extension mechanism that is no longer supported.

Name

object for

Extension-Name

manifest attribute.

Name

object for

Implementation-Title

manifest attribute used for package versioning.

Name

object for

Implementation-Vendor

manifest attribute used for package versioning.

Name

object for

Implementation-Version

manifest attribute used for package versioning.

Name

object for

Main-Class

manifest
attribute used for launching applications packaged in JAR files.

Name

object for

Manifest-Version

manifest attribute.

Name

object for

Multi-Release

manifest attribute that indicates this is a multi-release JAR file.

Name

object for

Sealed

manifest attribute
used for sealing.

Name

object for

Signature-Version

manifest attribute used when signing JAR files.

Name

object for

Specification-Title

manifest attribute used for package versioning.

Name

object for

Specification-Vendor

manifest attribute used for package versioning.

Name

object for

Specification-Version

manifest attribute used for package versioning.

Constructor Summary

Constructors

Constructor

Description

Name

​(

String

name)

Constructs a new attribute name using the given string name.

---

#### Constructor Summary

Constructs a new attribute name using the given string name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Compares this attribute name to another for equality.

int

hashCode

()

Computes the hash value for this attribute name.

String

toString

()

Returns the attribute name as a String.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

#### Method Summary

Compares this attribute name to another for equality.

Computes the hash value for this attribute name.

Returns the attribute name as a String.

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

============ FIELD DETAIL ===========

- Field Detail

- MANIFEST_VERSION

```java
public static final
Attributes.Name
MANIFEST_VERSION
```

Name

object for

Manifest-Version

manifest attribute. This attribute indicates the version number
of the manifest standard to which a JAR file's manifest conforms.

**See Also:** Manifest and Signature Specification

- SIGNATURE_VERSION

```java
public static final
Attributes.Name
SIGNATURE_VERSION
```

Name

object for

Signature-Version

manifest attribute used when signing JAR files.

**See Also:** Manifest and Signature Specification

- CONTENT_TYPE

```java
public static final
Attributes.Name
CONTENT_TYPE
```

Name

object for

Content-Type

manifest attribute.

- CLASS_PATH

```java
public static final
Attributes.Name
CLASS_PATH
```

Name

object for

Class-Path

manifest attribute.

**See Also:** JAR file specification

- MAIN_CLASS

```java
public static final
Attributes.Name
MAIN_CLASS
```

Name

object for

Main-Class

manifest
attribute used for launching applications packaged in JAR files.
The

Main-Class

attribute is used in conjunction
with the

-jar

command-line option of the

java

application launcher.

- SEALED

```java
public static final
Attributes.Name
SEALED
```

Name

object for

Sealed

manifest attribute
used for sealing.

**See Also:** Package Sealing

- EXTENSION_LIST

```java
public static final
Attributes.Name
EXTENSION_LIST
```

Name

object for

Extension-List

manifest attribute
used for the extension mechanism that is no longer supported.

- EXTENSION_NAME

```java
public static final
Attributes.Name
EXTENSION_NAME
```

Name

object for

Extension-Name

manifest attribute.
used for the extension mechanism that is no longer supported.

- EXTENSION_INSTALLATION

```java
@Deprecated

public static final
Attributes.Name
EXTENSION_INSTALLATION
```

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Extension-Installation

manifest attribute.

- IMPLEMENTATION_TITLE

```java
public static final
Attributes.Name
IMPLEMENTATION_TITLE
```

Name

object for

Implementation-Title

manifest attribute used for package versioning.

- IMPLEMENTATION_VERSION

```java
public static final
Attributes.Name
IMPLEMENTATION_VERSION
```

Name

object for

Implementation-Version

manifest attribute used for package versioning.

- IMPLEMENTATION_VENDOR

```java
public static final
Attributes.Name
IMPLEMENTATION_VENDOR
```

Name

object for

Implementation-Vendor

manifest attribute used for package versioning.

- IMPLEMENTATION_VENDOR_ID

```java
@Deprecated

public static final
Attributes.Name
IMPLEMENTATION_VENDOR_ID
```

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Implementation-Vendor-Id

manifest attribute.

- IMPLEMENTATION_URL

```java
@Deprecated

public static final
Attributes.Name
IMPLEMENTATION_URL
```

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Implementation-URL

manifest attribute.

- SPECIFICATION_TITLE

```java
public static final
Attributes.Name
SPECIFICATION_TITLE
```

Name

object for

Specification-Title

manifest attribute used for package versioning.

- SPECIFICATION_VERSION

```java
public static final
Attributes.Name
SPECIFICATION_VERSION
```

Name

object for

Specification-Version

manifest attribute used for package versioning.

- SPECIFICATION_VENDOR

```java
public static final
Attributes.Name
SPECIFICATION_VENDOR
```

Name

object for

Specification-Vendor

manifest attribute used for package versioning.

- MULTI_RELEASE

```java
public static final
Attributes.Name
MULTI_RELEASE
```

Name

object for

Multi-Release

manifest attribute that indicates this is a multi-release JAR file.

**Since:** 9

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Name

```java
public Name​(
String
name)
```

Constructs a new attribute name using the given string name.

**Parameters:** name

- the attribute string name
**Throws:** IllegalArgumentException

- if the attribute name was
invalid
**Throws:** NullPointerException

- if the attribute name was null

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
o)
```

Compares this attribute name to another for equality.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare
**Returns:** true if this attribute name is equal to the
specified attribute object
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes the hash value for this attribute name.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the attribute name as a String.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Field Detail

- MANIFEST_VERSION

```java
public static final
Attributes.Name
MANIFEST_VERSION
```

Name

object for

Manifest-Version

manifest attribute. This attribute indicates the version number
of the manifest standard to which a JAR file's manifest conforms.

**See Also:** Manifest and Signature Specification

- SIGNATURE_VERSION

```java
public static final
Attributes.Name
SIGNATURE_VERSION
```

Name

object for

Signature-Version

manifest attribute used when signing JAR files.

**See Also:** Manifest and Signature Specification

- CONTENT_TYPE

```java
public static final
Attributes.Name
CONTENT_TYPE
```

Name

object for

Content-Type

manifest attribute.

- CLASS_PATH

```java
public static final
Attributes.Name
CLASS_PATH
```

Name

object for

Class-Path

manifest attribute.

**See Also:** JAR file specification

- MAIN_CLASS

```java
public static final
Attributes.Name
MAIN_CLASS
```

Name

object for

Main-Class

manifest
attribute used for launching applications packaged in JAR files.
The

Main-Class

attribute is used in conjunction
with the

-jar

command-line option of the

java

application launcher.

- SEALED

```java
public static final
Attributes.Name
SEALED
```

Name

object for

Sealed

manifest attribute
used for sealing.

**See Also:** Package Sealing

- EXTENSION_LIST

```java
public static final
Attributes.Name
EXTENSION_LIST
```

Name

object for

Extension-List

manifest attribute
used for the extension mechanism that is no longer supported.

- EXTENSION_NAME

```java
public static final
Attributes.Name
EXTENSION_NAME
```

Name

object for

Extension-Name

manifest attribute.
used for the extension mechanism that is no longer supported.

- EXTENSION_INSTALLATION

```java
@Deprecated

public static final
Attributes.Name
EXTENSION_INSTALLATION
```

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Extension-Installation

manifest attribute.

- IMPLEMENTATION_TITLE

```java
public static final
Attributes.Name
IMPLEMENTATION_TITLE
```

Name

object for

Implementation-Title

manifest attribute used for package versioning.

- IMPLEMENTATION_VERSION

```java
public static final
Attributes.Name
IMPLEMENTATION_VERSION
```

Name

object for

Implementation-Version

manifest attribute used for package versioning.

- IMPLEMENTATION_VENDOR

```java
public static final
Attributes.Name
IMPLEMENTATION_VENDOR
```

Name

object for

Implementation-Vendor

manifest attribute used for package versioning.

- IMPLEMENTATION_VENDOR_ID

```java
@Deprecated

public static final
Attributes.Name
IMPLEMENTATION_VENDOR_ID
```

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Implementation-Vendor-Id

manifest attribute.

- IMPLEMENTATION_URL

```java
@Deprecated

public static final
Attributes.Name
IMPLEMENTATION_URL
```

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Implementation-URL

manifest attribute.

- SPECIFICATION_TITLE

```java
public static final
Attributes.Name
SPECIFICATION_TITLE
```

Name

object for

Specification-Title

manifest attribute used for package versioning.

- SPECIFICATION_VERSION

```java
public static final
Attributes.Name
SPECIFICATION_VERSION
```

Name

object for

Specification-Version

manifest attribute used for package versioning.

- SPECIFICATION_VENDOR

```java
public static final
Attributes.Name
SPECIFICATION_VENDOR
```

Name

object for

Specification-Vendor

manifest attribute used for package versioning.

- MULTI_RELEASE

```java
public static final
Attributes.Name
MULTI_RELEASE
```

Name

object for

Multi-Release

manifest attribute that indicates this is a multi-release JAR file.

**Since:** 9

---

#### Field Detail

MANIFEST_VERSION

```java
public static final
Attributes.Name
MANIFEST_VERSION
```

Name

object for

Manifest-Version

manifest attribute. This attribute indicates the version number
of the manifest standard to which a JAR file's manifest conforms.

**See Also:** Manifest and Signature Specification

---

#### MANIFEST_VERSION

public static final

Attributes.Name

MANIFEST_VERSION

Name

object for

Manifest-Version

manifest attribute. This attribute indicates the version number
of the manifest standard to which a JAR file's manifest conforms.

SIGNATURE_VERSION

```java
public static final
Attributes.Name
SIGNATURE_VERSION
```

Name

object for

Signature-Version

manifest attribute used when signing JAR files.

**See Also:** Manifest and Signature Specification

---

#### SIGNATURE_VERSION

public static final

Attributes.Name

SIGNATURE_VERSION

Name

object for

Signature-Version

manifest attribute used when signing JAR files.

CONTENT_TYPE

```java
public static final
Attributes.Name
CONTENT_TYPE
```

Name

object for

Content-Type

manifest attribute.

---

#### CONTENT_TYPE

public static final

Attributes.Name

CONTENT_TYPE

Name

object for

Content-Type

manifest attribute.

CLASS_PATH

```java
public static final
Attributes.Name
CLASS_PATH
```

Name

object for

Class-Path

manifest attribute.

**See Also:** JAR file specification

---

#### CLASS_PATH

public static final

Attributes.Name

CLASS_PATH

Name

object for

Class-Path

manifest attribute.

MAIN_CLASS

```java
public static final
Attributes.Name
MAIN_CLASS
```

Name

object for

Main-Class

manifest
attribute used for launching applications packaged in JAR files.
The

Main-Class

attribute is used in conjunction
with the

-jar

command-line option of the

java

application launcher.

---

#### MAIN_CLASS

public static final

Attributes.Name

MAIN_CLASS

Name

object for

Main-Class

manifest
attribute used for launching applications packaged in JAR files.
The

Main-Class

attribute is used in conjunction
with the

-jar

command-line option of the

java

application launcher.

SEALED

```java
public static final
Attributes.Name
SEALED
```

Name

object for

Sealed

manifest attribute
used for sealing.

**See Also:** Package Sealing

---

#### SEALED

public static final

Attributes.Name

SEALED

Name

object for

Sealed

manifest attribute
used for sealing.

EXTENSION_LIST

```java
public static final
Attributes.Name
EXTENSION_LIST
```

Name

object for

Extension-List

manifest attribute
used for the extension mechanism that is no longer supported.

---

#### EXTENSION_LIST

public static final

Attributes.Name

EXTENSION_LIST

Name

object for

Extension-List

manifest attribute
used for the extension mechanism that is no longer supported.

EXTENSION_NAME

```java
public static final
Attributes.Name
EXTENSION_NAME
```

Name

object for

Extension-Name

manifest attribute.
used for the extension mechanism that is no longer supported.

---

#### EXTENSION_NAME

public static final

Attributes.Name

EXTENSION_NAME

Name

object for

Extension-Name

manifest attribute.
used for the extension mechanism that is no longer supported.

EXTENSION_INSTALLATION

```java
@Deprecated

public static final
Attributes.Name
EXTENSION_INSTALLATION
```

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Extension-Installation

manifest attribute.

---

#### EXTENSION_INSTALLATION

@Deprecated

public static final

Attributes.Name

EXTENSION_INSTALLATION

Name

object for

Extension-Installation

manifest attribute.

IMPLEMENTATION_TITLE

```java
public static final
Attributes.Name
IMPLEMENTATION_TITLE
```

Name

object for

Implementation-Title

manifest attribute used for package versioning.

---

#### IMPLEMENTATION_TITLE

public static final

Attributes.Name

IMPLEMENTATION_TITLE

Name

object for

Implementation-Title

manifest attribute used for package versioning.

IMPLEMENTATION_VERSION

```java
public static final
Attributes.Name
IMPLEMENTATION_VERSION
```

Name

object for

Implementation-Version

manifest attribute used for package versioning.

---

#### IMPLEMENTATION_VERSION

public static final

Attributes.Name

IMPLEMENTATION_VERSION

Name

object for

Implementation-Version

manifest attribute used for package versioning.

IMPLEMENTATION_VENDOR

```java
public static final
Attributes.Name
IMPLEMENTATION_VENDOR
```

Name

object for

Implementation-Vendor

manifest attribute used for package versioning.

---

#### IMPLEMENTATION_VENDOR

public static final

Attributes.Name

IMPLEMENTATION_VENDOR

Name

object for

Implementation-Vendor

manifest attribute used for package versioning.

IMPLEMENTATION_VENDOR_ID

```java
@Deprecated

public static final
Attributes.Name
IMPLEMENTATION_VENDOR_ID
```

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Implementation-Vendor-Id

manifest attribute.

---

#### IMPLEMENTATION_VENDOR_ID

@Deprecated

public static final

Attributes.Name

IMPLEMENTATION_VENDOR_ID

Name

object for

Implementation-Vendor-Id

manifest attribute.

IMPLEMENTATION_URL

```java
@Deprecated

public static final
Attributes.Name
IMPLEMENTATION_URL
```

Deprecated.

Extension mechanism is no longer supported.

Name

object for

Implementation-URL

manifest attribute.

---

#### IMPLEMENTATION_URL

@Deprecated

public static final

Attributes.Name

IMPLEMENTATION_URL

Name

object for

Implementation-URL

manifest attribute.

SPECIFICATION_TITLE

```java
public static final
Attributes.Name
SPECIFICATION_TITLE
```

Name

object for

Specification-Title

manifest attribute used for package versioning.

---

#### SPECIFICATION_TITLE

public static final

Attributes.Name

SPECIFICATION_TITLE

Name

object for

Specification-Title

manifest attribute used for package versioning.

SPECIFICATION_VERSION

```java
public static final
Attributes.Name
SPECIFICATION_VERSION
```

Name

object for

Specification-Version

manifest attribute used for package versioning.

---

#### SPECIFICATION_VERSION

public static final

Attributes.Name

SPECIFICATION_VERSION

Name

object for

Specification-Version

manifest attribute used for package versioning.

SPECIFICATION_VENDOR

```java
public static final
Attributes.Name
SPECIFICATION_VENDOR
```

Name

object for

Specification-Vendor

manifest attribute used for package versioning.

---

#### SPECIFICATION_VENDOR

public static final

Attributes.Name

SPECIFICATION_VENDOR

Name

object for

Specification-Vendor

manifest attribute used for package versioning.

MULTI_RELEASE

```java
public static final
Attributes.Name
MULTI_RELEASE
```

Name

object for

Multi-Release

manifest attribute that indicates this is a multi-release JAR file.

**Since:** 9

---

#### MULTI_RELEASE

public static final

Attributes.Name

MULTI_RELEASE

Name

object for

Multi-Release

manifest attribute that indicates this is a multi-release JAR file.

Constructor Detail

- Name

```java
public Name​(
String
name)
```

Constructs a new attribute name using the given string name.

**Parameters:** name

- the attribute string name
**Throws:** IllegalArgumentException

- if the attribute name was
invalid
**Throws:** NullPointerException

- if the attribute name was null

---

#### Constructor Detail

Name

```java
public Name​(
String
name)
```

Constructs a new attribute name using the given string name.

**Parameters:** name

- the attribute string name
**Throws:** IllegalArgumentException

- if the attribute name was
invalid
**Throws:** NullPointerException

- if the attribute name was null

---

#### Name

public Name​(

String

name)

Constructs a new attribute name using the given string name.

Method Detail

- equals

```java
public boolean equals​(
Object
o)
```

Compares this attribute name to another for equality.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare
**Returns:** true if this attribute name is equal to the
specified attribute object
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes the hash value for this attribute name.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the attribute name as a String.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

equals

```java
public boolean equals​(
Object
o)
```

Compares this attribute name to another for equality.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare
**Returns:** true if this attribute name is equal to the
specified attribute object
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares this attribute name to another for equality.

hashCode

```java
public int hashCode()
```

Computes the hash value for this attribute name.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes the hash value for this attribute name.

toString

```java
public
String
toString()
```

Returns the attribute name as a String.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns the attribute name as a String.

---

