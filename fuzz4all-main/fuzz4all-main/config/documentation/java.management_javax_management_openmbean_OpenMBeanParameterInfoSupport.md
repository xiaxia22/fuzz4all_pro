# Class OpenMBeanParameterInfoSupport

**Source:** `java.management\javax\management\openmbean\OpenMBeanParameterInfoSupport.html`

### Class Description

```java
public class
OpenMBeanParameterInfoSupport

extends
MBeanParameterInfo

implements
OpenMBeanParameterInfo
```

Describes a parameter used in one or more operations or
constructors of an open MBean.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

OpenMBeanParameterInfo

---

### Field Details

*No entries found.*

### Constructor Details

#### public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<?> openType)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

and

description

.

**Parameters:**
- name

- cannot be a null or empty string.
- description

- cannot be a null or empty string.
- openType

- cannot be null.

**Throws:**
- IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.

---

#### public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<?> openType,

Descriptor
descriptor)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,
and

descriptor

.

The

descriptor

can contain entries that will define
the values returned by certain methods of this class, as
explained in the

package description

.

**Parameters:**
- name

- cannot be a null or empty string.
- description

- cannot be a null or empty string.
- openType

- cannot be null.
- descriptor

- The descriptor for the parameter. This may be null
which is equivalent to an empty descriptor.

**Throws:**
- IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null, or the descriptor entries are invalid as described in the

package
description

.

**Since:**
- 1.6

---

#### public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue)
throws
OpenDataException

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

and

defaultValue

.

**Parameters:**
- name

- cannot be a null or empty string.
- description

- cannot be a null or empty string.
- openType

- cannot be null.
- defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.

**Throws:**
- IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
- OpenDataException

- if

defaultValue

is not a
valid value for the specified

openType

, or

defaultValue

is non null and

openType

is an

ArrayType

or a

TabularType

.

**Type Parameters:**
- T

- allows the compiler to check that the

defaultValue

,
if non-null, has the correct Java type for the given

openType

.

---

#### public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue,
T[] legalValues)
throws
OpenDataException

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

and

legalValues

.

The contents of

legalValues

are copied, so subsequent
modifications of the array referenced by

legalValues

have no impact on this

OpenMBeanParameterInfoSupport

instance.

**Parameters:**
- name

- cannot be a null or empty string.
- description

- cannot be a null or empty string.
- openType

- cannot be null.
- defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
- legalValues

- each contained value must be valid for the

openType

specified for this parameter; legal values not
supported for

ArrayType

and

TabularType

; can be
null or empty.

**Throws:**
- IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
- OpenDataException

- if

defaultValue

is not a
valid value for the specified

openType

, or one value in

legalValues

is not valid for the specified

openType

, or

defaultValue

is non null and

openType

is an

ArrayType

or a

TabularType

, or

legalValues

is non null and non empty and

openType

is an

ArrayType

or a

TabularType

, or

legalValues

is non null and non empty and

defaultValue

is not contained in

legalValues

.

**Type Parameters:**
- T

- allows the compiler to check that the

defaultValue

and

legalValues

, if non-null, have the
correct Java type for the given

openType

.

---

#### public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue,

Comparable
<T> minValue,

Comparable
<T> maxValue)
throws
OpenDataException

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

,

minValue

and

maxValue

.

It is possible to specify minimal and maximal values only for
an open type whose values are

Comparable

.

**Parameters:**
- name

- cannot be a null or empty string.
- description

- cannot be a null or empty string.
- openType

- cannot be null.
- defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
- minValue

- must be valid for the

openType

specified for this parameter; can be null, in which case it
means that no minimal value is set.
- maxValue

- must be valid for the

openType

specified for this parameter; can be null, in which case it
means that no maximal value is set.

**Throws:**
- IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
- OpenDataException

- if

defaultValue

,

minValue

or

maxValue

is not a valid value for the
specified

openType

, or

defaultValue

is non null
and

openType

is an

ArrayType

or a

TabularType

, or both

minValue

and

maxValue

are
non-null and

minValue.compareTo(maxValue) > 0

is

true

, or both

defaultValue

and

minValue

are
non-null and

minValue.compareTo(defaultValue) > 0

is

true

, or both

defaultValue

and

maxValue

are non-null and

defaultValue.compareTo(maxValue) > 0

is

true

.

**Type Parameters:**
- T

- allows the compiler to check that the

defaultValue

,

minValue

, and

maxValue

, if
non-null, have the correct Java type for the given

openType

.

---

### Method Details

#### public
OpenType
<?> getOpenType()

Returns the open type for the values of the parameter described
by this

OpenMBeanParameterInfoSupport

instance.

**Specified by:**
- getOpenType

in interface

OpenMBeanParameterInfo

**Returns:**
- the open type.

---

#### public
Object
getDefaultValue()

Returns the default value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:**
- getDefaultValue

in interface

OpenMBeanParameterInfo

**Returns:**
- the default value.

---

#### public
Set
<?> getLegalValues()

Returns an unmodifiable Set of legal values for the parameter
described by this

OpenMBeanParameterInfoSupport

instance, if specified, or

null

otherwise.

**Specified by:**
- getLegalValues

in interface

OpenMBeanParameterInfo

**Returns:**
- the set of legal values.

---

#### public
Comparable
<?> getMinValue()

Returns the minimal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:**
- getMinValue

in interface

OpenMBeanParameterInfo

**Returns:**
- the minimum value.

---

#### public
Comparable
<?> getMaxValue()

Returns the maximal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:**
- getMaxValue

in interface

OpenMBeanParameterInfo

**Returns:**
- the maximum value.

---

#### public boolean hasDefaultValue()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
default value for the described parameter,

false

otherwise.

**Specified by:**
- hasDefaultValue

in interface

OpenMBeanParameterInfo

**Returns:**
- true if there is a default value.

---

#### public boolean hasLegalValues()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
set of legal values for the described parameter,

false

otherwise.

**Specified by:**
- hasLegalValues

in interface

OpenMBeanParameterInfo

**Returns:**
- true if there is a set of legal values.

---

#### public boolean hasMinValue()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
minimal value for the described parameter,

false

otherwise.

**Specified by:**
- hasMinValue

in interface

OpenMBeanParameterInfo

**Returns:**
- true if there is a minimum value.

---

#### public boolean hasMaxValue()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
maximal value for the described parameter,

false

otherwise.

**Specified by:**
- hasMaxValue

in interface

OpenMBeanParameterInfo

**Returns:**
- true if there is a maximum value.

---

#### public boolean isValue​(
Object
obj)

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

**Specified by:**
- isValue

in interface

OpenMBeanParameterInfo

**Parameters:**
- obj

- the object to be tested.

**Returns:**
- true

if

obj

is a valid value
for the parameter described by this

OpenMBeanParameterInfo

instance,

false

otherwise.

---

#### public boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

OpenMBeanParameterInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanParameterInfo

interface,
- their names are equal
- their open types are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanParameterInfo

interface.

If

obj

also implements

DescriptorRead

, then its

getDescriptor()

method must
also return the same value as for this object.

**Specified by:**
- equals

in interface

OpenMBeanParameterInfo

**Overrides:**
- equals

in class

MBeanParameterInfo

**Parameters:**
- obj

- the object to be compared for equality with this

OpenMBeanParameterInfoSupport

instance.

**Returns:**
- true

if the specified object is equal to this

OpenMBeanParameterInfoSupport

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

OpenMBeanParameterInfoSupport

instance.

The hash code of an

OpenMBeanParameterInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
its

open type

, its default, min, max and legal
values, and its Descriptor).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanParameterInfo

interface may be equal to
this

OpenMBeanParameterInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanParameterInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:**
- hashCode

in interface

OpenMBeanParameterInfo

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

OpenMBeanParameterInfoSupport

instance

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this

OpenMBeanParameterInfoSupport

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.OpenMBeanParameterInfoSupport

),
the string representation of the name and open type of the described
parameter, the string representation of its default, min, max and legal
values and the string representation of its descriptor.

As

OpenMBeanParameterInfoSupport

instances are immutable,
the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value
is returned for subsequent calls.

**Specified by:**
- toString

in interface

OpenMBeanParameterInfo

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

OpenMBeanParameterInfoSupport

instance.

---

### Additional Sections

#### Class OpenMBeanParameterInfoSupport

java.lang.Object

- javax.management.MBeanFeatureInfo
- - javax.management.MBeanParameterInfo
- - javax.management.openmbean.OpenMBeanParameterInfoSupport

javax.management.MBeanFeatureInfo

- javax.management.MBeanParameterInfo
- - javax.management.openmbean.OpenMBeanParameterInfoSupport

javax.management.MBeanParameterInfo

- javax.management.openmbean.OpenMBeanParameterInfoSupport

javax.management.openmbean.OpenMBeanParameterInfoSupport

**All Implemented Interfaces:** Serializable

,

Cloneable

,

DescriptorRead

,

OpenMBeanParameterInfo

```java
public class
OpenMBeanParameterInfoSupport

extends
MBeanParameterInfo

implements
OpenMBeanParameterInfo
```

Describes a parameter used in one or more operations or
constructors of an open MBean.

**Since:** 1.5
**See Also:** Serialized Form

public class

OpenMBeanParameterInfoSupport

extends

MBeanParameterInfo

implements

OpenMBeanParameterInfo

Describes a parameter used in one or more operations or
constructors of an open MBean.

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

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<?> openType)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

and

description

.

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<?> openType,

Descriptor

descriptor)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,
and

descriptor

.

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<T> openType,
T defaultValue)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

and

defaultValue

.

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<T> openType,
T defaultValue,

Comparable

<T> minValue,

Comparable

<T> maxValue)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

,

minValue

and

maxValue

.

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<T> openType,
T defaultValue,
T[] legalValues)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

and

legalValues

.

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

obj)

Compares the specified

obj

parameter with this

OpenMBeanParameterInfoSupport

instance for equality.

Object

getDefaultValue

()

Returns the default value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

Set

<?>

getLegalValues

()

Returns an unmodifiable Set of legal values for the parameter
described by this

OpenMBeanParameterInfoSupport

instance, if specified, or

null

otherwise.

Comparable

<?>

getMaxValue

()

Returns the maximal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

Comparable

<?>

getMinValue

()

Returns the minimal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

OpenType

<?>

getOpenType

()

Returns the open type for the values of the parameter described
by this

OpenMBeanParameterInfoSupport

instance.

boolean

hasDefaultValue

()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
default value for the described parameter,

false

otherwise.

int

hashCode

()

Returns the hash code value for this

OpenMBeanParameterInfoSupport

instance.

boolean

hasLegalValues

()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
set of legal values for the described parameter,

false

otherwise.

boolean

hasMaxValue

()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
maximal value for the described parameter,

false

otherwise.

boolean

hasMinValue

()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
minimal value for the described parameter,

false

otherwise.

boolean

isValue

​(

Object

obj)

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

String

toString

()

Returns a string representation of this

OpenMBeanParameterInfoSupport

instance.

- Methods declared in class javax.management.

MBeanParameterInfo

clone

,

getType

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

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface javax.management.openmbean.

OpenMBeanParameterInfo

getDescription

,

getName

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

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<?> openType)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

and

description

.

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<?> openType,

Descriptor

descriptor)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,
and

descriptor

.

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<T> openType,
T defaultValue)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

and

defaultValue

.

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<T> openType,
T defaultValue,

Comparable

<T> minValue,

Comparable

<T> maxValue)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

,

minValue

and

maxValue

.

OpenMBeanParameterInfoSupport

​(

String

name,

String

description,

OpenType

<T> openType,
T defaultValue,
T[] legalValues)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

and

legalValues

.

---

#### Constructor Summary

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

and

description

.

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,
and

descriptor

.

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

and

defaultValue

.

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

,

minValue

and

maxValue

.

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

and

legalValues

.

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

obj)

Compares the specified

obj

parameter with this

OpenMBeanParameterInfoSupport

instance for equality.

Object

getDefaultValue

()

Returns the default value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

Set

<?>

getLegalValues

()

Returns an unmodifiable Set of legal values for the parameter
described by this

OpenMBeanParameterInfoSupport

instance, if specified, or

null

otherwise.

Comparable

<?>

getMaxValue

()

Returns the maximal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

Comparable

<?>

getMinValue

()

Returns the minimal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

OpenType

<?>

getOpenType

()

Returns the open type for the values of the parameter described
by this

OpenMBeanParameterInfoSupport

instance.

boolean

hasDefaultValue

()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
default value for the described parameter,

false

otherwise.

int

hashCode

()

Returns the hash code value for this

OpenMBeanParameterInfoSupport

instance.

boolean

hasLegalValues

()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
set of legal values for the described parameter,

false

otherwise.

boolean

hasMaxValue

()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
maximal value for the described parameter,

false

otherwise.

boolean

hasMinValue

()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
minimal value for the described parameter,

false

otherwise.

boolean

isValue

​(

Object

obj)

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

String

toString

()

Returns a string representation of this

OpenMBeanParameterInfoSupport

instance.

- Methods declared in class javax.management.

MBeanParameterInfo

clone

,

getType

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

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface javax.management.openmbean.

OpenMBeanParameterInfo

getDescription

,

getName

---

#### Method Summary

Compares the specified

obj

parameter with this

OpenMBeanParameterInfoSupport

instance for equality.

Returns the default value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

Returns an unmodifiable Set of legal values for the parameter
described by this

OpenMBeanParameterInfoSupport

instance, if specified, or

null

otherwise.

Returns the maximal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

Returns the minimal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

Returns the open type for the values of the parameter described
by this

OpenMBeanParameterInfoSupport

instance.

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
default value for the described parameter,

false

otherwise.

Returns the hash code value for this

OpenMBeanParameterInfoSupport

instance.

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
set of legal values for the described parameter,

false

otherwise.

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
maximal value for the described parameter,

false

otherwise.

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
minimal value for the described parameter,

false

otherwise.

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

Returns a string representation of this

OpenMBeanParameterInfoSupport

instance.

Methods declared in class javax.management.

MBeanParameterInfo

clone

,

getType

---

#### Methods declared in class javax.management. MBeanParameterInfo

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

Methods declared in interface javax.management.openmbean.

OpenMBeanParameterInfo

getDescription

,

getName

---

#### Methods declared in interface javax.management.openmbean. OpenMBeanParameterInfo

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<?> openType)
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

and

description

.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<?> openType,

Descriptor
descriptor)
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,
and

descriptor

.

The

descriptor

can contain entries that will define
the values returned by certain methods of this class, as
explained in the

package description

.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** descriptor

- The descriptor for the parameter. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null, or the descriptor entries are invalid as described in the

package
description

.
**Since:** 1.6

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue)
throws
OpenDataException
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

and

defaultValue

.

**Type Parameters:** T

- allows the compiler to check that the

defaultValue

,
if non-null, has the correct Java type for the given

openType

.
**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
**Throws:** OpenDataException

- if

defaultValue

is not a
valid value for the specified

openType

, or

defaultValue

is non null and

openType

is an

ArrayType

or a

TabularType

.

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue,
T[] legalValues)
throws
OpenDataException
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

and

legalValues

.

The contents of

legalValues

are copied, so subsequent
modifications of the array referenced by

legalValues

have no impact on this

OpenMBeanParameterInfoSupport

instance.

**Type Parameters:** T

- allows the compiler to check that the

defaultValue

and

legalValues

, if non-null, have the
correct Java type for the given

openType

.
**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
**Parameters:** legalValues

- each contained value must be valid for the

openType

specified for this parameter; legal values not
supported for

ArrayType

and

TabularType

; can be
null or empty.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
**Throws:** OpenDataException

- if

defaultValue

is not a
valid value for the specified

openType

, or one value in

legalValues

is not valid for the specified

openType

, or

defaultValue

is non null and

openType

is an

ArrayType

or a

TabularType

, or

legalValues

is non null and non empty and

openType

is an

ArrayType

or a

TabularType

, or

legalValues

is non null and non empty and

defaultValue

is not contained in

legalValues

.

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue,

Comparable
<T> minValue,

Comparable
<T> maxValue)
throws
OpenDataException
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

,

minValue

and

maxValue

.

It is possible to specify minimal and maximal values only for
an open type whose values are

Comparable

.

**Type Parameters:** T

- allows the compiler to check that the

defaultValue

,

minValue

, and

maxValue

, if
non-null, have the correct Java type for the given

openType

.
**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
**Parameters:** minValue

- must be valid for the

openType

specified for this parameter; can be null, in which case it
means that no minimal value is set.
**Parameters:** maxValue

- must be valid for the

openType

specified for this parameter; can be null, in which case it
means that no maximal value is set.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
**Throws:** OpenDataException

- if

defaultValue

,

minValue

or

maxValue

is not a valid value for the
specified

openType

, or

defaultValue

is non null
and

openType

is an

ArrayType

or a

TabularType

, or both

minValue

and

maxValue

are
non-null and

minValue.compareTo(maxValue) > 0

is

true

, or both

defaultValue

and

minValue

are
non-null and

minValue.compareTo(defaultValue) > 0

is

true

, or both

defaultValue

and

maxValue

are non-null and

defaultValue.compareTo(maxValue) > 0

is

true

.

============ METHOD DETAIL ==========

- Method Detail

- getOpenType

```java
public
OpenType
<?> getOpenType()
```

Returns the open type for the values of the parameter described
by this

OpenMBeanParameterInfoSupport

instance.

**Specified by:** getOpenType

in interface

OpenMBeanParameterInfo
**Returns:** the open type.

- getDefaultValue

```java
public
Object
getDefaultValue()
```

Returns the default value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:** getDefaultValue

in interface

OpenMBeanParameterInfo
**Returns:** the default value.

- getLegalValues

```java
public
Set
<?> getLegalValues()
```

Returns an unmodifiable Set of legal values for the parameter
described by this

OpenMBeanParameterInfoSupport

instance, if specified, or

null

otherwise.

**Specified by:** getLegalValues

in interface

OpenMBeanParameterInfo
**Returns:** the set of legal values.

- getMinValue

```java
public
Comparable
<?> getMinValue()
```

Returns the minimal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:** getMinValue

in interface

OpenMBeanParameterInfo
**Returns:** the minimum value.

- getMaxValue

```java
public
Comparable
<?> getMaxValue()
```

Returns the maximal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:** getMaxValue

in interface

OpenMBeanParameterInfo
**Returns:** the maximum value.

- hasDefaultValue

```java
public boolean hasDefaultValue()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
default value for the described parameter,

false

otherwise.

**Specified by:** hasDefaultValue

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a default value.

- hasLegalValues

```java
public boolean hasLegalValues()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
set of legal values for the described parameter,

false

otherwise.

**Specified by:** hasLegalValues

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a set of legal values.

- hasMinValue

```java
public boolean hasMinValue()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
minimal value for the described parameter,

false

otherwise.

**Specified by:** hasMinValue

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a minimum value.

- hasMaxValue

```java
public boolean hasMaxValue()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
maximal value for the described parameter,

false

otherwise.

**Specified by:** hasMaxValue

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a maximum value.

- isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

**Specified by:** isValue

in interface

OpenMBeanParameterInfo
**Parameters:** obj

- the object to be tested.
**Returns:** true

if

obj

is a valid value
for the parameter described by this

OpenMBeanParameterInfo

instance,

false

otherwise.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanParameterInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanParameterInfo

interface,
- their names are equal
- their open types are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanParameterInfo

interface.

If

obj

also implements

DescriptorRead

, then its

getDescriptor()

method must
also return the same value as for this object.

**Specified by:** equals

in interface

OpenMBeanParameterInfo
**Overrides:** equals

in class

MBeanParameterInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanParameterInfoSupport

instance.
**Returns:** true

if the specified object is equal to this

OpenMBeanParameterInfoSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanParameterInfoSupport

instance.

The hash code of an

OpenMBeanParameterInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
its

open type

, its default, min, max and legal
values, and its Descriptor).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanParameterInfo

interface may be equal to
this

OpenMBeanParameterInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanParameterInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanParameterInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanParameterInfoSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

OpenMBeanParameterInfoSupport

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.OpenMBeanParameterInfoSupport

),
the string representation of the name and open type of the described
parameter, the string representation of its default, min, max and legal
values and the string representation of its descriptor.

As

OpenMBeanParameterInfoSupport

instances are immutable,
the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value
is returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanParameterInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanParameterInfoSupport

instance.

Constructor Detail

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<?> openType)
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

and

description

.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<?> openType,

Descriptor
descriptor)
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,
and

descriptor

.

The

descriptor

can contain entries that will define
the values returned by certain methods of this class, as
explained in the

package description

.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** descriptor

- The descriptor for the parameter. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null, or the descriptor entries are invalid as described in the

package
description

.
**Since:** 1.6

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue)
throws
OpenDataException
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

and

defaultValue

.

**Type Parameters:** T

- allows the compiler to check that the

defaultValue

,
if non-null, has the correct Java type for the given

openType

.
**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
**Throws:** OpenDataException

- if

defaultValue

is not a
valid value for the specified

openType

, or

defaultValue

is non null and

openType

is an

ArrayType

or a

TabularType

.

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue,
T[] legalValues)
throws
OpenDataException
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

and

legalValues

.

The contents of

legalValues

are copied, so subsequent
modifications of the array referenced by

legalValues

have no impact on this

OpenMBeanParameterInfoSupport

instance.

**Type Parameters:** T

- allows the compiler to check that the

defaultValue

and

legalValues

, if non-null, have the
correct Java type for the given

openType

.
**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
**Parameters:** legalValues

- each contained value must be valid for the

openType

specified for this parameter; legal values not
supported for

ArrayType

and

TabularType

; can be
null or empty.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
**Throws:** OpenDataException

- if

defaultValue

is not a
valid value for the specified

openType

, or one value in

legalValues

is not valid for the specified

openType

, or

defaultValue

is non null and

openType

is an

ArrayType

or a

TabularType

, or

legalValues

is non null and non empty and

openType

is an

ArrayType

or a

TabularType

, or

legalValues

is non null and non empty and

defaultValue

is not contained in

legalValues

.

- OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue,

Comparable
<T> minValue,

Comparable
<T> maxValue)
throws
OpenDataException
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

,

minValue

and

maxValue

.

It is possible to specify minimal and maximal values only for
an open type whose values are

Comparable

.

**Type Parameters:** T

- allows the compiler to check that the

defaultValue

,

minValue

, and

maxValue

, if
non-null, have the correct Java type for the given

openType

.
**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
**Parameters:** minValue

- must be valid for the

openType

specified for this parameter; can be null, in which case it
means that no minimal value is set.
**Parameters:** maxValue

- must be valid for the

openType

specified for this parameter; can be null, in which case it
means that no maximal value is set.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
**Throws:** OpenDataException

- if

defaultValue

,

minValue

or

maxValue

is not a valid value for the
specified

openType

, or

defaultValue

is non null
and

openType

is an

ArrayType

or a

TabularType

, or both

minValue

and

maxValue

are
non-null and

minValue.compareTo(maxValue) > 0

is

true

, or both

defaultValue

and

minValue

are
non-null and

minValue.compareTo(defaultValue) > 0

is

true

, or both

defaultValue

and

maxValue

are non-null and

defaultValue.compareTo(maxValue) > 0

is

true

.

---

#### Constructor Detail

OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<?> openType)
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

and

description

.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.

---

#### OpenMBeanParameterInfoSupport

public OpenMBeanParameterInfoSupport​(

String

name,

String

description,

OpenType

<?> openType)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

and

description

.

OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<?> openType,

Descriptor
descriptor)
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,
and

descriptor

.

The

descriptor

can contain entries that will define
the values returned by certain methods of this class, as
explained in the

package description

.

**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** descriptor

- The descriptor for the parameter. This may be null
which is equivalent to an empty descriptor.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null, or the descriptor entries are invalid as described in the

package
description

.
**Since:** 1.6

---

#### OpenMBeanParameterInfoSupport

public OpenMBeanParameterInfoSupport​(

String

name,

String

description,

OpenType

<?> openType,

Descriptor

descriptor)

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,
and

descriptor

.

The

descriptor

can contain entries that will define
the values returned by certain methods of this class, as
explained in the

package description

.

The

descriptor

can contain entries that will define
the values returned by certain methods of this class, as
explained in the

package description

.

OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue)
throws
OpenDataException
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

and

defaultValue

.

**Type Parameters:** T

- allows the compiler to check that the

defaultValue

,
if non-null, has the correct Java type for the given

openType

.
**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
**Throws:** OpenDataException

- if

defaultValue

is not a
valid value for the specified

openType

, or

defaultValue

is non null and

openType

is an

ArrayType

or a

TabularType

.

---

#### OpenMBeanParameterInfoSupport

public OpenMBeanParameterInfoSupport​(

String

name,

String

description,

OpenType

<T> openType,
T defaultValue)
throws

OpenDataException

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

and

defaultValue

.

OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue,
T[] legalValues)
throws
OpenDataException
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

and

legalValues

.

The contents of

legalValues

are copied, so subsequent
modifications of the array referenced by

legalValues

have no impact on this

OpenMBeanParameterInfoSupport

instance.

**Type Parameters:** T

- allows the compiler to check that the

defaultValue

and

legalValues

, if non-null, have the
correct Java type for the given

openType

.
**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
**Parameters:** legalValues

- each contained value must be valid for the

openType

specified for this parameter; legal values not
supported for

ArrayType

and

TabularType

; can be
null or empty.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
**Throws:** OpenDataException

- if

defaultValue

is not a
valid value for the specified

openType

, or one value in

legalValues

is not valid for the specified

openType

, or

defaultValue

is non null and

openType

is an

ArrayType

or a

TabularType

, or

legalValues

is non null and non empty and

openType

is an

ArrayType

or a

TabularType

, or

legalValues

is non null and non empty and

defaultValue

is not contained in

legalValues

.

---

#### OpenMBeanParameterInfoSupport

public OpenMBeanParameterInfoSupport​(

String

name,

String

description,

OpenType

<T> openType,
T defaultValue,
T[] legalValues)
throws

OpenDataException

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

and

legalValues

.

The contents of

legalValues

are copied, so subsequent
modifications of the array referenced by

legalValues

have no impact on this

OpenMBeanParameterInfoSupport

instance.

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

and

legalValues

.

The contents of

legalValues

are copied, so subsequent
modifications of the array referenced by

legalValues

have no impact on this

OpenMBeanParameterInfoSupport

instance.

OpenMBeanParameterInfoSupport

```java
public OpenMBeanParameterInfoSupport​(
String
name,

String
description,

OpenType
<T> openType,
T defaultValue,

Comparable
<T> minValue,

Comparable
<T> maxValue)
throws
OpenDataException
```

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

,

minValue

and

maxValue

.

It is possible to specify minimal and maximal values only for
an open type whose values are

Comparable

.

**Type Parameters:** T

- allows the compiler to check that the

defaultValue

,

minValue

, and

maxValue

, if
non-null, have the correct Java type for the given

openType

.
**Parameters:** name

- cannot be a null or empty string.
**Parameters:** description

- cannot be a null or empty string.
**Parameters:** openType

- cannot be null.
**Parameters:** defaultValue

- must be a valid value for the

openType

specified for this parameter; default value not
supported for

ArrayType

and

TabularType

; can be
null, in which case it means that no default value is set.
**Parameters:** minValue

- must be valid for the

openType

specified for this parameter; can be null, in which case it
means that no minimal value is set.
**Parameters:** maxValue

- must be valid for the

openType

specified for this parameter; can be null, in which case it
means that no maximal value is set.
**Throws:** IllegalArgumentException

- if

name

or

description

are null or empty string, or

openType

is
null.
**Throws:** OpenDataException

- if

defaultValue

,

minValue

or

maxValue

is not a valid value for the
specified

openType

, or

defaultValue

is non null
and

openType

is an

ArrayType

or a

TabularType

, or both

minValue

and

maxValue

are
non-null and

minValue.compareTo(maxValue) > 0

is

true

, or both

defaultValue

and

minValue

are
non-null and

minValue.compareTo(defaultValue) > 0

is

true

, or both

defaultValue

and

maxValue

are non-null and

defaultValue.compareTo(maxValue) > 0

is

true

.

---

#### OpenMBeanParameterInfoSupport

public OpenMBeanParameterInfoSupport​(

String

name,

String

description,

OpenType

<T> openType,
T defaultValue,

Comparable

<T> minValue,

Comparable

<T> maxValue)
throws

OpenDataException

Constructs an

OpenMBeanParameterInfoSupport

instance,
which describes the parameter used in one or more operations or
constructors of a class of open MBeans, with the specified

name

,

openType

,

description

,

defaultValue

,

minValue

and

maxValue

.

It is possible to specify minimal and maximal values only for
an open type whose values are

Comparable

.

Method Detail

- getOpenType

```java
public
OpenType
<?> getOpenType()
```

Returns the open type for the values of the parameter described
by this

OpenMBeanParameterInfoSupport

instance.

**Specified by:** getOpenType

in interface

OpenMBeanParameterInfo
**Returns:** the open type.

- getDefaultValue

```java
public
Object
getDefaultValue()
```

Returns the default value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:** getDefaultValue

in interface

OpenMBeanParameterInfo
**Returns:** the default value.

- getLegalValues

```java
public
Set
<?> getLegalValues()
```

Returns an unmodifiable Set of legal values for the parameter
described by this

OpenMBeanParameterInfoSupport

instance, if specified, or

null

otherwise.

**Specified by:** getLegalValues

in interface

OpenMBeanParameterInfo
**Returns:** the set of legal values.

- getMinValue

```java
public
Comparable
<?> getMinValue()
```

Returns the minimal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:** getMinValue

in interface

OpenMBeanParameterInfo
**Returns:** the minimum value.

- getMaxValue

```java
public
Comparable
<?> getMaxValue()
```

Returns the maximal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:** getMaxValue

in interface

OpenMBeanParameterInfo
**Returns:** the maximum value.

- hasDefaultValue

```java
public boolean hasDefaultValue()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
default value for the described parameter,

false

otherwise.

**Specified by:** hasDefaultValue

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a default value.

- hasLegalValues

```java
public boolean hasLegalValues()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
set of legal values for the described parameter,

false

otherwise.

**Specified by:** hasLegalValues

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a set of legal values.

- hasMinValue

```java
public boolean hasMinValue()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
minimal value for the described parameter,

false

otherwise.

**Specified by:** hasMinValue

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a minimum value.

- hasMaxValue

```java
public boolean hasMaxValue()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
maximal value for the described parameter,

false

otherwise.

**Specified by:** hasMaxValue

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a maximum value.

- isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

**Specified by:** isValue

in interface

OpenMBeanParameterInfo
**Parameters:** obj

- the object to be tested.
**Returns:** true

if

obj

is a valid value
for the parameter described by this

OpenMBeanParameterInfo

instance,

false

otherwise.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanParameterInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanParameterInfo

interface,
- their names are equal
- their open types are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanParameterInfo

interface.

If

obj

also implements

DescriptorRead

, then its

getDescriptor()

method must
also return the same value as for this object.

**Specified by:** equals

in interface

OpenMBeanParameterInfo
**Overrides:** equals

in class

MBeanParameterInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanParameterInfoSupport

instance.
**Returns:** true

if the specified object is equal to this

OpenMBeanParameterInfoSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanParameterInfoSupport

instance.

The hash code of an

OpenMBeanParameterInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
its

open type

, its default, min, max and legal
values, and its Descriptor).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanParameterInfo

interface may be equal to
this

OpenMBeanParameterInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanParameterInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanParameterInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanParameterInfoSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

OpenMBeanParameterInfoSupport

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.OpenMBeanParameterInfoSupport

),
the string representation of the name and open type of the described
parameter, the string representation of its default, min, max and legal
values and the string representation of its descriptor.

As

OpenMBeanParameterInfoSupport

instances are immutable,
the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value
is returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanParameterInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanParameterInfoSupport

instance.

---

#### Method Detail

getOpenType

```java
public
OpenType
<?> getOpenType()
```

Returns the open type for the values of the parameter described
by this

OpenMBeanParameterInfoSupport

instance.

**Specified by:** getOpenType

in interface

OpenMBeanParameterInfo
**Returns:** the open type.

---

#### getOpenType

public

OpenType

<?> getOpenType()

Returns the open type for the values of the parameter described
by this

OpenMBeanParameterInfoSupport

instance.

getDefaultValue

```java
public
Object
getDefaultValue()
```

Returns the default value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:** getDefaultValue

in interface

OpenMBeanParameterInfo
**Returns:** the default value.

---

#### getDefaultValue

public

Object

getDefaultValue()

Returns the default value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

getLegalValues

```java
public
Set
<?> getLegalValues()
```

Returns an unmodifiable Set of legal values for the parameter
described by this

OpenMBeanParameterInfoSupport

instance, if specified, or

null

otherwise.

**Specified by:** getLegalValues

in interface

OpenMBeanParameterInfo
**Returns:** the set of legal values.

---

#### getLegalValues

public

Set

<?> getLegalValues()

Returns an unmodifiable Set of legal values for the parameter
described by this

OpenMBeanParameterInfoSupport

instance, if specified, or

null

otherwise.

getMinValue

```java
public
Comparable
<?> getMinValue()
```

Returns the minimal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:** getMinValue

in interface

OpenMBeanParameterInfo
**Returns:** the minimum value.

---

#### getMinValue

public

Comparable

<?> getMinValue()

Returns the minimal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

getMaxValue

```java
public
Comparable
<?> getMaxValue()
```

Returns the maximal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

**Specified by:** getMaxValue

in interface

OpenMBeanParameterInfo
**Returns:** the maximum value.

---

#### getMaxValue

public

Comparable

<?> getMaxValue()

Returns the maximal value for the parameter described by this

OpenMBeanParameterInfoSupport

instance, if specified,
or

null

otherwise.

hasDefaultValue

```java
public boolean hasDefaultValue()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
default value for the described parameter,

false

otherwise.

**Specified by:** hasDefaultValue

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a default value.

---

#### hasDefaultValue

public boolean hasDefaultValue()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
default value for the described parameter,

false

otherwise.

hasLegalValues

```java
public boolean hasLegalValues()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
set of legal values for the described parameter,

false

otherwise.

**Specified by:** hasLegalValues

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a set of legal values.

---

#### hasLegalValues

public boolean hasLegalValues()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
set of legal values for the described parameter,

false

otherwise.

hasMinValue

```java
public boolean hasMinValue()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
minimal value for the described parameter,

false

otherwise.

**Specified by:** hasMinValue

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a minimum value.

---

#### hasMinValue

public boolean hasMinValue()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
minimal value for the described parameter,

false

otherwise.

hasMaxValue

```java
public boolean hasMaxValue()
```

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
maximal value for the described parameter,

false

otherwise.

**Specified by:** hasMaxValue

in interface

OpenMBeanParameterInfo
**Returns:** true if there is a maximum value.

---

#### hasMaxValue

public boolean hasMaxValue()

Returns

true

if this

OpenMBeanParameterInfoSupport

instance specifies a non-null
maximal value for the described parameter,

false

otherwise.

isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

**Specified by:** isValue

in interface

OpenMBeanParameterInfo
**Parameters:** obj

- the object to be tested.
**Returns:** true

if

obj

is a valid value
for the parameter described by this

OpenMBeanParameterInfo

instance,

false

otherwise.

---

#### isValue

public boolean isValue​(

Object

obj)

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanParameterInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanParameterInfo

interface,
- their names are equal
- their open types are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanParameterInfo

interface.

If

obj

also implements

DescriptorRead

, then its

getDescriptor()

method must
also return the same value as for this object.

**Specified by:** equals

in interface

OpenMBeanParameterInfo
**Overrides:** equals

in class

MBeanParameterInfo
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanParameterInfoSupport

instance.
**Returns:** true

if the specified object is equal to this

OpenMBeanParameterInfoSupport

instance.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified

obj

parameter with this

OpenMBeanParameterInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanParameterInfo

interface,
- their names are equal
- their open types are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanParameterInfo

interface.

If

obj

also implements

DescriptorRead

, then its

getDescriptor()

method must
also return the same value as for this object.

Compares the specified

obj

parameter with this

OpenMBeanParameterInfoSupport

instance for equality.

Returns

true

if and only if all of the following
statements are true:

- obj

is non null,
- obj

also implements the

OpenMBeanParameterInfo

interface,
- their names are equal
- their open types are equal
- their default, min, max and legal values are equal.

This ensures that this

equals

method works properly for

obj

parameters which are different implementations of
the

OpenMBeanParameterInfo

interface.

If

obj

also implements

DescriptorRead

, then its

getDescriptor()

method must
also return the same value as for this object.

obj

is non null,

obj

also implements the

OpenMBeanParameterInfo

interface,

their names are equal

their open types are equal

their default, min, max and legal values are equal.

If

obj

also implements

DescriptorRead

, then its

getDescriptor()

method must
also return the same value as for this object.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

OpenMBeanParameterInfoSupport

instance.

The hash code of an

OpenMBeanParameterInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
its

open type

, its default, min, max and legal
values, and its Descriptor).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanParameterInfo

interface may be equal to
this

OpenMBeanParameterInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanParameterInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

**Specified by:** hashCode

in interface

OpenMBeanParameterInfo
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanParameterInfoSupport

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

OpenMBeanParameterInfoSupport

instance.

The hash code of an

OpenMBeanParameterInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
its

open type

, its default, min, max and legal
values, and its Descriptor).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanParameterInfo

interface may be equal to
this

OpenMBeanParameterInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanParameterInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

Returns the hash code value for this

OpenMBeanParameterInfoSupport

instance.

The hash code of an

OpenMBeanParameterInfoSupport

instance is the sum of the hash codes of all elements of
information used in

equals

comparisons (ie: its name,
its

open type

, its default, min, max and legal
values, and its Descriptor).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanParameterInfo

interface may be equal to
this

OpenMBeanParameterInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanParameterInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfoSupport

instances

t1

and

t2

, as required by the general contract of the method

Object.hashCode()

.

However, note that another instance of a class implementing
the

OpenMBeanParameterInfo

interface may be equal to
this

OpenMBeanParameterInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanParameterInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

However, note that another instance of a class implementing
the

OpenMBeanParameterInfo

interface may be equal to
this

OpenMBeanParameterInfoSupport

instance as defined
by

equals(java.lang.Object)

, but may have a different
hash code if it is calculated differently.

As

OpenMBeanParameterInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

As

OpenMBeanParameterInfoSupport

instances are
immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value
is returned for subsequent calls.

toString

```java
public
String
toString()
```

Returns a string representation of this

OpenMBeanParameterInfoSupport

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.OpenMBeanParameterInfoSupport

),
the string representation of the name and open type of the described
parameter, the string representation of its default, min, max and legal
values and the string representation of its descriptor.

As

OpenMBeanParameterInfoSupport

instances are immutable,
the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value
is returned for subsequent calls.

**Specified by:** toString

in interface

OpenMBeanParameterInfo
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanParameterInfoSupport

instance.

---

#### toString

public

String

toString()

Returns a string representation of this

OpenMBeanParameterInfoSupport

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.OpenMBeanParameterInfoSupport

),
the string representation of the name and open type of the described
parameter, the string representation of its default, min, max and legal
values and the string representation of its descriptor.

As

OpenMBeanParameterInfoSupport

instances are immutable,
the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value
is returned for subsequent calls.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.OpenMBeanParameterInfoSupport

),
the string representation of the name and open type of the described
parameter, the string representation of its default, min, max and legal
values and the string representation of its descriptor.

As

OpenMBeanParameterInfoSupport

instances are immutable,
the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value
is returned for subsequent calls.

As

OpenMBeanParameterInfoSupport

instances are immutable,
the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value
is returned for subsequent calls.

---

