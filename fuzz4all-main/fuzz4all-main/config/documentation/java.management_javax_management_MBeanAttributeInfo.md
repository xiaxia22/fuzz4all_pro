# Class MBeanAttributeInfo

**Source:** `java.management\javax\management\MBeanAttributeInfo.html`

### Class Description

```java
public class
MBeanAttributeInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

Describes an MBean attribute exposed for management. Instances of
this class are immutable. Subclasses may be mutable but this is
not recommended.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanAttributeInfo​(
String
name,

String
type,

String
description,
boolean isReadable,
boolean isWritable,
boolean isIs)

Constructs an

MBeanAttributeInfo

object.

**Parameters:**
- name

- The name of the attribute.
- type

- The type or class name of the attribute.
- description

- A human readable description of the attribute.
- isReadable

- True if the attribute has a getter method, false otherwise.
- isWritable

- True if the attribute has a setter method, false otherwise.
- isIs

- True if this attribute has an "is" getter, false otherwise.

**Throws:**
- IllegalArgumentException

- if

isIs

is true but

isReadable

is not, or if

isIs

is true and

type

is not

boolean

or

java.lang.Boolean

.
(New code should always use

boolean

rather than

java.lang.Boolean

.)

---

#### public MBeanAttributeInfo​(
String
name,

String
type,

String
description,
boolean isReadable,
boolean isWritable,
boolean isIs,

Descriptor
descriptor)

Constructs an

MBeanAttributeInfo

object.

**Parameters:**
- name

- The name of the attribute.
- type

- The type or class name of the attribute.
- description

- A human readable description of the attribute.
- isReadable

- True if the attribute has a getter method, false otherwise.
- isWritable

- True if the attribute has a setter method, false otherwise.
- isIs

- True if this attribute has an "is" getter, false otherwise.
- descriptor

- The descriptor for the attribute. This may be null
which is equivalent to an empty descriptor.

**Throws:**
- IllegalArgumentException

- if

isIs

is true but

isReadable

is not, or if

isIs

is true and

type

is not

boolean

or

java.lang.Boolean

.
(New code should always use

boolean

rather than

java.lang.Boolean

.)

**Since:**
- 1.6

---

#### public MBeanAttributeInfo​(
String
name,

String
description,

Method
getter,

Method
setter)
throws
IntrospectionException

This constructor takes the name of a simple attribute, and Method
objects for reading and writing the attribute. The

Descriptor

of the constructed object will include fields contributed by any
annotations on the

Method

objects that contain the

DescriptorKey

meta-annotation.

**Parameters:**
- name

- The programmatic name of the attribute.
- description

- A human readable description of the attribute.
- getter

- The method used for reading the attribute value.
May be null if the property is write-only.
- setter

- The method used for writing the attribute value.
May be null if the attribute is read-only.

**Throws:**
- IntrospectionException

- There is a consistency
problem in the definition of this attribute.

---

### Method Details

#### public
Object
clone()

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

#### public
String
getType()

Returns the class name of the attribute.

**Returns:**
- the class name.

---

#### public boolean isReadable()

Whether the value of the attribute can be read.

**Returns:**
- True if the attribute can be read, false otherwise.

---

#### public boolean isWritable()

Whether new values can be written to the attribute.

**Returns:**
- True if the attribute can be written to, false otherwise.

---

#### public boolean isIs()

Indicates if this attribute has an "is" getter.

**Returns:**
- true if this attribute has an "is" getter.

---

#### public boolean equals​(
Object
o)

Compare this MBeanAttributeInfo to another.

**Overrides:**
- equals

in class

MBeanFeatureInfo

**Parameters:**
- o

- the object to compare to.

**Returns:**
- true if and only if

o

is an MBeanAttributeInfo such
that its

MBeanFeatureInfo.getName()

,

getType()

,

MBeanFeatureInfo.getDescription()

,

isReadable()

,

isWritable()

, and

isIs()

values are equal (not
necessarily identical) to those of this MBeanAttributeInfo.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class MBeanAttributeInfo

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanAttributeInfo

javax.management.MBeanFeatureInfo

- javax.management.MBeanAttributeInfo

javax.management.MBeanAttributeInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

**Direct Known Subclasses:** ModelMBeanAttributeInfo

,

OpenMBeanAttributeInfoSupport

```java
public class
MBeanAttributeInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

Describes an MBean attribute exposed for management. Instances of
this class are immutable. Subclasses may be mutable but this is
not recommended.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanAttributeInfo

extends

MBeanFeatureInfo

implements

Cloneable

Describes an MBean attribute exposed for management. Instances of
this class are immutable. Subclasses may be mutable but this is
not recommended.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.management.

MBeanFeatureInfo

description

,

name

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanAttributeInfo

​(

String

name,

String

description,

Method

getter,

Method

setter)

This constructor takes the name of a simple attribute, and Method
objects for reading and writing the attribute.

MBeanAttributeInfo

​(

String

name,

String

type,

String

description,
boolean isReadable,
boolean isWritable,
boolean isIs)

Constructs an

MBeanAttributeInfo

object.

MBeanAttributeInfo

​(

String

name,

String

type,

String

description,
boolean isReadable,
boolean isWritable,
boolean isIs,

Descriptor

descriptor)

Constructs an

MBeanAttributeInfo

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a shallow clone of this instance.

boolean

equals

​(

Object

o)

Compare this MBeanAttributeInfo to another.

String

getType

()

Returns the class name of the attribute.

boolean

isIs

()

Indicates if this attribute has an "is" getter.

boolean

isReadable

()

Whether the value of the attribute can be read.

boolean

isWritable

()

Whether new values can be written to the attribute.

- Methods declared in class javax.management.

MBeanFeatureInfo

getDescription

,

getDescriptor

,

getName

- Methods declared in class java.lang.

Object

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

Field Summary

- Fields declared in class javax.management.

MBeanFeatureInfo

description

,

name

---

#### Field Summary

Fields declared in class javax.management.

MBeanFeatureInfo

description

,

name

---

#### Fields declared in class javax.management. MBeanFeatureInfo

Constructor Summary

Constructors

Constructor

Description

MBeanAttributeInfo

​(

String

name,

String

description,

Method

getter,

Method

setter)

This constructor takes the name of a simple attribute, and Method
objects for reading and writing the attribute.

MBeanAttributeInfo

​(

String

name,

String

type,

String

description,
boolean isReadable,
boolean isWritable,
boolean isIs)

Constructs an

MBeanAttributeInfo

object.

MBeanAttributeInfo

​(

String

name,

String

type,

String

description,
boolean isReadable,
boolean isWritable,
boolean isIs,

Descriptor

descriptor)

Constructs an

MBeanAttributeInfo

object.

---

#### Constructor Summary

This constructor takes the name of a simple attribute, and Method
objects for reading and writing the attribute.

Constructs an

MBeanAttributeInfo

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a shallow clone of this instance.

boolean

equals

​(

Object

o)

Compare this MBeanAttributeInfo to another.

String

getType

()

Returns the class name of the attribute.

boolean

isIs

()

Indicates if this attribute has an "is" getter.

boolean

isReadable

()

Whether the value of the attribute can be read.

boolean

isWritable

()

Whether new values can be written to the attribute.

- Methods declared in class javax.management.

MBeanFeatureInfo

getDescription

,

getDescriptor

,

getName

- Methods declared in class java.lang.

Object

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

Returns a shallow clone of this instance.

Compare this MBeanAttributeInfo to another.

Returns the class name of the attribute.

Indicates if this attribute has an "is" getter.

Whether the value of the attribute can be read.

Whether new values can be written to the attribute.

Methods declared in class javax.management.

MBeanFeatureInfo

getDescription

,

getDescriptor

,

getName

---

#### Methods declared in class javax.management. MBeanFeatureInfo

Methods declared in class java.lang.

Object

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

- MBeanAttributeInfo

```java
public MBeanAttributeInfo​(
String
name,

String
type,

String
description,
boolean isReadable,
boolean isWritable,
boolean isIs)
```

Constructs an

MBeanAttributeInfo

object.

**Parameters:** name

- The name of the attribute.
**Parameters:** type

- The type or class name of the attribute.
**Parameters:** description

- A human readable description of the attribute.
**Parameters:** isReadable

- True if the attribute has a getter method, false otherwise.
**Parameters:** isWritable

- True if the attribute has a setter method, false otherwise.
**Parameters:** isIs

- True if this attribute has an "is" getter, false otherwise.
**Throws:** IllegalArgumentException

- if

isIs

is true but

isReadable

is not, or if

isIs

is true and

type

is not

boolean

or

java.lang.Boolean

.
(New code should always use

boolean

rather than

java.lang.Boolean

.)

- MBeanAttributeInfo

```java
public MBeanAttributeInfo​(
String
name,

String
type,

String
description,
boolean isReadable,
boolean isWritable,
boolean isIs,

Descriptor
descriptor)
```

Constructs an

MBeanAttributeInfo

object.

**Parameters:** name

- The name of the attribute.
**Parameters:** type

- The type or class name of the attribute.
**Parameters:** description

- A human readable description of the attribute.
**Parameters:** isReadable

- True if the attribute has a getter method, false otherwise.
**Parameters:** isWritable

- True if the attribute has a setter method, false otherwise.
**Parameters:** isIs

- True if this attribute has an "is" getter, false otherwise.
**Parameters:** descriptor

- The descriptor for the attribute. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

isIs

is true but

isReadable

is not, or if

isIs

is true and

type

is not

boolean

or

java.lang.Boolean

.
(New code should always use

boolean

rather than

java.lang.Boolean

.)
**Since:** 1.6

- MBeanAttributeInfo

```java
public MBeanAttributeInfo​(
String
name,

String
description,

Method
getter,

Method
setter)
throws
IntrospectionException
```

This constructor takes the name of a simple attribute, and Method
objects for reading and writing the attribute. The

Descriptor

of the constructed object will include fields contributed by any
annotations on the

Method

objects that contain the

DescriptorKey

meta-annotation.

**Parameters:** name

- The programmatic name of the attribute.
**Parameters:** description

- A human readable description of the attribute.
**Parameters:** getter

- The method used for reading the attribute value.
May be null if the property is write-only.
**Parameters:** setter

- The method used for writing the attribute value.
May be null if the attribute is read-only.
**Throws:** IntrospectionException

- There is a consistency
problem in the definition of this attribute.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getType

```java
public
String
getType()
```

Returns the class name of the attribute.

**Returns:** the class name.

- isReadable

```java
public boolean isReadable()
```

Whether the value of the attribute can be read.

**Returns:** True if the attribute can be read, false otherwise.

- isWritable

```java
public boolean isWritable()
```

Whether new values can be written to the attribute.

**Returns:** True if the attribute can be written to, false otherwise.

- isIs

```java
public boolean isIs()
```

Indicates if this attribute has an "is" getter.

**Returns:** true if this attribute has an "is" getter.

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanAttributeInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanAttributeInfo such
that its

MBeanFeatureInfo.getName()

,

getType()

,

MBeanFeatureInfo.getDescription()

,

isReadable()

,

isWritable()

, and

isIs()

values are equal (not
necessarily identical) to those of this MBeanAttributeInfo.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- MBeanAttributeInfo

```java
public MBeanAttributeInfo​(
String
name,

String
type,

String
description,
boolean isReadable,
boolean isWritable,
boolean isIs)
```

Constructs an

MBeanAttributeInfo

object.

**Parameters:** name

- The name of the attribute.
**Parameters:** type

- The type or class name of the attribute.
**Parameters:** description

- A human readable description of the attribute.
**Parameters:** isReadable

- True if the attribute has a getter method, false otherwise.
**Parameters:** isWritable

- True if the attribute has a setter method, false otherwise.
**Parameters:** isIs

- True if this attribute has an "is" getter, false otherwise.
**Throws:** IllegalArgumentException

- if

isIs

is true but

isReadable

is not, or if

isIs

is true and

type

is not

boolean

or

java.lang.Boolean

.
(New code should always use

boolean

rather than

java.lang.Boolean

.)

- MBeanAttributeInfo

```java
public MBeanAttributeInfo​(
String
name,

String
type,

String
description,
boolean isReadable,
boolean isWritable,
boolean isIs,

Descriptor
descriptor)
```

Constructs an

MBeanAttributeInfo

object.

**Parameters:** name

- The name of the attribute.
**Parameters:** type

- The type or class name of the attribute.
**Parameters:** description

- A human readable description of the attribute.
**Parameters:** isReadable

- True if the attribute has a getter method, false otherwise.
**Parameters:** isWritable

- True if the attribute has a setter method, false otherwise.
**Parameters:** isIs

- True if this attribute has an "is" getter, false otherwise.
**Parameters:** descriptor

- The descriptor for the attribute. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

isIs

is true but

isReadable

is not, or if

isIs

is true and

type

is not

boolean

or

java.lang.Boolean

.
(New code should always use

boolean

rather than

java.lang.Boolean

.)
**Since:** 1.6

- MBeanAttributeInfo

```java
public MBeanAttributeInfo​(
String
name,

String
description,

Method
getter,

Method
setter)
throws
IntrospectionException
```

This constructor takes the name of a simple attribute, and Method
objects for reading and writing the attribute. The

Descriptor

of the constructed object will include fields contributed by any
annotations on the

Method

objects that contain the

DescriptorKey

meta-annotation.

**Parameters:** name

- The programmatic name of the attribute.
**Parameters:** description

- A human readable description of the attribute.
**Parameters:** getter

- The method used for reading the attribute value.
May be null if the property is write-only.
**Parameters:** setter

- The method used for writing the attribute value.
May be null if the attribute is read-only.
**Throws:** IntrospectionException

- There is a consistency
problem in the definition of this attribute.

---

#### Constructor Detail

MBeanAttributeInfo

```java
public MBeanAttributeInfo​(
String
name,

String
type,

String
description,
boolean isReadable,
boolean isWritable,
boolean isIs)
```

Constructs an

MBeanAttributeInfo

object.

**Parameters:** name

- The name of the attribute.
**Parameters:** type

- The type or class name of the attribute.
**Parameters:** description

- A human readable description of the attribute.
**Parameters:** isReadable

- True if the attribute has a getter method, false otherwise.
**Parameters:** isWritable

- True if the attribute has a setter method, false otherwise.
**Parameters:** isIs

- True if this attribute has an "is" getter, false otherwise.
**Throws:** IllegalArgumentException

- if

isIs

is true but

isReadable

is not, or if

isIs

is true and

type

is not

boolean

or

java.lang.Boolean

.
(New code should always use

boolean

rather than

java.lang.Boolean

.)

---

#### MBeanAttributeInfo

public MBeanAttributeInfo​(

String

name,

String

type,

String

description,
boolean isReadable,
boolean isWritable,
boolean isIs)

Constructs an

MBeanAttributeInfo

object.

MBeanAttributeInfo

```java
public MBeanAttributeInfo​(
String
name,

String
type,

String
description,
boolean isReadable,
boolean isWritable,
boolean isIs,

Descriptor
descriptor)
```

Constructs an

MBeanAttributeInfo

object.

**Parameters:** name

- The name of the attribute.
**Parameters:** type

- The type or class name of the attribute.
**Parameters:** description

- A human readable description of the attribute.
**Parameters:** isReadable

- True if the attribute has a getter method, false otherwise.
**Parameters:** isWritable

- True if the attribute has a setter method, false otherwise.
**Parameters:** isIs

- True if this attribute has an "is" getter, false otherwise.
**Parameters:** descriptor

- The descriptor for the attribute. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

isIs

is true but

isReadable

is not, or if

isIs

is true and

type

is not

boolean

or

java.lang.Boolean

.
(New code should always use

boolean

rather than

java.lang.Boolean

.)
**Since:** 1.6

---

#### MBeanAttributeInfo

public MBeanAttributeInfo​(

String

name,

String

type,

String

description,
boolean isReadable,
boolean isWritable,
boolean isIs,

Descriptor

descriptor)

Constructs an

MBeanAttributeInfo

object.

MBeanAttributeInfo

```java
public MBeanAttributeInfo​(
String
name,

String
description,

Method
getter,

Method
setter)
throws
IntrospectionException
```

This constructor takes the name of a simple attribute, and Method
objects for reading and writing the attribute. The

Descriptor

of the constructed object will include fields contributed by any
annotations on the

Method

objects that contain the

DescriptorKey

meta-annotation.

**Parameters:** name

- The programmatic name of the attribute.
**Parameters:** description

- A human readable description of the attribute.
**Parameters:** getter

- The method used for reading the attribute value.
May be null if the property is write-only.
**Parameters:** setter

- The method used for writing the attribute value.
May be null if the attribute is read-only.
**Throws:** IntrospectionException

- There is a consistency
problem in the definition of this attribute.

---

#### MBeanAttributeInfo

public MBeanAttributeInfo​(

String

name,

String

description,

Method

getter,

Method

setter)
throws

IntrospectionException

This constructor takes the name of a simple attribute, and Method
objects for reading and writing the attribute. The

Descriptor

of the constructed object will include fields contributed by any
annotations on the

Method

objects that contain the

DescriptorKey

meta-annotation.

Method Detail

- clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getType

```java
public
String
getType()
```

Returns the class name of the attribute.

**Returns:** the class name.

- isReadable

```java
public boolean isReadable()
```

Whether the value of the attribute can be read.

**Returns:** True if the attribute can be read, false otherwise.

- isWritable

```java
public boolean isWritable()
```

Whether new values can be written to the attribute.

**Returns:** True if the attribute can be written to, false otherwise.

- isIs

```java
public boolean isIs()
```

Indicates if this attribute has an "is" getter.

**Returns:** true if this attribute has an "is" getter.

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanAttributeInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanAttributeInfo such
that its

MBeanFeatureInfo.getName()

,

getType()

,

MBeanFeatureInfo.getDescription()

,

isReadable()

,

isWritable()

, and

isIs()

values are equal (not
necessarily identical) to those of this MBeanAttributeInfo.
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

getType

```java
public
String
getType()
```

Returns the class name of the attribute.

**Returns:** the class name.

---

#### getType

public

String

getType()

Returns the class name of the attribute.

isReadable

```java
public boolean isReadable()
```

Whether the value of the attribute can be read.

**Returns:** True if the attribute can be read, false otherwise.

---

#### isReadable

public boolean isReadable()

Whether the value of the attribute can be read.

isWritable

```java
public boolean isWritable()
```

Whether new values can be written to the attribute.

**Returns:** True if the attribute can be written to, false otherwise.

---

#### isWritable

public boolean isWritable()

Whether new values can be written to the attribute.

isIs

```java
public boolean isIs()
```

Indicates if this attribute has an "is" getter.

**Returns:** true if this attribute has an "is" getter.

---

#### isIs

public boolean isIs()

Indicates if this attribute has an "is" getter.

equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanAttributeInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanAttributeInfo such
that its

MBeanFeatureInfo.getName()

,

getType()

,

MBeanFeatureInfo.getDescription()

,

isReadable()

,

isWritable()

, and

isIs()

values are equal (not
necessarily identical) to those of this MBeanAttributeInfo.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compare this MBeanAttributeInfo to another.

---

