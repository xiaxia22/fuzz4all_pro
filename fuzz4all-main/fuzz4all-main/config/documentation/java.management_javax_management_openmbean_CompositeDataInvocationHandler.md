# Class CompositeDataInvocationHandler

**Source:** `java.management\javax\management\openmbean\CompositeDataInvocationHandler.html`

### Class Description

```java
public class
CompositeDataInvocationHandler

extends
Object

implements
InvocationHandler
```

An

InvocationHandler

that forwards getter methods to a

CompositeData

. If you have an interface that contains
only getter methods (such as

String getName()

or

boolean isActive()

) then you can use this class in
conjunction with the

Proxy

class to produce an implementation
of the interface where each getter returns the value of the
corresponding item in a

CompositeData

.

For example, suppose you have an interface like this:

```java
public interface NamedNumber {
public int getNumber();
public String getName();
}
```

and a

CompositeData

constructed like this:

```java
CompositeData cd =
new
CompositeDataSupport
(
someCompositeType,
new String[] {"number", "name"},
new Object[] {
5
, "five"}
);
```

then you can construct an object implementing

NamedNumber

and backed by the object

cd

like this:

```java
InvocationHandler handler =
new CompositeDataInvocationHandler(cd);
NamedNumber nn = (NamedNumber)
Proxy.newProxyInstance(NamedNumber.class.getClassLoader(),
new Class[] {NamedNumber.class},
handler);
```

A call to

nn.getNumber()

will then return

5

.

If the first letter of the property defined by a getter is a
capital, then this handler will look first for an item in the

CompositeData

beginning with a capital, then, if that is
not found, for an item beginning with the corresponding lowercase
letter or code point. For a getter called

getNumber()

, the
handler will first look for an item called

Number

, then for

number

. If the getter is called

getnumber()

, then
the item must be called

number

.

If the method given to

invoke

is the method

boolean equals(Object)

inherited from

Object

, then
it will return true if and only if the argument is a

Proxy

whose

InvocationHandler

is also a

CompositeDataInvocationHandler

and whose backing

CompositeData

is equal (not necessarily identical) to this
object's. If the method given to

invoke

is the method

int hashCode()

inherited from

Object

, then it will
return a value that is consistent with this definition of

equals

: if two objects are equal according to

equals

, then
they will have the same

hashCode

.

**All Implemented Interfaces:** InvocationHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### public CompositeDataInvocationHandler​(
CompositeData
compositeData)

Construct a handler backed by the given

CompositeData

.

**Parameters:**
- compositeData

- the

CompositeData

that will supply
information to getters.

**Throws:**
- IllegalArgumentException

- if

compositeData

is null.

---

### Method Details

#### public
CompositeData
getCompositeData()

Return the

CompositeData

that was supplied to the
constructor.

**Returns:**
- the

CompositeData

that this handler is backed
by. This is never null.

---

### Additional Sections

#### Class CompositeDataInvocationHandler

java.lang.Object

- javax.management.openmbean.CompositeDataInvocationHandler

javax.management.openmbean.CompositeDataInvocationHandler

**All Implemented Interfaces:** InvocationHandler

```java
public class
CompositeDataInvocationHandler

extends
Object

implements
InvocationHandler
```

An

InvocationHandler

that forwards getter methods to a

CompositeData

. If you have an interface that contains
only getter methods (such as

String getName()

or

boolean isActive()

) then you can use this class in
conjunction with the

Proxy

class to produce an implementation
of the interface where each getter returns the value of the
corresponding item in a

CompositeData

.

For example, suppose you have an interface like this:

```java
public interface NamedNumber {
public int getNumber();
public String getName();
}
```

and a

CompositeData

constructed like this:

```java
CompositeData cd =
new
CompositeDataSupport
(
someCompositeType,
new String[] {"number", "name"},
new Object[] {
5
, "five"}
);
```

then you can construct an object implementing

NamedNumber

and backed by the object

cd

like this:

```java
InvocationHandler handler =
new CompositeDataInvocationHandler(cd);
NamedNumber nn = (NamedNumber)
Proxy.newProxyInstance(NamedNumber.class.getClassLoader(),
new Class[] {NamedNumber.class},
handler);
```

A call to

nn.getNumber()

will then return

5

.

If the first letter of the property defined by a getter is a
capital, then this handler will look first for an item in the

CompositeData

beginning with a capital, then, if that is
not found, for an item beginning with the corresponding lowercase
letter or code point. For a getter called

getNumber()

, the
handler will first look for an item called

Number

, then for

number

. If the getter is called

getnumber()

, then
the item must be called

number

.

If the method given to

invoke

is the method

boolean equals(Object)

inherited from

Object

, then
it will return true if and only if the argument is a

Proxy

whose

InvocationHandler

is also a

CompositeDataInvocationHandler

and whose backing

CompositeData

is equal (not necessarily identical) to this
object's. If the method given to

invoke

is the method

int hashCode()

inherited from

Object

, then it will
return a value that is consistent with this definition of

equals

: if two objects are equal according to

equals

, then
they will have the same

hashCode

.

**Since:** 1.6

public class

CompositeDataInvocationHandler

extends

Object

implements

InvocationHandler

An

InvocationHandler

that forwards getter methods to a

CompositeData

. If you have an interface that contains
only getter methods (such as

String getName()

or

boolean isActive()

) then you can use this class in
conjunction with the

Proxy

class to produce an implementation
of the interface where each getter returns the value of the
corresponding item in a

CompositeData

.

For example, suppose you have an interface like this:

```java
public interface NamedNumber {
public int getNumber();
public String getName();
}
```

and a

CompositeData

constructed like this:

```java
CompositeData cd =
new
CompositeDataSupport
(
someCompositeType,
new String[] {"number", "name"},
new Object[] {
5
, "five"}
);
```

then you can construct an object implementing

NamedNumber

and backed by the object

cd

like this:

```java
InvocationHandler handler =
new CompositeDataInvocationHandler(cd);
NamedNumber nn = (NamedNumber)
Proxy.newProxyInstance(NamedNumber.class.getClassLoader(),
new Class[] {NamedNumber.class},
handler);
```

A call to

nn.getNumber()

will then return

5

.

If the first letter of the property defined by a getter is a
capital, then this handler will look first for an item in the

CompositeData

beginning with a capital, then, if that is
not found, for an item beginning with the corresponding lowercase
letter or code point. For a getter called

getNumber()

, the
handler will first look for an item called

Number

, then for

number

. If the getter is called

getnumber()

, then
the item must be called

number

.

If the method given to

invoke

is the method

boolean equals(Object)

inherited from

Object

, then
it will return true if and only if the argument is a

Proxy

whose

InvocationHandler

is also a

CompositeDataInvocationHandler

and whose backing

CompositeData

is equal (not necessarily identical) to this
object's. If the method given to

invoke

is the method

int hashCode()

inherited from

Object

, then it will
return a value that is consistent with this definition of

equals

: if two objects are equal according to

equals

, then
they will have the same

hashCode

.

An

InvocationHandler

that forwards getter methods to a

CompositeData

. If you have an interface that contains
only getter methods (such as

String getName()

or

boolean isActive()

) then you can use this class in
conjunction with the

Proxy

class to produce an implementation
of the interface where each getter returns the value of the
corresponding item in a

CompositeData

.

For example, suppose you have an interface like this:

```java
public interface NamedNumber {
public int getNumber();
public String getName();
}
```

and a

CompositeData

constructed like this:

```java
CompositeData cd =
new
CompositeDataSupport
(
someCompositeType,
new String[] {"number", "name"},
new Object[] {
5
, "five"}
);
```

then you can construct an object implementing

NamedNumber

and backed by the object

cd

like this:

```java
InvocationHandler handler =
new CompositeDataInvocationHandler(cd);
NamedNumber nn = (NamedNumber)
Proxy.newProxyInstance(NamedNumber.class.getClassLoader(),
new Class[] {NamedNumber.class},
handler);
```

A call to

nn.getNumber()

will then return

5

.

If the first letter of the property defined by a getter is a
capital, then this handler will look first for an item in the

CompositeData

beginning with a capital, then, if that is
not found, for an item beginning with the corresponding lowercase
letter or code point. For a getter called

getNumber()

, the
handler will first look for an item called

Number

, then for

number

. If the getter is called

getnumber()

, then
the item must be called

number

.

If the method given to

invoke

is the method

boolean equals(Object)

inherited from

Object

, then
it will return true if and only if the argument is a

Proxy

whose

InvocationHandler

is also a

CompositeDataInvocationHandler

and whose backing

CompositeData

is equal (not necessarily identical) to this
object's. If the method given to

invoke

is the method

int hashCode()

inherited from

Object

, then it will
return a value that is consistent with this definition of

equals

: if two objects are equal according to

equals

, then
they will have the same

hashCode

.

public interface NamedNumber {
public int getNumber();
public String getName();
}

CompositeData cd =
new

CompositeDataSupport

(
someCompositeType,
new String[] {"number", "name"},
new Object[] {

5

, "five"}
);

InvocationHandler handler =
new CompositeDataInvocationHandler(cd);
NamedNumber nn = (NamedNumber)
Proxy.newProxyInstance(NamedNumber.class.getClassLoader(),
new Class[] {NamedNumber.class},
handler);

If the first letter of the property defined by a getter is a
capital, then this handler will look first for an item in the

CompositeData

beginning with a capital, then, if that is
not found, for an item beginning with the corresponding lowercase
letter or code point. For a getter called

getNumber()

, the
handler will first look for an item called

Number

, then for

number

. If the getter is called

getnumber()

, then
the item must be called

number

.

If the method given to

invoke

is the method

boolean equals(Object)

inherited from

Object

, then
it will return true if and only if the argument is a

Proxy

whose

InvocationHandler

is also a

CompositeDataInvocationHandler

and whose backing

CompositeData

is equal (not necessarily identical) to this
object's. If the method given to

invoke

is the method

int hashCode()

inherited from

Object

, then it will
return a value that is consistent with this definition of

equals

: if two objects are equal according to

equals

, then
they will have the same

hashCode

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CompositeDataInvocationHandler

​(

CompositeData

compositeData)

Construct a handler backed by the given

CompositeData

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CompositeData

getCompositeData

()

Return the

CompositeData

that was supplied to the
constructor.

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

- Methods declared in interface java.lang.reflect.

InvocationHandler

invoke

Constructor Summary

Constructors

Constructor

Description

CompositeDataInvocationHandler

​(

CompositeData

compositeData)

Construct a handler backed by the given

CompositeData

.

---

#### Constructor Summary

Construct a handler backed by the given

CompositeData

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CompositeData

getCompositeData

()

Return the

CompositeData

that was supplied to the
constructor.

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

- Methods declared in interface java.lang.reflect.

InvocationHandler

invoke

---

#### Method Summary

Return the

CompositeData

that was supplied to the
constructor.

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

Methods declared in interface java.lang.reflect.

InvocationHandler

invoke

---

#### Methods declared in interface java.lang.reflect. InvocationHandler

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CompositeDataInvocationHandler

```java
public CompositeDataInvocationHandler​(
CompositeData
compositeData)
```

Construct a handler backed by the given

CompositeData

.

**Parameters:** compositeData

- the

CompositeData

that will supply
information to getters.
**Throws:** IllegalArgumentException

- if

compositeData

is null.

============ METHOD DETAIL ==========

- Method Detail

- getCompositeData

```java
public
CompositeData
getCompositeData()
```

Return the

CompositeData

that was supplied to the
constructor.

**Returns:** the

CompositeData

that this handler is backed
by. This is never null.

Constructor Detail

- CompositeDataInvocationHandler

```java
public CompositeDataInvocationHandler​(
CompositeData
compositeData)
```

Construct a handler backed by the given

CompositeData

.

**Parameters:** compositeData

- the

CompositeData

that will supply
information to getters.
**Throws:** IllegalArgumentException

- if

compositeData

is null.

---

#### Constructor Detail

CompositeDataInvocationHandler

```java
public CompositeDataInvocationHandler​(
CompositeData
compositeData)
```

Construct a handler backed by the given

CompositeData

.

**Parameters:** compositeData

- the

CompositeData

that will supply
information to getters.
**Throws:** IllegalArgumentException

- if

compositeData

is null.

---

#### CompositeDataInvocationHandler

public CompositeDataInvocationHandler​(

CompositeData

compositeData)

Construct a handler backed by the given

CompositeData

.

Method Detail

- getCompositeData

```java
public
CompositeData
getCompositeData()
```

Return the

CompositeData

that was supplied to the
constructor.

**Returns:** the

CompositeData

that this handler is backed
by. This is never null.

---

#### Method Detail

getCompositeData

```java
public
CompositeData
getCompositeData()
```

Return the

CompositeData

that was supplied to the
constructor.

**Returns:** the

CompositeData

that this handler is backed
by. This is never null.

---

#### getCompositeData

public

CompositeData

getCompositeData()

Return the

CompositeData

that was supplied to the
constructor.

---

