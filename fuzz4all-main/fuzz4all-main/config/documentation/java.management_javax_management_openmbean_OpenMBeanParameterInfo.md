# Interface OpenMBeanParameterInfo

**Source:** `java.management\javax\management\openmbean\OpenMBeanParameterInfo.html`

### Class Description

```java
public interface
OpenMBeanParameterInfo
```

Describes a parameter used in one or more operations or
constructors of an open MBean.

This interface declares the same methods as the class

MBeanParameterInfo

. A class implementing this
interface (typically

OpenMBeanParameterInfoSupport

) should
extend

MBeanParameterInfo

.

**All Known Subinterfaces:** OpenMBeanAttributeInfo

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getDescription()

Returns a human readable description of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:**
- the description.

---

#### String
getName()

Returns the name of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:**
- the name.

---

#### OpenType
<?> getOpenType()

Returns the

open type

of the values of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:**
- the open type.

---

#### Object
getDefaultValue()

Returns the default value for this parameter, if it has one, or

null

otherwise.

**Returns:**
- the default value.

---

#### Set
<?> getLegalValues()

Returns the set of legal values for this parameter, if it has
one, or

null

otherwise.

**Returns:**
- the set of legal values.

---

#### Comparable
<?> getMinValue()

Returns the minimal value for this parameter, if it has one, or

null

otherwise.

**Returns:**
- the minimum value.

---

#### Comparable
<?> getMaxValue()

Returns the maximal value for this parameter, if it has one, or

null

otherwise.

**Returns:**
- the maximum value.

---

#### boolean hasDefaultValue()

Returns

true

if this parameter has a specified default
value, or

false

otherwise.

**Returns:**
- true if there is a default value.

---

#### boolean hasLegalValues()

Returns

true

if this parameter has a specified set of
legal values, or

false

otherwise.

**Returns:**
- true if there is a set of legal values.

---

#### boolean hasMinValue()

Returns

true

if this parameter has a specified minimal
value, or

false

otherwise.

**Returns:**
- true if there is a minimum value.

---

#### boolean hasMaxValue()

Returns

true

if this parameter has a specified maximal
value, or

false

otherwise.

**Returns:**
- true if there is a maximum value.

---

#### boolean isValue​(
Object
obj)

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

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

#### boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

OpenMBeanParameterInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanParameterInfo

interface.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this

OpenMBeanParameterInfo

instance;

**Returns:**
- true

if the specified object is equal to this

OpenMBeanParameterInfo

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this

OpenMBeanParameterInfo

instance.

The hash code of an

OpenMBeanParameterInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

OpenMBeanParameterInfo

instance

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### String
toString()

Returns a string representation of this

OpenMBeanParameterInfo

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.OpenMBeanParameterInfo

),
the string representation of the name and open type of the described parameter,
and the string representation of its default, min, max and legal values.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

OpenMBeanParameterInfo

instance

---

### Additional Sections

#### Interface OpenMBeanParameterInfo

**All Known Subinterfaces:** OpenMBeanAttributeInfo

**All Known Implementing Classes:** OpenMBeanAttributeInfoSupport

,

OpenMBeanParameterInfoSupport

```java
public interface
OpenMBeanParameterInfo
```

Describes a parameter used in one or more operations or
constructors of an open MBean.

This interface declares the same methods as the class

MBeanParameterInfo

. A class implementing this
interface (typically

OpenMBeanParameterInfoSupport

) should
extend

MBeanParameterInfo

.

**Since:** 1.5

public interface

OpenMBeanParameterInfo

Describes a parameter used in one or more operations or
constructors of an open MBean.

This interface declares the same methods as the class

MBeanParameterInfo

. A class implementing this
interface (typically

OpenMBeanParameterInfoSupport

) should
extend

MBeanParameterInfo

.

Describes a parameter used in one or more operations or
constructors of an open MBean.

This interface declares the same methods as the class

MBeanParameterInfo

. A class implementing this
interface (typically

OpenMBeanParameterInfoSupport

) should
extend

MBeanParameterInfo

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

OpenMBeanParameterInfo

instance for equality.

Object

getDefaultValue

()

Returns the default value for this parameter, if it has one, or

null

otherwise.

String

getDescription

()

Returns a human readable description of the parameter
described by this

OpenMBeanParameterInfo

instance.

Set

<?>

getLegalValues

()

Returns the set of legal values for this parameter, if it has
one, or

null

otherwise.

Comparable

<?>

getMaxValue

()

Returns the maximal value for this parameter, if it has one, or

null

otherwise.

Comparable

<?>

getMinValue

()

Returns the minimal value for this parameter, if it has one, or

null

otherwise.

String

getName

()

Returns the name of the parameter
described by this

OpenMBeanParameterInfo

instance.

OpenType

<?>

getOpenType

()

Returns the

open type

of the values of the parameter
described by this

OpenMBeanParameterInfo

instance.

boolean

hasDefaultValue

()

Returns

true

if this parameter has a specified default
value, or

false

otherwise.

int

hashCode

()

Returns the hash code value for this

OpenMBeanParameterInfo

instance.

boolean

hasLegalValues

()

Returns

true

if this parameter has a specified set of
legal values, or

false

otherwise.

boolean

hasMaxValue

()

Returns

true

if this parameter has a specified maximal
value, or

false

otherwise.

boolean

hasMinValue

()

Returns

true

if this parameter has a specified minimal
value, or

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

OpenMBeanParameterInfo

instance.

Method Summary

All Methods

Instance Methods

Abstract Methods

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

OpenMBeanParameterInfo

instance for equality.

Object

getDefaultValue

()

Returns the default value for this parameter, if it has one, or

null

otherwise.

String

getDescription

()

Returns a human readable description of the parameter
described by this

OpenMBeanParameterInfo

instance.

Set

<?>

getLegalValues

()

Returns the set of legal values for this parameter, if it has
one, or

null

otherwise.

Comparable

<?>

getMaxValue

()

Returns the maximal value for this parameter, if it has one, or

null

otherwise.

Comparable

<?>

getMinValue

()

Returns the minimal value for this parameter, if it has one, or

null

otherwise.

String

getName

()

Returns the name of the parameter
described by this

OpenMBeanParameterInfo

instance.

OpenType

<?>

getOpenType

()

Returns the

open type

of the values of the parameter
described by this

OpenMBeanParameterInfo

instance.

boolean

hasDefaultValue

()

Returns

true

if this parameter has a specified default
value, or

false

otherwise.

int

hashCode

()

Returns the hash code value for this

OpenMBeanParameterInfo

instance.

boolean

hasLegalValues

()

Returns

true

if this parameter has a specified set of
legal values, or

false

otherwise.

boolean

hasMaxValue

()

Returns

true

if this parameter has a specified maximal
value, or

false

otherwise.

boolean

hasMinValue

()

Returns

true

if this parameter has a specified minimal
value, or

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

OpenMBeanParameterInfo

instance.

---

#### Method Summary

Compares the specified

obj

parameter with this

OpenMBeanParameterInfo

instance for equality.

Returns the default value for this parameter, if it has one, or

null

otherwise.

Returns a human readable description of the parameter
described by this

OpenMBeanParameterInfo

instance.

Returns the set of legal values for this parameter, if it has
one, or

null

otherwise.

Returns the maximal value for this parameter, if it has one, or

null

otherwise.

Returns the minimal value for this parameter, if it has one, or

null

otherwise.

Returns the name of the parameter
described by this

OpenMBeanParameterInfo

instance.

Returns the

open type

of the values of the parameter
described by this

OpenMBeanParameterInfo

instance.

Returns

true

if this parameter has a specified default
value, or

false

otherwise.

Returns the hash code value for this

OpenMBeanParameterInfo

instance.

Returns

true

if this parameter has a specified set of
legal values, or

false

otherwise.

Returns

true

if this parameter has a specified maximal
value, or

false

otherwise.

Returns

true

if this parameter has a specified minimal
value, or

false

otherwise.

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

Returns a string representation of this

OpenMBeanParameterInfo

instance.

============ METHOD DETAIL ==========

- Method Detail

- getDescription

```java
String
getDescription()
```

Returns a human readable description of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:** the description.

- getName

```java
String
getName()
```

Returns the name of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:** the name.

- getOpenType

```java
OpenType
<?> getOpenType()
```

Returns the

open type

of the values of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:** the open type.

- getDefaultValue

```java
Object
getDefaultValue()
```

Returns the default value for this parameter, if it has one, or

null

otherwise.

**Returns:** the default value.

- getLegalValues

```java
Set
<?> getLegalValues()
```

Returns the set of legal values for this parameter, if it has
one, or

null

otherwise.

**Returns:** the set of legal values.

- getMinValue

```java
Comparable
<?> getMinValue()
```

Returns the minimal value for this parameter, if it has one, or

null

otherwise.

**Returns:** the minimum value.

- getMaxValue

```java
Comparable
<?> getMaxValue()
```

Returns the maximal value for this parameter, if it has one, or

null

otherwise.

**Returns:** the maximum value.

- hasDefaultValue

```java
boolean hasDefaultValue()
```

Returns

true

if this parameter has a specified default
value, or

false

otherwise.

**Returns:** true if there is a default value.

- hasLegalValues

```java
boolean hasLegalValues()
```

Returns

true

if this parameter has a specified set of
legal values, or

false

otherwise.

**Returns:** true if there is a set of legal values.

- hasMinValue

```java
boolean hasMinValue()
```

Returns

true

if this parameter has a specified minimal
value, or

false

otherwise.

**Returns:** true if there is a minimum value.

- hasMaxValue

```java
boolean hasMaxValue()
```

Returns

true

if this parameter has a specified maximal
value, or

false

otherwise.

**Returns:** true if there is a maximum value.

- isValue

```java
boolean isValue​(
Object
obj)
```

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

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
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanParameterInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanParameterInfo

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanParameterInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanParameterInfo

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanParameterInfo

instance.

The hash code of an

OpenMBeanParameterInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanParameterInfo

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
String
toString()
```

Returns a string representation of this

OpenMBeanParameterInfo

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.OpenMBeanParameterInfo

),
the string representation of the name and open type of the described parameter,
and the string representation of its default, min, max and legal values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanParameterInfo

instance

Method Detail

- getDescription

```java
String
getDescription()
```

Returns a human readable description of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:** the description.

- getName

```java
String
getName()
```

Returns the name of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:** the name.

- getOpenType

```java
OpenType
<?> getOpenType()
```

Returns the

open type

of the values of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:** the open type.

- getDefaultValue

```java
Object
getDefaultValue()
```

Returns the default value for this parameter, if it has one, or

null

otherwise.

**Returns:** the default value.

- getLegalValues

```java
Set
<?> getLegalValues()
```

Returns the set of legal values for this parameter, if it has
one, or

null

otherwise.

**Returns:** the set of legal values.

- getMinValue

```java
Comparable
<?> getMinValue()
```

Returns the minimal value for this parameter, if it has one, or

null

otherwise.

**Returns:** the minimum value.

- getMaxValue

```java
Comparable
<?> getMaxValue()
```

Returns the maximal value for this parameter, if it has one, or

null

otherwise.

**Returns:** the maximum value.

- hasDefaultValue

```java
boolean hasDefaultValue()
```

Returns

true

if this parameter has a specified default
value, or

false

otherwise.

**Returns:** true if there is a default value.

- hasLegalValues

```java
boolean hasLegalValues()
```

Returns

true

if this parameter has a specified set of
legal values, or

false

otherwise.

**Returns:** true if there is a set of legal values.

- hasMinValue

```java
boolean hasMinValue()
```

Returns

true

if this parameter has a specified minimal
value, or

false

otherwise.

**Returns:** true if there is a minimum value.

- hasMaxValue

```java
boolean hasMaxValue()
```

Returns

true

if this parameter has a specified maximal
value, or

false

otherwise.

**Returns:** true if there is a maximum value.

- isValue

```java
boolean isValue​(
Object
obj)
```

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

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
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanParameterInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanParameterInfo

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanParameterInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanParameterInfo

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanParameterInfo

instance.

The hash code of an

OpenMBeanParameterInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanParameterInfo

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
String
toString()
```

Returns a string representation of this

OpenMBeanParameterInfo

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.OpenMBeanParameterInfo

),
the string representation of the name and open type of the described parameter,
and the string representation of its default, min, max and legal values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanParameterInfo

instance

---

#### Method Detail

getDescription

```java
String
getDescription()
```

Returns a human readable description of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:** the description.

---

#### getDescription

String

getDescription()

Returns a human readable description of the parameter
described by this

OpenMBeanParameterInfo

instance.

getName

```java
String
getName()
```

Returns the name of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:** the name.

---

#### getName

String

getName()

Returns the name of the parameter
described by this

OpenMBeanParameterInfo

instance.

getOpenType

```java
OpenType
<?> getOpenType()
```

Returns the

open type

of the values of the parameter
described by this

OpenMBeanParameterInfo

instance.

**Returns:** the open type.

---

#### getOpenType

OpenType

<?> getOpenType()

Returns the

open type

of the values of the parameter
described by this

OpenMBeanParameterInfo

instance.

getDefaultValue

```java
Object
getDefaultValue()
```

Returns the default value for this parameter, if it has one, or

null

otherwise.

**Returns:** the default value.

---

#### getDefaultValue

Object

getDefaultValue()

Returns the default value for this parameter, if it has one, or

null

otherwise.

getLegalValues

```java
Set
<?> getLegalValues()
```

Returns the set of legal values for this parameter, if it has
one, or

null

otherwise.

**Returns:** the set of legal values.

---

#### getLegalValues

Set

<?> getLegalValues()

Returns the set of legal values for this parameter, if it has
one, or

null

otherwise.

getMinValue

```java
Comparable
<?> getMinValue()
```

Returns the minimal value for this parameter, if it has one, or

null

otherwise.

**Returns:** the minimum value.

---

#### getMinValue

Comparable

<?> getMinValue()

Returns the minimal value for this parameter, if it has one, or

null

otherwise.

getMaxValue

```java
Comparable
<?> getMaxValue()
```

Returns the maximal value for this parameter, if it has one, or

null

otherwise.

**Returns:** the maximum value.

---

#### getMaxValue

Comparable

<?> getMaxValue()

Returns the maximal value for this parameter, if it has one, or

null

otherwise.

hasDefaultValue

```java
boolean hasDefaultValue()
```

Returns

true

if this parameter has a specified default
value, or

false

otherwise.

**Returns:** true if there is a default value.

---

#### hasDefaultValue

boolean hasDefaultValue()

Returns

true

if this parameter has a specified default
value, or

false

otherwise.

hasLegalValues

```java
boolean hasLegalValues()
```

Returns

true

if this parameter has a specified set of
legal values, or

false

otherwise.

**Returns:** true if there is a set of legal values.

---

#### hasLegalValues

boolean hasLegalValues()

Returns

true

if this parameter has a specified set of
legal values, or

false

otherwise.

hasMinValue

```java
boolean hasMinValue()
```

Returns

true

if this parameter has a specified minimal
value, or

false

otherwise.

**Returns:** true if there is a minimum value.

---

#### hasMinValue

boolean hasMinValue()

Returns

true

if this parameter has a specified minimal
value, or

false

otherwise.

hasMaxValue

```java
boolean hasMaxValue()
```

Returns

true

if this parameter has a specified maximal
value, or

false

otherwise.

**Returns:** true if there is a maximum value.

---

#### hasMaxValue

boolean hasMaxValue()

Returns

true

if this parameter has a specified maximal
value, or

false

otherwise.

isValue

```java
boolean isValue​(
Object
obj)
```

Tests whether

obj

is a valid value for the parameter
described by this

OpenMBeanParameterInfo

instance.

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

boolean isValue​(

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
boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

OpenMBeanParameterInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanParameterInfo

interface.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this

OpenMBeanParameterInfo

instance;
**Returns:** true

if the specified object is equal to this

OpenMBeanParameterInfo

instance.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Compares the specified

obj

parameter with this

OpenMBeanParameterInfo

instance for equality.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanParameterInfo

interface.

Returns

true

if and only if all of the following statements are true:

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

parameters which are
different implementations of the

OpenMBeanParameterInfo

interface.

obj

is non null,

obj

also implements the

OpenMBeanParameterInfo

interface,

their names are equal

their open types are equal

their default, min, max and legal values are equal.

hashCode

```java
int hashCode()
```

Returns the hash code value for this

OpenMBeanParameterInfo

instance.

The hash code of an

OpenMBeanParameterInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

OpenMBeanParameterInfo

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this

OpenMBeanParameterInfo

instance.

The hash code of an

OpenMBeanParameterInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

The hash code of an

OpenMBeanParameterInfo

instance is the sum of the hash codes
of all elements of information used in

equals

comparisons
(ie: its name, its

open type

, and its default, min, max and legal values).

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

OpenMBeanParameterInfo

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

toString

```java
String
toString()
```

Returns a string representation of this

OpenMBeanParameterInfo

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.OpenMBeanParameterInfo

),
the string representation of the name and open type of the described parameter,
and the string representation of its default, min, max and legal values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

OpenMBeanParameterInfo

instance

---

#### toString

String

toString()

Returns a string representation of this

OpenMBeanParameterInfo

instance.

The string representation consists of the name of this class (ie

javax.management.openmbean.OpenMBeanParameterInfo

),
the string representation of the name and open type of the described parameter,
and the string representation of its default, min, max and legal values.

The string representation consists of the name of this class (ie

javax.management.openmbean.OpenMBeanParameterInfo

),
the string representation of the name and open type of the described parameter,
and the string representation of its default, min, max and legal values.

---

