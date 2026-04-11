# Class UIDefaults.ProxyLazyValue

**Source:** `java.desktop\javax\swing\UIDefaults.ProxyLazyValue.html`

### Class Description

```java
public static class
UIDefaults.ProxyLazyValue

extends
Object

implements
UIDefaults.LazyValue
```

This class provides an implementation of

LazyValue

which can be
used to delay loading of the Class for the instance to be created.
It also avoids creation of an anonymous inner class for the

LazyValue

subclass. Both of these improve performance at the time that a
a Look and Feel is loaded, at the cost of a slight performance
reduction the first time

createValue

is called
(since Reflection APIs are used).

**All Implemented Interfaces:** UIDefaults.LazyValue

---

### Field Details

*No entries found.*

### Constructor Details

#### public ProxyLazyValue​(
String
c)

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:**
- c

- a

String

specifying the classname
of the instance to be created on demand

---

#### public ProxyLazyValue​(
String
c,

String
m)

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:**
- c

- a

String

specifying the classname of
the class
containing a static method to be called for
instance creation
- m

- a

String

specifying the static
method to be called on class c

---

#### public ProxyLazyValue​(
String
c,

Object
[] o)

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:**
- c

- a

String

specifying the classname
of the instance to be created on demand
- o

- an array of

Objects

to be passed as
paramaters to the constructor in class c

---

#### public ProxyLazyValue​(
String
c,

String
m,

Object
[] o)

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:**
- c

- a

String

specifying the classname
of the class
containing a static method to be called for
instance creation.
- m

- a

String

specifying the static method
to be called on class c
- o

- an array of

Objects

to be passed as
paramaters to the static method in class c

---

### Method Details

#### public
Object
createValue​(
UIDefaults
table)

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

**Specified by:**
- createValue

in interface

UIDefaults.LazyValue

**Parameters:**
- table

- a

UIDefaults

table

**Returns:**
- the created

Object

---

### Additional Sections

#### Class UIDefaults.ProxyLazyValue

java.lang.Object

- javax.swing.UIDefaults.ProxyLazyValue

javax.swing.UIDefaults.ProxyLazyValue

**All Implemented Interfaces:** UIDefaults.LazyValue

**Enclosing class:** UIDefaults

```java
public static class
UIDefaults.ProxyLazyValue

extends
Object

implements
UIDefaults.LazyValue
```

This class provides an implementation of

LazyValue

which can be
used to delay loading of the Class for the instance to be created.
It also avoids creation of an anonymous inner class for the

LazyValue

subclass. Both of these improve performance at the time that a
a Look and Feel is loaded, at the cost of a slight performance
reduction the first time

createValue

is called
(since Reflection APIs are used).

**Since:** 1.3

public static class

UIDefaults.ProxyLazyValue

extends

Object

implements

UIDefaults.LazyValue

This class provides an implementation of

LazyValue

which can be
used to delay loading of the Class for the instance to be created.
It also avoids creation of an anonymous inner class for the

LazyValue

subclass. Both of these improve performance at the time that a
a Look and Feel is loaded, at the cost of a slight performance
reduction the first time

createValue

is called
(since Reflection APIs are used).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ProxyLazyValue

​(

String

c)

Creates a

LazyValue

which will construct an instance
when asked.

ProxyLazyValue

​(

String

c,

Object

[] o)

Creates a

LazyValue

which will construct an instance
when asked.

ProxyLazyValue

​(

String

c,

String

m)

Creates a

LazyValue

which will construct an instance
when asked.

ProxyLazyValue

​(

String

c,

String

m,

Object

[] o)

Creates a

LazyValue

which will construct an instance
when asked.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

createValue

​(

UIDefaults

table)

Creates the value retrieved from the

UIDefaults

table.

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

Constructor Summary

Constructors

Constructor

Description

ProxyLazyValue

​(

String

c)

Creates a

LazyValue

which will construct an instance
when asked.

ProxyLazyValue

​(

String

c,

Object

[] o)

Creates a

LazyValue

which will construct an instance
when asked.

ProxyLazyValue

​(

String

c,

String

m)

Creates a

LazyValue

which will construct an instance
when asked.

ProxyLazyValue

​(

String

c,

String

m,

Object

[] o)

Creates a

LazyValue

which will construct an instance
when asked.

---

#### Constructor Summary

Creates a

LazyValue

which will construct an instance
when asked.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

createValue

​(

UIDefaults

table)

Creates the value retrieved from the

UIDefaults

table.

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

---

#### Method Summary

Creates the value retrieved from the

UIDefaults

table.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ProxyLazyValue

```java
public ProxyLazyValue​(
String
c)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname
of the instance to be created on demand

- ProxyLazyValue

```java
public ProxyLazyValue​(
String
c,

String
m)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname of
the class
containing a static method to be called for
instance creation
**Parameters:** m

- a

String

specifying the static
method to be called on class c

- ProxyLazyValue

```java
public ProxyLazyValue​(
String
c,

Object
[] o)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname
of the instance to be created on demand
**Parameters:** o

- an array of

Objects

to be passed as
paramaters to the constructor in class c

- ProxyLazyValue

```java
public ProxyLazyValue​(
String
c,

String
m,

Object
[] o)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname
of the class
containing a static method to be called for
instance creation.
**Parameters:** m

- a

String

specifying the static method
to be called on class c
**Parameters:** o

- an array of

Objects

to be passed as
paramaters to the static method in class c

============ METHOD DETAIL ==========

- Method Detail

- createValue

```java
public
Object
createValue​(
UIDefaults
table)
```

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

**Specified by:** createValue

in interface

UIDefaults.LazyValue
**Parameters:** table

- a

UIDefaults

table
**Returns:** the created

Object

Constructor Detail

- ProxyLazyValue

```java
public ProxyLazyValue​(
String
c)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname
of the instance to be created on demand

- ProxyLazyValue

```java
public ProxyLazyValue​(
String
c,

String
m)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname of
the class
containing a static method to be called for
instance creation
**Parameters:** m

- a

String

specifying the static
method to be called on class c

- ProxyLazyValue

```java
public ProxyLazyValue​(
String
c,

Object
[] o)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname
of the instance to be created on demand
**Parameters:** o

- an array of

Objects

to be passed as
paramaters to the constructor in class c

- ProxyLazyValue

```java
public ProxyLazyValue​(
String
c,

String
m,

Object
[] o)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname
of the class
containing a static method to be called for
instance creation.
**Parameters:** m

- a

String

specifying the static method
to be called on class c
**Parameters:** o

- an array of

Objects

to be passed as
paramaters to the static method in class c

---

#### Constructor Detail

ProxyLazyValue

```java
public ProxyLazyValue​(
String
c)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname
of the instance to be created on demand

---

#### ProxyLazyValue

public ProxyLazyValue​(

String

c)

Creates a

LazyValue

which will construct an instance
when asked.

ProxyLazyValue

```java
public ProxyLazyValue​(
String
c,

String
m)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname of
the class
containing a static method to be called for
instance creation
**Parameters:** m

- a

String

specifying the static
method to be called on class c

---

#### ProxyLazyValue

public ProxyLazyValue​(

String

c,

String

m)

Creates a

LazyValue

which will construct an instance
when asked.

ProxyLazyValue

```java
public ProxyLazyValue​(
String
c,

Object
[] o)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname
of the instance to be created on demand
**Parameters:** o

- an array of

Objects

to be passed as
paramaters to the constructor in class c

---

#### ProxyLazyValue

public ProxyLazyValue​(

String

c,

Object

[] o)

Creates a

LazyValue

which will construct an instance
when asked.

ProxyLazyValue

```java
public ProxyLazyValue​(
String
c,

String
m,

Object
[] o)
```

Creates a

LazyValue

which will construct an instance
when asked.

**Parameters:** c

- a

String

specifying the classname
of the class
containing a static method to be called for
instance creation.
**Parameters:** m

- a

String

specifying the static method
to be called on class c
**Parameters:** o

- an array of

Objects

to be passed as
paramaters to the static method in class c

---

#### ProxyLazyValue

public ProxyLazyValue​(

String

c,

String

m,

Object

[] o)

Creates a

LazyValue

which will construct an instance
when asked.

Method Detail

- createValue

```java
public
Object
createValue​(
UIDefaults
table)
```

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

**Specified by:** createValue

in interface

UIDefaults.LazyValue
**Parameters:** table

- a

UIDefaults

table
**Returns:** the created

Object

---

#### Method Detail

createValue

```java
public
Object
createValue​(
UIDefaults
table)
```

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

**Specified by:** createValue

in interface

UIDefaults.LazyValue
**Parameters:** table

- a

UIDefaults

table
**Returns:** the created

Object

---

#### createValue

public

Object

createValue​(

UIDefaults

table)

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

---

