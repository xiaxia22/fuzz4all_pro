# Class Character.Subset

**Source:** `java.base\java\lang\Character.Subset.html`

### Class Description

```java
public static class
Character.Subset

extends
Object
```

Instances of this class represent particular subsets of the Unicode
character set. The only family of subsets defined in the

Character

class is

Character.UnicodeBlock

.
Other portions of the Java API may define other subsets for their
own purposes.

**Direct Known Subclasses:** Character.UnicodeBlock

,

InputSubset

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Subset​(
String
name)

Constructs a new

Subset

instance.

**Parameters:**
- name

- The name of this subset

**Throws:**
- NullPointerException

- if name is

null

---

### Method Details

#### public final boolean equals​(
Object
obj)

Compares two

Subset

objects for equality.
This method returns

true

if and only if

this

and the argument refer to the same
object; since this method is

final

, this
guarantee holds for all subclasses.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns the standard hash code as defined by the

Object.hashCode()

method. This method
is

final

in order to ensure that the

equals

and

hashCode

methods will
be consistent in all subclasses.

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

#### public final
String
toString()

Returns the name of this subset.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class Character.Subset

java.lang.Object

- java.lang.Character.Subset

java.lang.Character.Subset

**Direct Known Subclasses:** Character.UnicodeBlock

,

InputSubset

**Enclosing class:** Character

```java
public static class
Character.Subset

extends
Object
```

Instances of this class represent particular subsets of the Unicode
character set. The only family of subsets defined in the

Character

class is

Character.UnicodeBlock

.
Other portions of the Java API may define other subsets for their
own purposes.

**Since:** 1.2

public static class

Character.Subset

extends

Object

Instances of this class represent particular subsets of the Unicode
character set. The only family of subsets defined in the

Character

class is

Character.UnicodeBlock

.
Other portions of the Java API may define other subsets for their
own purposes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Subset

​(

String

name)

Constructs a new

Subset

instance.

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

Compares two

Subset

objects for equality.

int

hashCode

()

Returns the standard hash code as defined by the

Object.hashCode()

method.

String

toString

()

Returns the name of this subset.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Subset

​(

String

name)

Constructs a new

Subset

instance.

---

#### Constructor Summary

Constructs a new

Subset

instance.

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

Compares two

Subset

objects for equality.

int

hashCode

()

Returns the standard hash code as defined by the

Object.hashCode()

method.

String

toString

()

Returns the name of this subset.

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

Compares two

Subset

objects for equality.

Returns the standard hash code as defined by the

Object.hashCode()

method.

Returns the name of this subset.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Subset

```java
protected Subset​(
String
name)
```

Constructs a new

Subset

instance.

**Parameters:** name

- The name of this subset
**Throws:** NullPointerException

- if name is

null

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Compares two

Subset

objects for equality.
This method returns

true

if and only if

this

and the argument refer to the same
object; since this method is

final

, this
guarantee holds for all subclasses.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns the standard hash code as defined by the

Object.hashCode()

method. This method
is

final

in order to ensure that the

equals

and

hashCode

methods will
be consistent in all subclasses.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Returns the name of this subset.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- Subset

```java
protected Subset​(
String
name)
```

Constructs a new

Subset

instance.

**Parameters:** name

- The name of this subset
**Throws:** NullPointerException

- if name is

null

---

#### Constructor Detail

Subset

```java
protected Subset​(
String
name)
```

Constructs a new

Subset

instance.

**Parameters:** name

- The name of this subset
**Throws:** NullPointerException

- if name is

null

---

#### Subset

protected Subset​(

String

name)

Constructs a new

Subset

instance.

Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Compares two

Subset

objects for equality.
This method returns

true

if and only if

this

and the argument refer to the same
object; since this method is

final

, this
guarantee holds for all subclasses.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns the standard hash code as defined by the

Object.hashCode()

method. This method
is

final

in order to ensure that the

equals

and

hashCode

methods will
be consistent in all subclasses.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Returns the name of this subset.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

equals

```java
public final boolean equals​(
Object
obj)
```

Compares two

Subset

objects for equality.
This method returns

true

if and only if

this

and the argument refer to the same
object; since this method is

final

, this
guarantee holds for all subclasses.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Compares two

Subset

objects for equality.
This method returns

true

if and only if

this

and the argument refer to the same
object; since this method is

final

, this
guarantee holds for all subclasses.

hashCode

```java
public final int hashCode()
```

Returns the standard hash code as defined by the

Object.hashCode()

method. This method
is

final

in order to ensure that the

equals

and

hashCode

methods will
be consistent in all subclasses.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns the standard hash code as defined by the

Object.hashCode()

method. This method
is

final

in order to ensure that the

equals

and

hashCode

methods will
be consistent in all subclasses.

toString

```java
public final
String
toString()
```

Returns the name of this subset.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public final

String

toString()

Returns the name of this subset.

---

