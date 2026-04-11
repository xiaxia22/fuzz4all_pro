# Class MBeanConstructorInfo

**Source:** `java.management\javax\management\MBeanConstructorInfo.html`

### Class Description

```java
public class
MBeanConstructorInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

Describes a constructor exposed by an MBean. Instances of this
class are immutable. Subclasses may be mutable but this is not
recommended.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanConstructorInfo​(
String
description,

Constructor
<?> constructor)

Constructs an

MBeanConstructorInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:**
- description

- A human readable description of the operation.
- constructor

- The

java.lang.reflect.Constructor

object describing the MBean constructor.

---

#### public MBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature)

Constructs an

MBeanConstructorInfo

object.

**Parameters:**
- name

- The name of the constructor.
- signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the constructor. This
may be null with the same effect as a zero-length array.
- description

- A human readable description of the constructor.

---

#### public MBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

Descriptor
descriptor)

Constructs an

MBeanConstructorInfo

object.

**Parameters:**
- name

- The name of the constructor.
- signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the constructor. This
may be null with the same effect as a zero-length array.
- description

- A human readable description of the constructor.
- descriptor

- The descriptor for the constructor. This may be null
which is equivalent to an empty descriptor.

**Since:**
- 1.6

---

### Method Details

#### public
Object
clone()

Returns a shallow clone of this instance. The clone is
obtained by simply calling

super.clone()

, thus calling
the default native shallow cloning mechanism implemented by

Object.clone()

. No deeper cloning of any internal
field is made.

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
MBeanParameterInfo
[] getSignature()

Returns the list of parameters for this constructor. Each
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

#### public boolean equals​(
Object
o)

Compare this MBeanConstructorInfo to another.

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

is an MBeanConstructorInfo such
that its

MBeanFeatureInfo.getName()

,

MBeanFeatureInfo.getDescription()

,

getSignature()

, and

MBeanFeatureInfo.getDescriptor()

values are equal (not necessarily
identical) to those of this MBeanConstructorInfo. Two
signature arrays are equal if their elements are pairwise
equal.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class MBeanConstructorInfo

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanConstructorInfo

javax.management.MBeanFeatureInfo

- javax.management.MBeanConstructorInfo

javax.management.MBeanConstructorInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

**Direct Known Subclasses:** ModelMBeanConstructorInfo

,

OpenMBeanConstructorInfoSupport

```java
public class
MBeanConstructorInfo

extends
MBeanFeatureInfo

implements
Cloneable
```

Describes a constructor exposed by an MBean. Instances of this
class are immutable. Subclasses may be mutable but this is not
recommended.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanConstructorInfo

extends

MBeanFeatureInfo

implements

Cloneable

Describes a constructor exposed by an MBean. Instances of this
class are immutable. Subclasses may be mutable but this is not
recommended.

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

MBeanConstructorInfo

​(

String

description,

Constructor

<?> constructor)

Constructs an

MBeanConstructorInfo

object.

MBeanConstructorInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature)

Constructs an

MBeanConstructorInfo

object.

MBeanConstructorInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

Descriptor

descriptor)

Constructs an

MBeanConstructorInfo

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

Compare this MBeanConstructorInfo to another.

MBeanParameterInfo

[]

getSignature

()

Returns the list of parameters for this constructor.

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

MBeanConstructorInfo

​(

String

description,

Constructor

<?> constructor)

Constructs an

MBeanConstructorInfo

object.

MBeanConstructorInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature)

Constructs an

MBeanConstructorInfo

object.

MBeanConstructorInfo

​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

Descriptor

descriptor)

Constructs an

MBeanConstructorInfo

object.

---

#### Constructor Summary

Constructs an

MBeanConstructorInfo

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

Compare this MBeanConstructorInfo to another.

MBeanParameterInfo

[]

getSignature

()

Returns the list of parameters for this constructor.

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

Compare this MBeanConstructorInfo to another.

Returns the list of parameters for this constructor.

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

- MBeanConstructorInfo

```java
public MBeanConstructorInfo​(
String
description,

Constructor
<?> constructor)
```

Constructs an

MBeanConstructorInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** description

- A human readable description of the operation.
**Parameters:** constructor

- The

java.lang.reflect.Constructor

object describing the MBean constructor.

- MBeanConstructorInfo

```java
public MBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature)
```

Constructs an

MBeanConstructorInfo

object.

**Parameters:** name

- The name of the constructor.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the constructor. This
may be null with the same effect as a zero-length array.
**Parameters:** description

- A human readable description of the constructor.

- MBeanConstructorInfo

```java
public MBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

Descriptor
descriptor)
```

Constructs an

MBeanConstructorInfo

object.

**Parameters:** name

- The name of the constructor.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the constructor. This
may be null with the same effect as a zero-length array.
**Parameters:** description

- A human readable description of the constructor.
**Parameters:** descriptor

- The descriptor for the constructor. This may be null
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

Returns a shallow clone of this instance. The clone is
obtained by simply calling

super.clone()

, thus calling
the default native shallow cloning mechanism implemented by

Object.clone()

. No deeper cloning of any internal
field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getSignature

```java
public
MBeanParameterInfo
[] getSignature()
```

Returns the list of parameters for this constructor. Each
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

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanConstructorInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanConstructorInfo such
that its

MBeanFeatureInfo.getName()

,

MBeanFeatureInfo.getDescription()

,

getSignature()

, and

MBeanFeatureInfo.getDescriptor()

values are equal (not necessarily
identical) to those of this MBeanConstructorInfo. Two
signature arrays are equal if their elements are pairwise
equal.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- MBeanConstructorInfo

```java
public MBeanConstructorInfo​(
String
description,

Constructor
<?> constructor)
```

Constructs an

MBeanConstructorInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** description

- A human readable description of the operation.
**Parameters:** constructor

- The

java.lang.reflect.Constructor

object describing the MBean constructor.

- MBeanConstructorInfo

```java
public MBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature)
```

Constructs an

MBeanConstructorInfo

object.

**Parameters:** name

- The name of the constructor.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the constructor. This
may be null with the same effect as a zero-length array.
**Parameters:** description

- A human readable description of the constructor.

- MBeanConstructorInfo

```java
public MBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

Descriptor
descriptor)
```

Constructs an

MBeanConstructorInfo

object.

**Parameters:** name

- The name of the constructor.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the constructor. This
may be null with the same effect as a zero-length array.
**Parameters:** description

- A human readable description of the constructor.
**Parameters:** descriptor

- The descriptor for the constructor. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

---

#### Constructor Detail

MBeanConstructorInfo

```java
public MBeanConstructorInfo​(
String
description,

Constructor
<?> constructor)
```

Constructs an

MBeanConstructorInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

**Parameters:** description

- A human readable description of the operation.
**Parameters:** constructor

- The

java.lang.reflect.Constructor

object describing the MBean constructor.

---

#### MBeanConstructorInfo

public MBeanConstructorInfo​(

String

description,

Constructor

<?> constructor)

Constructs an

MBeanConstructorInfo

object. The

Descriptor

of the constructed object will include
fields contributed by any annotations on the

Constructor

object that contain the

DescriptorKey

meta-annotation.

MBeanConstructorInfo

```java
public MBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature)
```

Constructs an

MBeanConstructorInfo

object.

**Parameters:** name

- The name of the constructor.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the constructor. This
may be null with the same effect as a zero-length array.
**Parameters:** description

- A human readable description of the constructor.

---

#### MBeanConstructorInfo

public MBeanConstructorInfo​(

String

name,

String

description,

MBeanParameterInfo

[] signature)

Constructs an

MBeanConstructorInfo

object.

MBeanConstructorInfo

```java
public MBeanConstructorInfo​(
String
name,

String
description,

MBeanParameterInfo
[] signature,

Descriptor
descriptor)
```

Constructs an

MBeanConstructorInfo

object.

**Parameters:** name

- The name of the constructor.
**Parameters:** signature

-

MBeanParameterInfo

objects
describing the parameters(arguments) of the constructor. This
may be null with the same effect as a zero-length array.
**Parameters:** description

- A human readable description of the constructor.
**Parameters:** descriptor

- The descriptor for the constructor. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

---

#### MBeanConstructorInfo

public MBeanConstructorInfo​(

String

name,

String

description,

MBeanParameterInfo

[] signature,

Descriptor

descriptor)

Constructs an

MBeanConstructorInfo

object.

Method Detail

- clone

```java
public
Object
clone()
```

Returns a shallow clone of this instance. The clone is
obtained by simply calling

super.clone()

, thus calling
the default native shallow cloning mechanism implemented by

Object.clone()

. No deeper cloning of any internal
field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- getSignature

```java
public
MBeanParameterInfo
[] getSignature()
```

Returns the list of parameters for this constructor. Each
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

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanConstructorInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanConstructorInfo such
that its

MBeanFeatureInfo.getName()

,

MBeanFeatureInfo.getDescription()

,

getSignature()

, and

MBeanFeatureInfo.getDescriptor()

values are equal (not necessarily
identical) to those of this MBeanConstructorInfo. Two
signature arrays are equal if their elements are pairwise
equal.
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

Returns a shallow clone of this instance. The clone is
obtained by simply calling

super.clone()

, thus calling
the default native shallow cloning mechanism implemented by

Object.clone()

. No deeper cloning of any internal
field is made.

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

Returns a shallow clone of this instance. The clone is
obtained by simply calling

super.clone()

, thus calling
the default native shallow cloning mechanism implemented by

Object.clone()

. No deeper cloning of any internal
field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

Returns a shallow clone of this instance. The clone is
obtained by simply calling

super.clone()

, thus calling
the default native shallow cloning mechanism implemented by

Object.clone()

. No deeper cloning of any internal
field is made.

Since this class is immutable, cloning is chiefly of
interest to subclasses.

getSignature

```java
public
MBeanParameterInfo
[] getSignature()
```

Returns the list of parameters for this constructor. Each
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

Returns the list of parameters for this constructor. Each
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

Returns the list of parameters for this constructor. Each
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

equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanConstructorInfo to another.

**Overrides:** equals

in class

MBeanFeatureInfo
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanConstructorInfo such
that its

MBeanFeatureInfo.getName()

,

MBeanFeatureInfo.getDescription()

,

getSignature()

, and

MBeanFeatureInfo.getDescriptor()

values are equal (not necessarily
identical) to those of this MBeanConstructorInfo. Two
signature arrays are equal if their elements are pairwise
equal.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compare this MBeanConstructorInfo to another.

---

