# Class MBeanParameterInfo

**Source:** `java.management\javax\management\MBeanParameterInfo.html`

### Class Description

```java
public class
MBeanParameterInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

Describes an argument of an operation exposed by an MBean.
Instances of this class are immutable. Subclasses may be mutable
but this is not recommended.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanParameterInfo​(
String
name,

String
type,

String
description)

Constructs an

MBeanParameterInfo

object.

**Parameters:**
- name

- The name of the data
- type

- The type or class name of the data
- description

- A human readable description of the data. Optional.

---

#### public MBeanParameterInfo​(
String
name,

String
type,

String
description,

Descriptor
descriptor)

Constructs an

MBeanParameterInfo

object.

**Parameters:**
- name

- The name of the data
- type

- The type or class name of the data
- description

- A human readable description of the data. Optional.
- descriptor

- The descriptor for the operation. This may be null
which is equivalent to an empty descriptor.

**Since:**
- 1.6

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

Returns the type or class name of the data.

**Returns:**
- the type string.

---

#### public boolean equals​(
Object
o)

Compare this MBeanParameterInfo to another.

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

is an MBeanParameterInfo such
that its

MBeanFeatureInfo.getName()

,

getType()

,

MBeanFeatureInfo.getDescriptor()

, and

MBeanFeatureInfo.getDescription()

values are equal (not necessarily identical)
to those of this MBeanParameterInfo.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class MBeanParameterInfo

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanParameterInfo

javax.management.MBeanFeatureInfo

- javax.management.MBeanParameterInfo

javax.management.MBeanParameterInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

**Direct Known Subclasses:** OpenMBeanParameterInfoSupport

```java
public class
MBeanParameterInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

Describes an argument of an operation exposed by an MBean.
Instances of this class are immutable. Subclasses may be mutable
but this is not recommended.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanParameterInfo

extends

MBeanFeatureInfo

implements

Cloneable

Describes an argument of an operation exposed by an MBean.
Instances of this class are immutable. Subclasses may be mutable
but this is not recommended.

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

MBeanParameterInfo

​(

String

name,

String

type,

String

description)

Constructs an

MBeanParameterInfo

object.

MBeanParameterInfo

​(

String

name,

String

type,

String

description,

Descriptor

descriptor)

Constructs an

MBeanParameterInfo

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

Compare this MBeanParameterInfo to another.

String

getType

()

Returns the type or class name of the data.

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

MBeanParameterInfo

​(

String

name,

String

type,

String

description)

Constructs an

MBeanParameterInfo

object.

MBeanParameterInfo

​(

String

name,

String

type,

String

description,

Descriptor

descriptor)

Constructs an

MBeanParameterInfo

object.

---

#### Constructor Summary

Constructs an

MBeanParameterInfo

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

Compare this MBeanParameterInfo to another.

String

getType

()

Returns the type or class name of the data.

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

Compare this MBeanParameterInfo to another.

Returns the type or class name of the data.

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

- MBeanParameterInfo

```java
public MBeanParameterInfo​(
String
name,

String
type,

String
description)
```

Constructs an

MBeanParameterInfo

object.

**Parameters:** name

- The name of the data
**Parameters:** type

- The type or class name of the data
**Parameters:** description

- A human readable description of the data. Optional.

- MBeanParameterInfo

```java
public MBeanParameterInfo​(
String
name,

String
type,

String
description,

Descriptor
descriptor)
```

Constructs an

MBeanParameterInfo

object.

**Parameters:** name

- The name of the data
**Parameters:** type

- The type or class name of the data
**Parameters:** description

- A human readable description of the data. Optional.
**Parameters:** descriptor

- The descriptor for the operation. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

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

Returns the type or class name of the data.

**Returns:** the type string.

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanParameterInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanParameterInfo such
that its

MBeanFeatureInfo.getName()

,

getType()

,

MBeanFeatureInfo.getDescriptor()

, and

MBeanFeatureInfo.getDescription()

values are equal (not necessarily identical)
to those of this MBeanParameterInfo.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- MBeanParameterInfo

```java
public MBeanParameterInfo​(
String
name,

String
type,

String
description)
```

Constructs an

MBeanParameterInfo

object.

**Parameters:** name

- The name of the data
**Parameters:** type

- The type or class name of the data
**Parameters:** description

- A human readable description of the data. Optional.

- MBeanParameterInfo

```java
public MBeanParameterInfo​(
String
name,

String
type,

String
description,

Descriptor
descriptor)
```

Constructs an

MBeanParameterInfo

object.

**Parameters:** name

- The name of the data
**Parameters:** type

- The type or class name of the data
**Parameters:** description

- A human readable description of the data. Optional.
**Parameters:** descriptor

- The descriptor for the operation. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

---

#### Constructor Detail

MBeanParameterInfo

```java
public MBeanParameterInfo​(
String
name,

String
type,

String
description)
```

Constructs an

MBeanParameterInfo

object.

**Parameters:** name

- The name of the data
**Parameters:** type

- The type or class name of the data
**Parameters:** description

- A human readable description of the data. Optional.

---

#### MBeanParameterInfo

public MBeanParameterInfo​(

String

name,

String

type,

String

description)

Constructs an

MBeanParameterInfo

object.

MBeanParameterInfo

```java
public MBeanParameterInfo​(
String
name,

String
type,

String
description,

Descriptor
descriptor)
```

Constructs an

MBeanParameterInfo

object.

**Parameters:** name

- The name of the data
**Parameters:** type

- The type or class name of the data
**Parameters:** description

- A human readable description of the data. Optional.
**Parameters:** descriptor

- The descriptor for the operation. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

---

#### MBeanParameterInfo

public MBeanParameterInfo​(

String

name,

String

type,

String

description,

Descriptor

descriptor)

Constructs an

MBeanParameterInfo

object.

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

Returns the type or class name of the data.

**Returns:** the type string.

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanParameterInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanParameterInfo such
that its

MBeanFeatureInfo.getName()

,

getType()

,

MBeanFeatureInfo.getDescriptor()

, and

MBeanFeatureInfo.getDescription()

values are equal (not necessarily identical)
to those of this MBeanParameterInfo.
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

Returns the type or class name of the data.

**Returns:** the type string.

---

#### getType

public

String

getType()

Returns the type or class name of the data.

equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanParameterInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanParameterInfo such
that its

MBeanFeatureInfo.getName()

,

getType()

,

MBeanFeatureInfo.getDescriptor()

, and

MBeanFeatureInfo.getDescription()

values are equal (not necessarily identical)
to those of this MBeanParameterInfo.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compare this MBeanParameterInfo to another.

---

