# Class MBeanFeatureInfo

**Source:** `java.management\javax\management\MBeanFeatureInfo.html`

### Class Description

```java
public class
MBeanFeatureInfo

extends
Object

implements
Serializable
,
DescriptorRead
```

Provides general information for an MBean descriptor object.
The feature described can be an attribute, an operation, a
parameter, or a notification. Instances of this class are
immutable. Subclasses may be mutable but this is not
recommended.

**All Implemented Interfaces:** Serializable

,

DescriptorRead

---

### Field Details

#### protected
String
name

The name of the feature. It is recommended that subclasses call

getName()

rather than reading this field, and that they
not change it.

---

#### protected
String
description

The human-readable description of the feature. It is
recommended that subclasses call

getDescription()

rather
than reading this field, and that they not change it.

---

### Constructor Details

#### public MBeanFeatureInfo​(
String
name,

String
description)

Constructs an

MBeanFeatureInfo

object. This
constructor is equivalent to

MBeanFeatureInfo(name,
description, (Descriptor) null

.

**Parameters:**
- name

- The name of the feature.
- description

- A human readable description of the feature.

---

#### public MBeanFeatureInfo​(
String
name,

String
description,

Descriptor
descriptor)

Constructs an

MBeanFeatureInfo

object.

**Parameters:**
- name

- The name of the feature.
- description

- A human readable description of the feature.
- descriptor

- The descriptor for the feature. This may be null
which is equivalent to an empty descriptor.

**Since:**
- 1.6

---

### Method Details

#### public
String
getName()

Returns the name of the feature.

**Returns:**
- the name of the feature.

---

#### public
String
getDescription()

Returns the human-readable description of the feature.

**Returns:**
- the human-readable description of the feature.

---

#### public
Descriptor
getDescriptor()

Returns the descriptor for the feature. Changing the returned value
will have no affect on the original descriptor.

**Specified by:**
- getDescriptor

in interface

DescriptorRead

**Returns:**
- a descriptor that is either immutable or a copy of the original.

**Since:**
- 1.6

---

#### public boolean equals​(
Object
o)

Compare this MBeanFeatureInfo to another.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the object to compare to.

**Returns:**
- true if and only if

o

is an MBeanFeatureInfo such
that its

getName()

,

getDescription()

, and

getDescriptor()

values are equal (not necessarily identical) to those of this
MBeanFeatureInfo.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class MBeanFeatureInfo

java.lang.Object

- javax.management.MBeanFeatureInfo

javax.management.MBeanFeatureInfo

**All Implemented Interfaces:** Serializable

,

DescriptorRead

**Direct Known Subclasses:** MBeanAttributeInfo

,

MBeanConstructorInfo

,

MBeanNotificationInfo

,

MBeanOperationInfo

,

MBeanParameterInfo

```java
public class
MBeanFeatureInfo

extends
Object

implements
Serializable
,
DescriptorRead
```

Provides general information for an MBean descriptor object.
The feature described can be an attribute, an operation, a
parameter, or a notification. Instances of this class are
immutable. Subclasses may be mutable but this is not
recommended.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanFeatureInfo

extends

Object

implements

Serializable

,

DescriptorRead

Provides general information for an MBean descriptor object.
The feature described can be an attribute, an operation, a
parameter, or a notification. Instances of this class are
immutable. Subclasses may be mutable but this is not
recommended.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

description

The human-readable description of the feature.

protected

String

name

The name of the feature.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanFeatureInfo

​(

String

name,

String

description)

Constructs an

MBeanFeatureInfo

object.

MBeanFeatureInfo

​(

String

name,

String

description,

Descriptor

descriptor)

Constructs an

MBeanFeatureInfo

object.

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

Compare this MBeanFeatureInfo to another.

String

getDescription

()

Returns the human-readable description of the feature.

Descriptor

getDescriptor

()

Returns the descriptor for the feature.

String

getName

()

Returns the name of the feature.

- Methods declared in class java.lang.

Object

clone

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

String

description

The human-readable description of the feature.

protected

String

name

The name of the feature.

---

#### Field Summary

The human-readable description of the feature.

The name of the feature.

Constructor Summary

Constructors

Constructor

Description

MBeanFeatureInfo

​(

String

name,

String

description)

Constructs an

MBeanFeatureInfo

object.

MBeanFeatureInfo

​(

String

name,

String

description,

Descriptor

descriptor)

Constructs an

MBeanFeatureInfo

object.

---

#### Constructor Summary

Constructs an

MBeanFeatureInfo

object.

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

Compare this MBeanFeatureInfo to another.

String

getDescription

()

Returns the human-readable description of the feature.

Descriptor

getDescriptor

()

Returns the descriptor for the feature.

String

getName

()

Returns the name of the feature.

- Methods declared in class java.lang.

Object

clone

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

#### Method Summary

Compare this MBeanFeatureInfo to another.

Returns the human-readable description of the feature.

Returns the descriptor for the feature.

Returns the name of the feature.

Methods declared in class java.lang.

Object

clone

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

============ FIELD DETAIL ===========

- Field Detail

- name

```java
protected
String
name
```

The name of the feature. It is recommended that subclasses call

getName()

rather than reading this field, and that they
not change it.

- description

```java
protected
String
description
```

The human-readable description of the feature. It is
recommended that subclasses call

getDescription()

rather
than reading this field, and that they not change it.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MBeanFeatureInfo

```java
public MBeanFeatureInfo​(
String
name,

String
description)
```

Constructs an

MBeanFeatureInfo

object. This
constructor is equivalent to

MBeanFeatureInfo(name,
description, (Descriptor) null

.

**Parameters:** name

- The name of the feature.
**Parameters:** description

- A human readable description of the feature.

- MBeanFeatureInfo

```java
public MBeanFeatureInfo​(
String
name,

String
description,

Descriptor
descriptor)
```

Constructs an

MBeanFeatureInfo

object.

**Parameters:** name

- The name of the feature.
**Parameters:** description

- A human readable description of the feature.
**Parameters:** descriptor

- The descriptor for the feature. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the feature.

**Returns:** the name of the feature.

- getDescription

```java
public
String
getDescription()
```

Returns the human-readable description of the feature.

**Returns:** the human-readable description of the feature.

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns the descriptor for the feature. Changing the returned value
will have no affect on the original descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Returns:** a descriptor that is either immutable or a copy of the original.
**Since:** 1.6

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanFeatureInfo to another.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanFeatureInfo such
that its

getName()

,

getDescription()

, and

getDescriptor()

values are equal (not necessarily identical) to those of this
MBeanFeatureInfo.
**See Also:** Object.hashCode()

,

HashMap

Field Detail

- name

```java
protected
String
name
```

The name of the feature. It is recommended that subclasses call

getName()

rather than reading this field, and that they
not change it.

- description

```java
protected
String
description
```

The human-readable description of the feature. It is
recommended that subclasses call

getDescription()

rather
than reading this field, and that they not change it.

---

#### Field Detail

name

```java
protected
String
name
```

The name of the feature. It is recommended that subclasses call

getName()

rather than reading this field, and that they
not change it.

---

#### name

protected

String

name

The name of the feature. It is recommended that subclasses call

getName()

rather than reading this field, and that they
not change it.

description

```java
protected
String
description
```

The human-readable description of the feature. It is
recommended that subclasses call

getDescription()

rather
than reading this field, and that they not change it.

---

#### description

protected

String

description

The human-readable description of the feature. It is
recommended that subclasses call

getDescription()

rather
than reading this field, and that they not change it.

Constructor Detail

- MBeanFeatureInfo

```java
public MBeanFeatureInfo​(
String
name,

String
description)
```

Constructs an

MBeanFeatureInfo

object. This
constructor is equivalent to

MBeanFeatureInfo(name,
description, (Descriptor) null

.

**Parameters:** name

- The name of the feature.
**Parameters:** description

- A human readable description of the feature.

- MBeanFeatureInfo

```java
public MBeanFeatureInfo​(
String
name,

String
description,

Descriptor
descriptor)
```

Constructs an

MBeanFeatureInfo

object.

**Parameters:** name

- The name of the feature.
**Parameters:** description

- A human readable description of the feature.
**Parameters:** descriptor

- The descriptor for the feature. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

---

#### Constructor Detail

MBeanFeatureInfo

```java
public MBeanFeatureInfo​(
String
name,

String
description)
```

Constructs an

MBeanFeatureInfo

object. This
constructor is equivalent to

MBeanFeatureInfo(name,
description, (Descriptor) null

.

**Parameters:** name

- The name of the feature.
**Parameters:** description

- A human readable description of the feature.

---

#### MBeanFeatureInfo

public MBeanFeatureInfo​(

String

name,

String

description)

Constructs an

MBeanFeatureInfo

object. This
constructor is equivalent to

MBeanFeatureInfo(name,
description, (Descriptor) null

.

MBeanFeatureInfo

```java
public MBeanFeatureInfo​(
String
name,

String
description,

Descriptor
descriptor)
```

Constructs an

MBeanFeatureInfo

object.

**Parameters:** name

- The name of the feature.
**Parameters:** description

- A human readable description of the feature.
**Parameters:** descriptor

- The descriptor for the feature. This may be null
which is equivalent to an empty descriptor.
**Since:** 1.6

---

#### MBeanFeatureInfo

public MBeanFeatureInfo​(

String

name,

String

description,

Descriptor

descriptor)

Constructs an

MBeanFeatureInfo

object.

Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the feature.

**Returns:** the name of the feature.

- getDescription

```java
public
String
getDescription()
```

Returns the human-readable description of the feature.

**Returns:** the human-readable description of the feature.

- getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns the descriptor for the feature. Changing the returned value
will have no affect on the original descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Returns:** a descriptor that is either immutable or a copy of the original.
**Since:** 1.6

- equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanFeatureInfo to another.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanFeatureInfo such
that its

getName()

,

getDescription()

, and

getDescriptor()

values are equal (not necessarily identical) to those of this
MBeanFeatureInfo.
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the name of the feature.

**Returns:** the name of the feature.

---

#### getName

public

String

getName()

Returns the name of the feature.

getDescription

```java
public
String
getDescription()
```

Returns the human-readable description of the feature.

**Returns:** the human-readable description of the feature.

---

#### getDescription

public

String

getDescription()

Returns the human-readable description of the feature.

getDescriptor

```java
public
Descriptor
getDescriptor()
```

Returns the descriptor for the feature. Changing the returned value
will have no affect on the original descriptor.

**Specified by:** getDescriptor

in interface

DescriptorRead
**Returns:** a descriptor that is either immutable or a copy of the original.
**Since:** 1.6

---

#### getDescriptor

public

Descriptor

getDescriptor()

Returns the descriptor for the feature. Changing the returned value
will have no affect on the original descriptor.

equals

```java
public boolean equals​(
Object
o)
```

Compare this MBeanFeatureInfo to another.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare to.
**Returns:** true if and only if

o

is an MBeanFeatureInfo such
that its

getName()

,

getDescription()

, and

getDescriptor()

values are equal (not necessarily identical) to those of this
MBeanFeatureInfo.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compare this MBeanFeatureInfo to another.

---

