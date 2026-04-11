# Class JobAttributes.DefaultSelectionType

**Source:** `java.desktop\java\awt\JobAttributes.DefaultSelectionType.html`

### Class Description

```java
public static final class
JobAttributes.DefaultSelectionType

extends
Object
```

A type-safe enumeration of possible default selection states.

**Enclosing class:** JobAttributes

---

### Field Details

#### public static final
JobAttributes.DefaultSelectionType
ALL

The

DefaultSelectionType

instance to use for
specifying that all pages of the job should be printed.

---

#### public static final
JobAttributes.DefaultSelectionType
RANGE

The

DefaultSelectionType

instance to use for
specifying that a range of pages of the job should be printed.

---

#### public static final
JobAttributes.DefaultSelectionType
SELECTION

The

DefaultSelectionType

instance to use for
specifying that the current selection should be printed.

---

### Constructor Details

*No entries found.*

### Method Details

#### public int hashCode()

Description copied from class:

Object

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

Description copied from class:

Object

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class JobAttributes.DefaultSelectionType

java.lang.Object

- java.awt.JobAttributes.DefaultSelectionType

java.awt.JobAttributes.DefaultSelectionType

**Enclosing class:** JobAttributes

```java
public static final class
JobAttributes.DefaultSelectionType

extends
Object
```

A type-safe enumeration of possible default selection states.

**Since:** 1.3

public static final class

JobAttributes.DefaultSelectionType

extends

Object

A type-safe enumeration of possible default selection states.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

JobAttributes.DefaultSelectionType

ALL

The

DefaultSelectionType

instance to use for
specifying that all pages of the job should be printed.

static

JobAttributes.DefaultSelectionType

RANGE

The

DefaultSelectionType

instance to use for
specifying that a range of pages of the job should be printed.

static

JobAttributes.DefaultSelectionType

SELECTION

The

DefaultSelectionType

instance to use for
specifying that the current selection should be printed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

hashCode

()

Returns a hash code value for the object.

String

toString

()

Returns a string representation of the object.

- Methods declared in class java.lang.

Object

clone

,

equals

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

JobAttributes.DefaultSelectionType

ALL

The

DefaultSelectionType

instance to use for
specifying that all pages of the job should be printed.

static

JobAttributes.DefaultSelectionType

RANGE

The

DefaultSelectionType

instance to use for
specifying that a range of pages of the job should be printed.

static

JobAttributes.DefaultSelectionType

SELECTION

The

DefaultSelectionType

instance to use for
specifying that the current selection should be printed.

---

#### Field Summary

The

DefaultSelectionType

instance to use for
specifying that all pages of the job should be printed.

The

DefaultSelectionType

instance to use for
specifying that a range of pages of the job should be printed.

The

DefaultSelectionType

instance to use for
specifying that the current selection should be printed.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

hashCode

()

Returns a hash code value for the object.

String

toString

()

Returns a string representation of the object.

- Methods declared in class java.lang.

Object

clone

,

equals

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

Returns a hash code value for the object.

Returns a string representation of the object.

Methods declared in class java.lang.

Object

clone

,

equals

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

- ALL

```java
public static final
JobAttributes.DefaultSelectionType
ALL
```

The

DefaultSelectionType

instance to use for
specifying that all pages of the job should be printed.

- RANGE

```java
public static final
JobAttributes.DefaultSelectionType
RANGE
```

The

DefaultSelectionType

instance to use for
specifying that a range of pages of the job should be printed.

- SELECTION

```java
public static final
JobAttributes.DefaultSelectionType
SELECTION
```

The

DefaultSelectionType

instance to use for
specifying that the current selection should be printed.

============ METHOD DETAIL ==========

- Method Detail

- hashCode

```java
public int hashCode()
```

Description copied from class:

Object

Returns a hash code value for the object. This method is
supported for the benefit of hash tables such as those provided by

HashMap

.

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

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

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Field Detail

- ALL

```java
public static final
JobAttributes.DefaultSelectionType
ALL
```

The

DefaultSelectionType

instance to use for
specifying that all pages of the job should be printed.

- RANGE

```java
public static final
JobAttributes.DefaultSelectionType
RANGE
```

The

DefaultSelectionType

instance to use for
specifying that a range of pages of the job should be printed.

- SELECTION

```java
public static final
JobAttributes.DefaultSelectionType
SELECTION
```

The

DefaultSelectionType

instance to use for
specifying that the current selection should be printed.

---

#### Field Detail

ALL

```java
public static final
JobAttributes.DefaultSelectionType
ALL
```

The

DefaultSelectionType

instance to use for
specifying that all pages of the job should be printed.

---

#### ALL

public static final

JobAttributes.DefaultSelectionType

ALL

The

DefaultSelectionType

instance to use for
specifying that all pages of the job should be printed.

RANGE

```java
public static final
JobAttributes.DefaultSelectionType
RANGE
```

The

DefaultSelectionType

instance to use for
specifying that a range of pages of the job should be printed.

---

#### RANGE

public static final

JobAttributes.DefaultSelectionType

RANGE

The

DefaultSelectionType

instance to use for
specifying that a range of pages of the job should be printed.

SELECTION

```java
public static final
JobAttributes.DefaultSelectionType
SELECTION
```

The

DefaultSelectionType

instance to use for
specifying that the current selection should be printed.

---

#### SELECTION

public static final

JobAttributes.DefaultSelectionType

SELECTION

The

DefaultSelectionType

instance to use for
specifying that the current selection should be printed.

Method Detail

- hashCode

```java
public int hashCode()
```

Description copied from class:

Object

Returns a hash code value for the object. This method is
supported for the benefit of hash tables such as those provided by

HashMap

.

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

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

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

hashCode

```java
public int hashCode()
```

Description copied from class:

Object

Returns a hash code value for the object. This method is
supported for the benefit of hash tables such as those provided by

HashMap

.

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

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

Description copied from class:

Object

Returns a hash code value for the object. This method is
supported for the benefit of hash tables such as those provided by

HashMap

.

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

toString

```java
public
String
toString()
```

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

getClass().getName() + '@' + Integer.toHexString(hashCode())

---

