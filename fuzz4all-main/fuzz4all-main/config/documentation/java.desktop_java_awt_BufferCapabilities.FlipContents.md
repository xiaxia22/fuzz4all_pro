# Class BufferCapabilities.FlipContents

**Source:** `java.desktop\java\awt\BufferCapabilities.FlipContents.html`

### Class Description

```java
public static final class
BufferCapabilities.FlipContents

extends
Object
```

A type-safe enumeration of the possible back buffer contents after
page-flipping

**Enclosing class:** BufferCapabilities

---

### Field Details

#### public static final
BufferCapabilities.FlipContents
UNDEFINED

When flip contents are

UNDEFINED

, the
contents of the back buffer are undefined after flipping.

**See Also:**
- BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

BACKGROUND

,

PRIOR

,

COPIED

---

#### public static final
BufferCapabilities.FlipContents
BACKGROUND

When flip contents are

BACKGROUND

, the
contents of the back buffer are cleared with the background color after
flipping.

**See Also:**
- BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

PRIOR

,

COPIED

---

#### public static final
BufferCapabilities.FlipContents
PRIOR

When flip contents are

PRIOR

, the
contents of the back buffer are the prior contents of the front buffer
(a true page flip).

**See Also:**
- BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

BACKGROUND

,

COPIED

---

#### public static final
BufferCapabilities.FlipContents
COPIED

When flip contents are

COPIED

, the
contents of the back buffer are copied to the front buffer when
flipping.

**See Also:**
- BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

BACKGROUND

,

PRIOR

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

#### Class BufferCapabilities.FlipContents

java.lang.Object

- java.awt.BufferCapabilities.FlipContents

java.awt.BufferCapabilities.FlipContents

**Enclosing class:** BufferCapabilities

```java
public static final class
BufferCapabilities.FlipContents

extends
Object
```

A type-safe enumeration of the possible back buffer contents after
page-flipping

**Since:** 1.4

public static final class

BufferCapabilities.FlipContents

extends

Object

A type-safe enumeration of the possible back buffer contents after
page-flipping

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

BufferCapabilities.FlipContents

BACKGROUND

When flip contents are

BACKGROUND

, the
contents of the back buffer are cleared with the background color after
flipping.

static

BufferCapabilities.FlipContents

COPIED

When flip contents are

COPIED

, the
contents of the back buffer are copied to the front buffer when
flipping.

static

BufferCapabilities.FlipContents

PRIOR

When flip contents are

PRIOR

, the
contents of the back buffer are the prior contents of the front buffer
(a true page flip).

static

BufferCapabilities.FlipContents

UNDEFINED

When flip contents are

UNDEFINED

, the
contents of the back buffer are undefined after flipping.

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

BufferCapabilities.FlipContents

BACKGROUND

When flip contents are

BACKGROUND

, the
contents of the back buffer are cleared with the background color after
flipping.

static

BufferCapabilities.FlipContents

COPIED

When flip contents are

COPIED

, the
contents of the back buffer are copied to the front buffer when
flipping.

static

BufferCapabilities.FlipContents

PRIOR

When flip contents are

PRIOR

, the
contents of the back buffer are the prior contents of the front buffer
(a true page flip).

static

BufferCapabilities.FlipContents

UNDEFINED

When flip contents are

UNDEFINED

, the
contents of the back buffer are undefined after flipping.

---

#### Field Summary

When flip contents are

BACKGROUND

, the
contents of the back buffer are cleared with the background color after
flipping.

When flip contents are

COPIED

, the
contents of the back buffer are copied to the front buffer when
flipping.

When flip contents are

PRIOR

, the
contents of the back buffer are the prior contents of the front buffer
(a true page flip).

When flip contents are

UNDEFINED

, the
contents of the back buffer are undefined after flipping.

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

- UNDEFINED

```java
public static final
BufferCapabilities.FlipContents
UNDEFINED
```

When flip contents are

UNDEFINED

, the
contents of the back buffer are undefined after flipping.

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

BACKGROUND

,

PRIOR

,

COPIED

- BACKGROUND

```java
public static final
BufferCapabilities.FlipContents
BACKGROUND
```

When flip contents are

BACKGROUND

, the
contents of the back buffer are cleared with the background color after
flipping.

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

PRIOR

,

COPIED

- PRIOR

```java
public static final
BufferCapabilities.FlipContents
PRIOR
```

When flip contents are

PRIOR

, the
contents of the back buffer are the prior contents of the front buffer
(a true page flip).

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

BACKGROUND

,

COPIED

- COPIED

```java
public static final
BufferCapabilities.FlipContents
COPIED
```

When flip contents are

COPIED

, the
contents of the back buffer are copied to the front buffer when
flipping.

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

BACKGROUND

,

PRIOR

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

- UNDEFINED

```java
public static final
BufferCapabilities.FlipContents
UNDEFINED
```

When flip contents are

UNDEFINED

, the
contents of the back buffer are undefined after flipping.

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

BACKGROUND

,

PRIOR

,

COPIED

- BACKGROUND

```java
public static final
BufferCapabilities.FlipContents
BACKGROUND
```

When flip contents are

BACKGROUND

, the
contents of the back buffer are cleared with the background color after
flipping.

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

PRIOR

,

COPIED

- PRIOR

```java
public static final
BufferCapabilities.FlipContents
PRIOR
```

When flip contents are

PRIOR

, the
contents of the back buffer are the prior contents of the front buffer
(a true page flip).

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

BACKGROUND

,

COPIED

- COPIED

```java
public static final
BufferCapabilities.FlipContents
COPIED
```

When flip contents are

COPIED

, the
contents of the back buffer are copied to the front buffer when
flipping.

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

BACKGROUND

,

PRIOR

---

#### Field Detail

UNDEFINED

```java
public static final
BufferCapabilities.FlipContents
UNDEFINED
```

When flip contents are

UNDEFINED

, the
contents of the back buffer are undefined after flipping.

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

BACKGROUND

,

PRIOR

,

COPIED

---

#### UNDEFINED

public static final

BufferCapabilities.FlipContents

UNDEFINED

When flip contents are

UNDEFINED

, the
contents of the back buffer are undefined after flipping.

BACKGROUND

```java
public static final
BufferCapabilities.FlipContents
BACKGROUND
```

When flip contents are

BACKGROUND

, the
contents of the back buffer are cleared with the background color after
flipping.

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

PRIOR

,

COPIED

---

#### BACKGROUND

public static final

BufferCapabilities.FlipContents

BACKGROUND

When flip contents are

BACKGROUND

, the
contents of the back buffer are cleared with the background color after
flipping.

PRIOR

```java
public static final
BufferCapabilities.FlipContents
PRIOR
```

When flip contents are

PRIOR

, the
contents of the back buffer are the prior contents of the front buffer
(a true page flip).

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

BACKGROUND

,

COPIED

---

#### PRIOR

public static final

BufferCapabilities.FlipContents

PRIOR

When flip contents are

PRIOR

, the
contents of the back buffer are the prior contents of the front buffer
(a true page flip).

COPIED

```java
public static final
BufferCapabilities.FlipContents
COPIED
```

When flip contents are

COPIED

, the
contents of the back buffer are copied to the front buffer when
flipping.

**See Also:** BufferCapabilities.isPageFlipping()

,

BufferCapabilities.getFlipContents()

,

UNDEFINED

,

BACKGROUND

,

PRIOR

---

#### COPIED

public static final

BufferCapabilities.FlipContents

COPIED

When flip contents are

COPIED

, the
contents of the back buffer are copied to the front buffer when
flipping.

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

