# Class ModuleDescriptor.Provides

**Source:** `java.base\java\lang\module\ModuleDescriptor.Provides.html`

### Class Description

```java
public static final class
ModuleDescriptor.Provides

extends
Object

implements
Comparable
<
ModuleDescriptor.Provides
>
```

A service that a module provides one or more implementations of.

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor.Provides

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
service()

Returns the fully qualified class name of the service type.

**Returns:**
- The fully qualified class name of the service type

---

#### public
List
<
String
> providers()

Returns the list of the fully qualified class names of the providers
or provider factories.

**Returns:**
- A non-empty and unmodifiable list of the fully qualified class
names of the providers or provider factories

---

#### public int compareTo​(
ModuleDescriptor.Provides
that)

Compares this provides to another.

Two

Provides

objects are compared by comparing the fully
qualified class name of the service type lexicographically. Where the
class names are equal then the list of the provider class names are
compared by comparing the corresponding elements of both lists
lexicographically and in sequence. Where the lists differ in size,

N

is the size of the shorter list, and the first

N

corresponding elements are equal, then the longer list is considered
to succeed the shorter list.

**Specified by:**
- compareTo

in interface

Comparable

<

ModuleDescriptor.Provides

>

**Parameters:**
- that

- The

Provides

to compare

**Returns:**
- A negative integer, zero, or a positive integer if this provides
is less than, equal to, or greater than the given provides

---

#### public int hashCode()

Computes a hash code for this provides.

The hash code is based upon the service type and the set of
providers. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The hash-code value for this module provides

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
ob)

Tests this provides for equality with the given object.

If the given object is not a

Provides

then this method
returns

false

. Two

Provides

objects are equal if the
service type is equal and the list of providers is equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:**
- equals

in class

Object

**Parameters:**
- ob

- the object to which this object is to be compared

**Returns:**
- true

if, and only if, the given object is a

Provides

that is equal to this

Provides

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a string describing this provides.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string describing this provides

---

### Additional Sections

#### Class ModuleDescriptor.Provides

java.lang.Object

- java.lang.module.ModuleDescriptor.Provides

java.lang.module.ModuleDescriptor.Provides

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor.Provides

>

**Enclosing class:** ModuleDescriptor

```java
public static final class
ModuleDescriptor.Provides

extends
Object

implements
Comparable
<
ModuleDescriptor.Provides
>
```

A service that a module provides one or more implementations of.

**Since:** 9
**See Also:** ModuleDescriptor.provides()

public static final class

ModuleDescriptor.Provides

extends

Object

implements

Comparable

<

ModuleDescriptor.Provides

>

A service that a module provides one or more implementations of.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

ModuleDescriptor.Provides

that)

Compares this provides to another.

boolean

equals

​(

Object

ob)

Tests this provides for equality with the given object.

int

hashCode

()

Computes a hash code for this provides.

List

<

String

>

providers

()

Returns the list of the fully qualified class names of the providers
or provider factories.

String

service

()

Returns the fully qualified class name of the service type.

String

toString

()

Returns a string describing this provides.

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

ModuleDescriptor.Provides

that)

Compares this provides to another.

boolean

equals

​(

Object

ob)

Tests this provides for equality with the given object.

int

hashCode

()

Computes a hash code for this provides.

List

<

String

>

providers

()

Returns the list of the fully qualified class names of the providers
or provider factories.

String

service

()

Returns the fully qualified class name of the service type.

String

toString

()

Returns a string describing this provides.

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

Compares this provides to another.

Tests this provides for equality with the given object.

Computes a hash code for this provides.

Returns the list of the fully qualified class names of the providers
or provider factories.

Returns the fully qualified class name of the service type.

Returns a string describing this provides.

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

============ METHOD DETAIL ==========

- Method Detail

- service

```java
public
String
service()
```

Returns the fully qualified class name of the service type.

**Returns:** The fully qualified class name of the service type

- providers

```java
public
List
<
String
> providers()
```

Returns the list of the fully qualified class names of the providers
or provider factories.

**Returns:** A non-empty and unmodifiable list of the fully qualified class
names of the providers or provider factories

- compareTo

```java
public int compareTo​(
ModuleDescriptor.Provides
that)
```

Compares this provides to another.

Two

Provides

objects are compared by comparing the fully
qualified class name of the service type lexicographically. Where the
class names are equal then the list of the provider class names are
compared by comparing the corresponding elements of both lists
lexicographically and in sequence. Where the lists differ in size,

N

is the size of the shorter list, and the first

N

corresponding elements are equal, then the longer list is considered
to succeed the shorter list.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor.Provides

>
**Parameters:** that

- The

Provides

to compare
**Returns:** A negative integer, zero, or a positive integer if this provides
is less than, equal to, or greater than the given provides

- hashCode

```java
public int hashCode()
```

Computes a hash code for this provides.

The hash code is based upon the service type and the set of
providers. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module provides
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this provides for equality with the given object.

If the given object is not a

Provides

then this method
returns

false

. Two

Provides

objects are equal if the
service type is equal and the list of providers is equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is a

Provides

that is equal to this

Provides
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing this provides.

**Overrides:** toString

in class

Object
**Returns:** A string describing this provides

Method Detail

- service

```java
public
String
service()
```

Returns the fully qualified class name of the service type.

**Returns:** The fully qualified class name of the service type

- providers

```java
public
List
<
String
> providers()
```

Returns the list of the fully qualified class names of the providers
or provider factories.

**Returns:** A non-empty and unmodifiable list of the fully qualified class
names of the providers or provider factories

- compareTo

```java
public int compareTo​(
ModuleDescriptor.Provides
that)
```

Compares this provides to another.

Two

Provides

objects are compared by comparing the fully
qualified class name of the service type lexicographically. Where the
class names are equal then the list of the provider class names are
compared by comparing the corresponding elements of both lists
lexicographically and in sequence. Where the lists differ in size,

N

is the size of the shorter list, and the first

N

corresponding elements are equal, then the longer list is considered
to succeed the shorter list.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor.Provides

>
**Parameters:** that

- The

Provides

to compare
**Returns:** A negative integer, zero, or a positive integer if this provides
is less than, equal to, or greater than the given provides

- hashCode

```java
public int hashCode()
```

Computes a hash code for this provides.

The hash code is based upon the service type and the set of
providers. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module provides
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this provides for equality with the given object.

If the given object is not a

Provides

then this method
returns

false

. Two

Provides

objects are equal if the
service type is equal and the list of providers is equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is a

Provides

that is equal to this

Provides
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing this provides.

**Overrides:** toString

in class

Object
**Returns:** A string describing this provides

---

#### Method Detail

service

```java
public
String
service()
```

Returns the fully qualified class name of the service type.

**Returns:** The fully qualified class name of the service type

---

#### service

public

String

service()

Returns the fully qualified class name of the service type.

providers

```java
public
List
<
String
> providers()
```

Returns the list of the fully qualified class names of the providers
or provider factories.

**Returns:** A non-empty and unmodifiable list of the fully qualified class
names of the providers or provider factories

---

#### providers

public

List

<

String

> providers()

Returns the list of the fully qualified class names of the providers
or provider factories.

compareTo

```java
public int compareTo​(
ModuleDescriptor.Provides
that)
```

Compares this provides to another.

Two

Provides

objects are compared by comparing the fully
qualified class name of the service type lexicographically. Where the
class names are equal then the list of the provider class names are
compared by comparing the corresponding elements of both lists
lexicographically and in sequence. Where the lists differ in size,

N

is the size of the shorter list, and the first

N

corresponding elements are equal, then the longer list is considered
to succeed the shorter list.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor.Provides

>
**Parameters:** that

- The

Provides

to compare
**Returns:** A negative integer, zero, or a positive integer if this provides
is less than, equal to, or greater than the given provides

---

#### compareTo

public int compareTo​(

ModuleDescriptor.Provides

that)

Compares this provides to another.

Two

Provides

objects are compared by comparing the fully
qualified class name of the service type lexicographically. Where the
class names are equal then the list of the provider class names are
compared by comparing the corresponding elements of both lists
lexicographically and in sequence. Where the lists differ in size,

N

is the size of the shorter list, and the first

N

corresponding elements are equal, then the longer list is considered
to succeed the shorter list.

Two

Provides

objects are compared by comparing the fully
qualified class name of the service type lexicographically. Where the
class names are equal then the list of the provider class names are
compared by comparing the corresponding elements of both lists
lexicographically and in sequence. Where the lists differ in size,

N

is the size of the shorter list, and the first

N

corresponding elements are equal, then the longer list is considered
to succeed the shorter list.

hashCode

```java
public int hashCode()
```

Computes a hash code for this provides.

The hash code is based upon the service type and the set of
providers. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module provides
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes a hash code for this provides.

The hash code is based upon the service type and the set of
providers. It satisfies the general contract of the

Object.hashCode

method.

The hash code is based upon the service type and the set of
providers. It satisfies the general contract of the

Object.hashCode

method.

equals

```java
public boolean equals​(
Object
ob)
```

Tests this provides for equality with the given object.

If the given object is not a

Provides

then this method
returns

false

. Two

Provides

objects are equal if the
service type is equal and the list of providers is equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is a

Provides

that is equal to this

Provides
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

ob)

Tests this provides for equality with the given object.

If the given object is not a

Provides

then this method
returns

false

. Two

Provides

objects are equal if the
service type is equal and the list of providers is equal.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not a

Provides

then this method
returns

false

. Two

Provides

objects are equal if the
service type is equal and the list of providers is equal.

This method satisfies the general contract of the

Object.equals

method.

toString

```java
public
String
toString()
```

Returns a string describing this provides.

**Overrides:** toString

in class

Object
**Returns:** A string describing this provides

---

#### toString

public

String

toString()

Returns a string describing this provides.

---

