# Class RenderingHints.Key

**Source:** `java.desktop\java\awt\RenderingHints.Key.html`

### Class Description

```java
public abstract static class
RenderingHints.Key

extends
Object
```

Defines the base type of all keys used along with the

RenderingHints

class to control various
algorithm choices in the rendering and imaging pipelines.
Instances of this class are immutable and unique which
means that tests for matches can be made using the

==

operator instead of the more expensive

equals()

method.

**Enclosing class:** RenderingHints

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Key​(int privatekey)

Construct a key using the indicated private key. Each
subclass of Key maintains its own unique domain of integer
keys. No two objects with the same integer key and of the
same specific subclass can be constructed. An exception
will be thrown if an attempt is made to construct another
object of a given class with the same integer key as a
pre-existing instance of that subclass of Key.

**Parameters:**
- privatekey

- the specified key

---

### Method Details

#### public abstract boolean isCompatibleValue​(
Object
val)

Returns true if the specified object is a valid value
for this Key.

**Parameters:**
- val

- the

Object

to test for validity

**Returns:**
- true

if

val

is valid;

false

otherwise.

---

#### protected final int intKey()

Returns the private integer key that the subclass
instantiated this Key with.

**Returns:**
- the private integer key that the subclass
instantiated this Key with.

---

#### public final int hashCode()

The hash code for all Key objects will be the same as the
system identity code of the object as defined by the
System.identityHashCode() method.

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

#### public final boolean equals​(
Object
o)

The equals method for all Key objects will return the same
result as the equality operator '=='.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

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

### Additional Sections

#### Class RenderingHints.Key

java.lang.Object

- java.awt.RenderingHints.Key

java.awt.RenderingHints.Key

**Enclosing class:** RenderingHints

```java
public abstract static class
RenderingHints.Key

extends
Object
```

Defines the base type of all keys used along with the

RenderingHints

class to control various
algorithm choices in the rendering and imaging pipelines.
Instances of this class are immutable and unique which
means that tests for matches can be made using the

==

operator instead of the more expensive

equals()

method.

public abstract static class

RenderingHints.Key

extends

Object

Defines the base type of all keys used along with the

RenderingHints

class to control various
algorithm choices in the rendering and imaging pipelines.
Instances of this class are immutable and unique which
means that tests for matches can be made using the

==

operator instead of the more expensive

equals()

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Key

​(int privatekey)

Construct a key using the indicated private key.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

The equals method for all Key objects will return the same
result as the equality operator '=='.

int

hashCode

()

The hash code for all Key objects will be the same as the
system identity code of the object as defined by the
System.identityHashCode() method.

protected int

intKey

()

Returns the private integer key that the subclass
instantiated this Key with.

abstract boolean

isCompatibleValue

​(

Object

val)

Returns true if the specified object is a valid value
for this Key.

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

toString

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

Key

​(int privatekey)

Construct a key using the indicated private key.

---

#### Constructor Summary

Construct a key using the indicated private key.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

The equals method for all Key objects will return the same
result as the equality operator '=='.

int

hashCode

()

The hash code for all Key objects will be the same as the
system identity code of the object as defined by the
System.identityHashCode() method.

protected int

intKey

()

Returns the private integer key that the subclass
instantiated this Key with.

abstract boolean

isCompatibleValue

​(

Object

val)

Returns true if the specified object is a valid value
for this Key.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

The equals method for all Key objects will return the same
result as the equality operator '=='.

The hash code for all Key objects will be the same as the
system identity code of the object as defined by the
System.identityHashCode() method.

Returns the private integer key that the subclass
instantiated this Key with.

Returns true if the specified object is a valid value
for this Key.

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

- Key

```java
protected Key​(int privatekey)
```

Construct a key using the indicated private key. Each
subclass of Key maintains its own unique domain of integer
keys. No two objects with the same integer key and of the
same specific subclass can be constructed. An exception
will be thrown if an attempt is made to construct another
object of a given class with the same integer key as a
pre-existing instance of that subclass of Key.

**Parameters:** privatekey

- the specified key

============ METHOD DETAIL ==========

- Method Detail

- isCompatibleValue

```java
public abstract boolean isCompatibleValue​(
Object
val)
```

Returns true if the specified object is a valid value
for this Key.

**Parameters:** val

- the

Object

to test for validity
**Returns:** true

if

val

is valid;

false

otherwise.

- intKey

```java
protected final int intKey()
```

Returns the private integer key that the subclass
instantiated this Key with.

**Returns:** the private integer key that the subclass
instantiated this Key with.

- hashCode

```java
public final int hashCode()
```

The hash code for all Key objects will be the same as the
system identity code of the object as defined by the
System.identityHashCode() method.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public final boolean equals​(
Object
o)
```

The equals method for all Key objects will return the same
result as the equality operator '=='.

**Overrides:** equals

in class

Object
**Parameters:** o

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- Key

```java
protected Key​(int privatekey)
```

Construct a key using the indicated private key. Each
subclass of Key maintains its own unique domain of integer
keys. No two objects with the same integer key and of the
same specific subclass can be constructed. An exception
will be thrown if an attempt is made to construct another
object of a given class with the same integer key as a
pre-existing instance of that subclass of Key.

**Parameters:** privatekey

- the specified key

---

#### Constructor Detail

Key

```java
protected Key​(int privatekey)
```

Construct a key using the indicated private key. Each
subclass of Key maintains its own unique domain of integer
keys. No two objects with the same integer key and of the
same specific subclass can be constructed. An exception
will be thrown if an attempt is made to construct another
object of a given class with the same integer key as a
pre-existing instance of that subclass of Key.

**Parameters:** privatekey

- the specified key

---

#### Key

protected Key​(int privatekey)

Construct a key using the indicated private key. Each
subclass of Key maintains its own unique domain of integer
keys. No two objects with the same integer key and of the
same specific subclass can be constructed. An exception
will be thrown if an attempt is made to construct another
object of a given class with the same integer key as a
pre-existing instance of that subclass of Key.

Method Detail

- isCompatibleValue

```java
public abstract boolean isCompatibleValue​(
Object
val)
```

Returns true if the specified object is a valid value
for this Key.

**Parameters:** val

- the

Object

to test for validity
**Returns:** true

if

val

is valid;

false

otherwise.

- intKey

```java
protected final int intKey()
```

Returns the private integer key that the subclass
instantiated this Key with.

**Returns:** the private integer key that the subclass
instantiated this Key with.

- hashCode

```java
public final int hashCode()
```

The hash code for all Key objects will be the same as the
system identity code of the object as defined by the
System.identityHashCode() method.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public final boolean equals​(
Object
o)
```

The equals method for all Key objects will return the same
result as the equality operator '=='.

**Overrides:** equals

in class

Object
**Parameters:** o

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

#### Method Detail

isCompatibleValue

```java
public abstract boolean isCompatibleValue​(
Object
val)
```

Returns true if the specified object is a valid value
for this Key.

**Parameters:** val

- the

Object

to test for validity
**Returns:** true

if

val

is valid;

false

otherwise.

---

#### isCompatibleValue

public abstract boolean isCompatibleValue​(

Object

val)

Returns true if the specified object is a valid value
for this Key.

intKey

```java
protected final int intKey()
```

Returns the private integer key that the subclass
instantiated this Key with.

**Returns:** the private integer key that the subclass
instantiated this Key with.

---

#### intKey

protected final int intKey()

Returns the private integer key that the subclass
instantiated this Key with.

hashCode

```java
public final int hashCode()
```

The hash code for all Key objects will be the same as the
system identity code of the object as defined by the
System.identityHashCode() method.

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

The hash code for all Key objects will be the same as the
system identity code of the object as defined by the
System.identityHashCode() method.

equals

```java
public final boolean equals​(
Object
o)
```

The equals method for all Key objects will return the same
result as the equality operator '=='.

**Overrides:** equals

in class

Object
**Parameters:** o

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

o)

The equals method for all Key objects will return the same
result as the equality operator '=='.

---

