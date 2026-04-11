# Class MBeanOperationInfo

**Source:** `java.management\javax\management\MBeanOperationInfo.html`

### Class Description

```java
public class
MBeanOperationInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

Describes a management operation exposed by an MBean. Instances of
this class are immutable. Subclasses may be mutable but this is
not recommended.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

---

### Field Details

#### public static final int INFO

Indicates that the operation is read-like:
it returns information but does not change any state.

**See Also:**
- Constant Field Values

---

#### public static final int ACTION

Indicates that the operation is write-like: it has an effect but does
not return any information from the MBean.

**See Also:**
- Constant Field Values

---

#### public static final int ACTION_INFO

Indicates that the operation is both read-like and write-like:
it has an effect, and it also returns information from the MBean.

**See Also:**
- Constant Field Values

---

#### public static final int UNKNOWN

Indicates that the impact of the operation is unknown or cannot be
expressed using one of the other values.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public MBeanOperationInfo​(
String
description,

Method
method)

Constructs an

MBeanOperationInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Method

object that contain the

DescriptorKey

meta-annotation.

**Parameters:**
- method

- The

java.lang.reflect.Method

object
describing the MBean operation.
- description

- A human readable description of the operation.

---

#### public MBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact)

Constructs an

MBeanOperationInfo

object.

**Parameters:**
- name

- The name of the method.
- description

- A human readable description of the operation.
- signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the method. This may be
null with the same effect as a zero-length array.
- type

- The type of the method's return value.
- impact

- The impact of the method, one of

INFO

,

ACTION

,

ACTION_INFO

,

UNKNOWN

.

---

#### public MBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact,

Descriptor
descriptor)

Constructs an

MBeanOperationInfo

object.

**Parameters:**
- name

- The name of the method.
- description

- A human readable description of the operation.
- signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the method. This may be
null with the same effect as a zero-length array.
- type

- The type of the method's return value.
- impact

- The impact of the method, one of

INFO

,

ACTION

,

ACTION_INFO

,

UNKNOWN

.
- descriptor

- The descriptor for the operation. This may be null
which is equivalent to an empty descriptor.

**Throws:**
- IllegalArgumentException

- if

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

or

UNKNOWN

.

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

Since this class is immutable, cloning is chiefly of interest
to subclasses.

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
getReturnType()

Returns the type of the method's return value.

**Returns:**
- the return type.

---

#### public
MBeanParameterInfo
[] getSignature()

Returns the list of parameters for this operation. Each
parameter is described by an

MBeanParameterInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanParameterInfo

objects but
that each referenced

MBeanParameterInfo

object is
not copied.

**Returns:**
- An array of

MBeanParameterInfo

objects.

---

#### public int getImpact()

Returns the impact of the method, one of

INFO, ACTION, ACTION_INFO, UNKNOWN

.

**Returns:**
- the impact code.

---

#### public boolean equals​(
Object
o)

Compare this MBeanOperationInfo to another.

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

is an MBeanOperationInfo such
that its

MBeanFeatureInfo.getName()

,

getReturnType()

,

MBeanFeatureInfo.getDescription()

,

getImpact()

,

MBeanFeatureInfo.getDescriptor()

and

getSignature()

values are equal (not necessarily identical)
to those of this MBeanConstructorInfo. Two signature arrays
are equal if their elements are pairwise equal.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class MBeanOperationInfo

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanOperationInfo

javax.management.MBeanFeatureInfo

- javax.management.MBeanOperationInfo

javax.management.MBeanOperationInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

**Direct Known Subclasses:** ModelMBeanOperationInfo

,

OpenMBeanOperationInfoSupport

```java
public class
MBeanOperationInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

Describes a management operation exposed by an MBean. Instances of
this class are immutable. Subclasses may be mutable but this is
not recommended.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanOperationInfo

extends

MBeanFeatureInfo

implements

Cloneable

Describes a management operation exposed by an MBean. Instances of
this class are immutable. Subclasses may be mutable but this is
not recommended.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ACTION

Indicates that the operation is write-like: it has an effect but does
not return any information from the MBean.

static int

ACTION_INFO

Indicates that the operation is both read-like and write-like:
it has an effect, and it also returns information from the MBean.

static int

INFO

Indicates that the operation is read-like:
it returns information but does not change any state.

static int

UNKNOWN

Indicates that the impact of the operation is unknown or cannot be
expressed using one of the other values.

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

MBeanOperationInfo

​(

String

description,

Method

method)

Constructs an

MBeanOperationInfo

object.

MBeanOperationInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact)

Constructs an

MBeanOperationInfo

object.

MBeanOperationInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact,

Descriptor

descriptor)

Constructs an

MBeanOperationInfo

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

Compare this MBeanOperationInfo to another.

int

getImpact

()

Returns the impact of the method, one of

INFO, ACTION, ACTION_INFO, UNKNOWN

.

String

getReturnType

()

Returns the type of the method's return value.

MBeanParameterInfo

[]

getSignature

()

Returns the list of parameters for this operation.

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

Fields

Modifier and Type

Field

Description

static int

ACTION

Indicates that the operation is write-like: it has an effect but does
not return any information from the MBean.

static int

ACTION_INFO

Indicates that the operation is both read-like and write-like:
it has an effect, and it also returns information from the MBean.

static int

INFO

Indicates that the operation is read-like:
it returns information but does not change any state.

static int

UNKNOWN

Indicates that the impact of the operation is unknown or cannot be
expressed using one of the other values.

- Fields declared in class javax.management.

MBeanFeatureInfo

description

,

name

---

#### Field Summary

Indicates that the operation is write-like: it has an effect but does
not return any information from the MBean.

Indicates that the operation is both read-like and write-like:
it has an effect, and it also returns information from the MBean.

Indicates that the operation is read-like:
it returns information but does not change any state.

Indicates that the impact of the operation is unknown or cannot be
expressed using one of the other values.

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

MBeanOperationInfo

​(

String

description,

Method

method)

Constructs an

MBeanOperationInfo

object.

MBeanOperationInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact)

Constructs an

MBeanOperationInfo

object.

MBeanOperationInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact,

Descriptor

descriptor)

Constructs an

MBeanOperationInfo

object.

---

#### Constructor Summary

Constructs an

MBeanOperationInfo

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

Compare this MBeanOperationInfo to another.

int

getImpact

()

Returns the impact of the method, one of

INFO, ACTION, ACTION_INFO, UNKNOWN

.

String

getReturnType

()

Returns the type of the method's return value.

MBeanParameterInfo

[]

getSignature

()

Returns the list of parameters for this operation.

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

Compare this MBeanOperationInfo to another.

Returns the impact of the method, one of

INFO, ACTION, ACTION_INFO, UNKNOWN

.

Returns the type of the method's return value.

Returns the list of parameters for this operation.

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

============ FIELD DETAIL ===========

- Field Detail

- INFO

```java
public static final int INFO
```

Indicates that the operation is read-like:
it returns information but does not change any state.

**See Also:** Constant Field Values

- ACTION

```java
public static final int ACTION
```

Indicates that the operation is write-like: it has an effect but does
not return any information from the MBean.

**See Also:** Constant Field Values

- ACTION_INFO

```java
public static final int ACTION_INFO
```

Indicates that the operation is both read-like and write-like:
it has an effect, and it also returns information from the MBean.

**See Also:** Constant Field Values

- UNKNOWN

```java
public static final int UNKNOWN
```

Indicates that the impact of the operation is unknown or cannot be
expressed using one of the other values.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MBeanOperationInfo

```java
public MBeanOperationInfo​(
String
description,

Method
method)
```

Constructs an

MBeanOperationInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Method

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** method

- The

java.lang.reflect.Method

object
describing the MBean operation.
**Parameters:** description

- A human readable description of the operation.

- MBeanOperationInfo

```java
public MBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact)
```

Constructs an

MBeanOperationInfo

object.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the method. This may be
null with the same effect as a zero-length array.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of

INFO

,

ACTION

,

ACTION_INFO

,

UNKNOWN

.

- MBeanOperationInfo

```java
public MBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact,

Descriptor
descriptor)
```

Constructs an

MBeanOperationInfo

object.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the method. This may be
null with the same effect as a zero-length array.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of

INFO

,

ACTION

,

ACTION_INFO

,

UNKNOWN

.
**Parameters:** descriptor

- The descriptor for the operation. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

or

UNKNOWN

.
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

Since this class is immutable, cloning is chiefly of interest
to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getReturnType

```java
public
String
getReturnType()
```

Returns the type of the method's return value.

**Returns:** the return type.

- getSignature

```java
public
MBeanParameterInfo
[] getSignature()
```

Returns the list of parameters for this operation. Each
parameter is described by an

MBeanParameterInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanParameterInfo

objects but
that each referenced

MBeanParameterInfo

object is
not copied.

**Returns:** An array of

MBeanParameterInfo

objects.

- getImpact

```java
public int getImpact()
```

Returns the impact of the method, one of

INFO, ACTION, ACTION_INFO, UNKNOWN

.

**Returns:** the impact code.

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanOperationInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanOperationInfo such
that its

MBeanFeatureInfo.getName()

,

getReturnType()

,

MBeanFeatureInfo.getDescription()

,

getImpact()

,

MBeanFeatureInfo.getDescriptor()

and

getSignature()

values are equal (not necessarily identical)
to those of this MBeanConstructorInfo. Two signature arrays
are equal if their elements are pairwise equal.
**See Also:** Object.hashCode()

,

HashMap

Field Detail

- INFO

```java
public static final int INFO
```

Indicates that the operation is read-like:
it returns information but does not change any state.

**See Also:** Constant Field Values

- ACTION

```java
public static final int ACTION
```

Indicates that the operation is write-like: it has an effect but does
not return any information from the MBean.

**See Also:** Constant Field Values

- ACTION_INFO

```java
public static final int ACTION_INFO
```

Indicates that the operation is both read-like and write-like:
it has an effect, and it also returns information from the MBean.

**See Also:** Constant Field Values

- UNKNOWN

```java
public static final int UNKNOWN
```

Indicates that the impact of the operation is unknown or cannot be
expressed using one of the other values.

**See Also:** Constant Field Values

---

#### Field Detail

INFO

```java
public static final int INFO
```

Indicates that the operation is read-like:
it returns information but does not change any state.

**See Also:** Constant Field Values

---

#### INFO

public static final int INFO

Indicates that the operation is read-like:
it returns information but does not change any state.

ACTION

```java
public static final int ACTION
```

Indicates that the operation is write-like: it has an effect but does
not return any information from the MBean.

**See Also:** Constant Field Values

---

#### ACTION

public static final int ACTION

Indicates that the operation is write-like: it has an effect but does
not return any information from the MBean.

ACTION_INFO

```java
public static final int ACTION_INFO
```

Indicates that the operation is both read-like and write-like:
it has an effect, and it also returns information from the MBean.

**See Also:** Constant Field Values

---

#### ACTION_INFO

public static final int ACTION_INFO

Indicates that the operation is both read-like and write-like:
it has an effect, and it also returns information from the MBean.

UNKNOWN

```java
public static final int UNKNOWN
```

Indicates that the impact of the operation is unknown or cannot be
expressed using one of the other values.

**See Also:** Constant Field Values

---

#### UNKNOWN

public static final int UNKNOWN

Indicates that the impact of the operation is unknown or cannot be
expressed using one of the other values.

Constructor Detail

- MBeanOperationInfo

```java
public MBeanOperationInfo​(
String
description,

Method
method)
```

Constructs an

MBeanOperationInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Method

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** method

- The

java.lang.reflect.Method

object
describing the MBean operation.
**Parameters:** description

- A human readable description of the operation.

- MBeanOperationInfo

```java
public MBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact)
```

Constructs an

MBeanOperationInfo

object.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the method. This may be
null with the same effect as a zero-length array.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of

INFO

,

ACTION

,

ACTION_INFO

,

UNKNOWN

.

- MBeanOperationInfo

```java
public MBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact,

Descriptor
descriptor)
```

Constructs an

MBeanOperationInfo

object.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the method. This may be
null with the same effect as a zero-length array.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of

INFO

,

ACTION

,

ACTION_INFO

,

UNKNOWN

.
**Parameters:** descriptor

- The descriptor for the operation. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

or

UNKNOWN

.
**Since:** 1.6

---

#### Constructor Detail

MBeanOperationInfo

```java
public MBeanOperationInfo​(
String
description,

Method
method)
```

Constructs an

MBeanOperationInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Method

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** method

- The

java.lang.reflect.Method

object
describing the MBean operation.
**Parameters:** description

- A human readable description of the operation.

---

#### MBeanOperationInfo

public MBeanOperationInfo​(

String

description,

Method

method)

Constructs an

MBeanOperationInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Method

object that contain the

DescriptorKey

meta-annotation.

MBeanOperationInfo

```java
public MBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact)
```

Constructs an

MBeanOperationInfo

object.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the method. This may be
null with the same effect as a zero-length array.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of

INFO

,

ACTION

,

ACTION_INFO

,

UNKNOWN

.

---

#### MBeanOperationInfo

public MBeanOperationInfo​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact)

Constructs an

MBeanOperationInfo

object.

MBeanOperationInfo

```java
public MBeanOperationInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

String
type,
int impact,

Descriptor
descriptor)
```

Constructs an

MBeanOperationInfo

object.

**Parameters:** name

- The name of the method.
**Parameters:** description

- A human readable description of the operation.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the method. This may be
null with the same effect as a zero-length array.
**Parameters:** type

- The type of the method's return value.
**Parameters:** impact

- The impact of the method, one of

INFO

,

ACTION

,

ACTION_INFO

,

UNKNOWN

.
**Parameters:** descriptor

- The descriptor for the operation. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

impact

is not one of

ACTION

,

ACTION_INFO

,

INFO

or

UNKNOWN

.
**Since:** 1.6

---

#### MBeanOperationInfo

public MBeanOperationInfo​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

String

type,
int impact,

Descriptor

descriptor)

Constructs an

MBeanOperationInfo

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

Since this class is immutable, cloning is chiefly of interest
to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getReturnType

```java
public
String
getReturnType()
```

Returns the type of the method's return value.

**Returns:** the return type.

- getSignature

```java
public
MBeanParameterInfo
[] getSignature()
```

Returns the list of parameters for this operation. Each
parameter is described by an

MBeanParameterInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanParameterInfo

objects but
that each referenced

MBeanParameterInfo

object is
not copied.

**Returns:** An array of

MBeanParameterInfo

objects.

- getImpact

```java
public int getImpact()
```

Returns the impact of the method, one of

INFO, ACTION, ACTION_INFO, UNKNOWN

.

**Returns:** the impact code.

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanOperationInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanOperationInfo such
that its

MBeanFeatureInfo.getName()

,

getReturnType()

,

MBeanFeatureInfo.getDescription()

,

getImpact()

,

MBeanFeatureInfo.getDescriptor()

and

getSignature()

values are equal (not necessarily identical)
to those of this MBeanConstructorInfo. Two signature arrays
are equal if their elements are pairwise equal.
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

Since this class is immutable, cloning is chiefly of interest
to subclasses.

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

Since this class is immutable, cloning is chiefly of interest
to subclasses.

Returns a shallow clone of this instance.
The clone is obtained by simply calling

super.clone()

,
thus calling the default native shallow cloning mechanism
implemented by

Object.clone()

.
No deeper cloning of any internal field is made.

Since this class is immutable, cloning is chiefly of interest
to subclasses.

getReturnType

```java
public
String
getReturnType()
```

Returns the type of the method's return value.

**Returns:** the return type.

---

#### getReturnType

public

String

getReturnType()

Returns the type of the method's return value.

getSignature

```java
public
MBeanParameterInfo
[] getSignature()
```

Returns the list of parameters for this operation. Each
parameter is described by an

MBeanParameterInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanParameterInfo

objects but
that each referenced

MBeanParameterInfo

object is
not copied.

**Returns:** An array of

MBeanParameterInfo

objects.

---

#### getSignature

public

MBeanParameterInfo

[] getSignature()

Returns the list of parameters for this operation. Each
parameter is described by an

MBeanParameterInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanParameterInfo

objects but
that each referenced

MBeanParameterInfo

object is
not copied.

Returns the list of parameters for this operation. Each
parameter is described by an

MBeanParameterInfo

object.

The returned array is a shallow copy of the internal array,
which means that it is a copy of the internal array of
references to the

MBeanParameterInfo

objects but
that each referenced

MBeanParameterInfo

object is
not copied.

getImpact

```java
public int getImpact()
```

Returns the impact of the method, one of

INFO, ACTION, ACTION_INFO, UNKNOWN

.

**Returns:** the impact code.

---

#### getImpact

public int getImpact()

Returns the impact of the method, one of

INFO, ACTION, ACTION_INFO, UNKNOWN

.

equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanOperationInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanOperationInfo such
that its

MBeanFeatureInfo.getName()

,

getReturnType()

,

MBeanFeatureInfo.getDescription()

,

getImpact()

,

MBeanFeatureInfo.getDescriptor()

and

getSignature()

values are equal (not necessarily identical)
to those of this MBeanConstructorInfo. Two signature arrays
are equal if their elements are pairwise equal.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compare this MBeanOperationInfo to another.

---

