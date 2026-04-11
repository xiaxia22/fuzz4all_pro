# Class StaticClass

**Source:** `jdk.dynalink\jdk\dynalink\beans\StaticClass.html`

### Class Description

```java
public final class
StaticClass

extends
Object

implements
Serializable
```

Object that allows access to the static members of a class (its static
methods, properties, and fields), as well as construction of instances using

StandardOperation.NEW

operation. In Dynalink,

Class

objects
are not treated specially and act as ordinary Java objects; you can use e.g.

GET:PROPERTY:superclass

as a property getter to
invoke

clazz.getSuperclass()

. On the other hand, you can not use

Class

objects to access static members of a class, nor to create new
instances of the class using

NEW

. This is consistent with how

Class

objects behave in Java: in Java, you write e.g.

new BitSet()

instead of

new BitSet.class()

. Similarly, you
write

System.out

and not

System.class.out

. It is this aspect
of using a class name as the constructor and a namespace for static members
that

StaticClass

embodies.

Objects of this class are recognized by the

BeansLinker

as being
special, and operations on them will be linked against the represented class'
static members. The

"class"

synthetic property is additionally
recognized and returns the Java

Class

object, just as in Java

System.class

evaluates to the

Class

object for the
System class. Conversely,

Class

objects exposed through

BeansLinker

expose the

"static"

synthetic property which
returns their

StaticClass

object (there is no equivalent to this in
Java).

In summary, instances of this class act as namespaces for static members and
as constructors for classes, much the same way as specifying a class name in
Java language does, except that in Java this is just a syntactic element,
while in Dynalink they are expressed as actual objects.

StaticClass

objects representing Java array types will act as
constructors taking a single int argument and create an array of the
specified size.

If the class has several constructors,

StandardOperation.NEW

on

StaticClass

will try to select the most specific applicable
constructor. You might want to expose a mechanism in your language for
selecting a constructor with an explicit signature through

BeansLinker.getConstructorMethod(Class, String)

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
StaticClass
forClass​(
Class
<?> clazz)

Retrieves the

StaticClass

instance for the specified class.

**Parameters:**
- clazz

- the class for which the static facet is requested.

**Returns:**
- the

StaticClass

instance representing the specified class.

---

#### public
Class
<?> getRepresentedClass()

Returns the represented Java class.

**Returns:**
- the represented Java class.

---

### Additional Sections

#### Class StaticClass

java.lang.Object

- jdk.dynalink.beans.StaticClass

jdk.dynalink.beans.StaticClass

**All Implemented Interfaces:** Serializable

```java
public final class
StaticClass

extends
Object

implements
Serializable
```

Object that allows access to the static members of a class (its static
methods, properties, and fields), as well as construction of instances using

StandardOperation.NEW

operation. In Dynalink,

Class

objects
are not treated specially and act as ordinary Java objects; you can use e.g.

GET:PROPERTY:superclass

as a property getter to
invoke

clazz.getSuperclass()

. On the other hand, you can not use

Class

objects to access static members of a class, nor to create new
instances of the class using

NEW

. This is consistent with how

Class

objects behave in Java: in Java, you write e.g.

new BitSet()

instead of

new BitSet.class()

. Similarly, you
write

System.out

and not

System.class.out

. It is this aspect
of using a class name as the constructor and a namespace for static members
that

StaticClass

embodies.

Objects of this class are recognized by the

BeansLinker

as being
special, and operations on them will be linked against the represented class'
static members. The

"class"

synthetic property is additionally
recognized and returns the Java

Class

object, just as in Java

System.class

evaluates to the

Class

object for the
System class. Conversely,

Class

objects exposed through

BeansLinker

expose the

"static"

synthetic property which
returns their

StaticClass

object (there is no equivalent to this in
Java).

In summary, instances of this class act as namespaces for static members and
as constructors for classes, much the same way as specifying a class name in
Java language does, except that in Java this is just a syntactic element,
while in Dynalink they are expressed as actual objects.

StaticClass

objects representing Java array types will act as
constructors taking a single int argument and create an array of the
specified size.

If the class has several constructors,

StandardOperation.NEW

on

StaticClass

will try to select the most specific applicable
constructor. You might want to expose a mechanism in your language for
selecting a constructor with an explicit signature through

BeansLinker.getConstructorMethod(Class, String)

.

**See Also:** Serialized Form

public final class

StaticClass

extends

Object

implements

Serializable

Object that allows access to the static members of a class (its static
methods, properties, and fields), as well as construction of instances using

StandardOperation.NEW

operation. In Dynalink,

Class

objects
are not treated specially and act as ordinary Java objects; you can use e.g.

GET:PROPERTY:superclass

as a property getter to
invoke

clazz.getSuperclass()

. On the other hand, you can not use

Class

objects to access static members of a class, nor to create new
instances of the class using

NEW

. This is consistent with how

Class

objects behave in Java: in Java, you write e.g.

new BitSet()

instead of

new BitSet.class()

. Similarly, you
write

System.out

and not

System.class.out

. It is this aspect
of using a class name as the constructor and a namespace for static members
that

StaticClass

embodies.

Objects of this class are recognized by the

BeansLinker

as being
special, and operations on them will be linked against the represented class'
static members. The

"class"

synthetic property is additionally
recognized and returns the Java

Class

object, just as in Java

System.class

evaluates to the

Class

object for the
System class. Conversely,

Class

objects exposed through

BeansLinker

expose the

"static"

synthetic property which
returns their

StaticClass

object (there is no equivalent to this in
Java).

In summary, instances of this class act as namespaces for static members and
as constructors for classes, much the same way as specifying a class name in
Java language does, except that in Java this is just a syntactic element,
while in Dynalink they are expressed as actual objects.

StaticClass

objects representing Java array types will act as
constructors taking a single int argument and create an array of the
specified size.

If the class has several constructors,

StandardOperation.NEW

on

StaticClass

will try to select the most specific applicable
constructor. You might want to expose a mechanism in your language for
selecting a constructor with an explicit signature through

BeansLinker.getConstructorMethod(Class, String)

.

Objects of this class are recognized by the

BeansLinker

as being
special, and operations on them will be linked against the represented class'
static members. The

"class"

synthetic property is additionally
recognized and returns the Java

Class

object, just as in Java

System.class

evaluates to the

Class

object for the
System class. Conversely,

Class

objects exposed through

BeansLinker

expose the

"static"

synthetic property which
returns their

StaticClass

object (there is no equivalent to this in
Java).

In summary, instances of this class act as namespaces for static members and
as constructors for classes, much the same way as specifying a class name in
Java language does, except that in Java this is just a syntactic element,
while in Dynalink they are expressed as actual objects.

StaticClass

objects representing Java array types will act as
constructors taking a single int argument and create an array of the
specified size.

If the class has several constructors,

StandardOperation.NEW

on

StaticClass

will try to select the most specific applicable
constructor. You might want to expose a mechanism in your language for
selecting a constructor with an explicit signature through

BeansLinker.getConstructorMethod(Class, String)

.

In summary, instances of this class act as namespaces for static members and
as constructors for classes, much the same way as specifying a class name in
Java language does, except that in Java this is just a syntactic element,
while in Dynalink they are expressed as actual objects.

StaticClass

objects representing Java array types will act as
constructors taking a single int argument and create an array of the
specified size.

If the class has several constructors,

StandardOperation.NEW

on

StaticClass

will try to select the most specific applicable
constructor. You might want to expose a mechanism in your language for
selecting a constructor with an explicit signature through

BeansLinker.getConstructorMethod(Class, String)

.

StaticClass

objects representing Java array types will act as
constructors taking a single int argument and create an array of the
specified size.

If the class has several constructors,

StandardOperation.NEW

on

StaticClass

will try to select the most specific applicable
constructor. You might want to expose a mechanism in your language for
selecting a constructor with an explicit signature through

BeansLinker.getConstructorMethod(Class, String)

.

If the class has several constructors,

StandardOperation.NEW

on

StaticClass

will try to select the most specific applicable
constructor. You might want to expose a mechanism in your language for
selecting a constructor with an explicit signature through

BeansLinker.getConstructorMethod(Class, String)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

StaticClass

forClass

​(

Class

<?> clazz)

Retrieves the

StaticClass

instance for the specified class.

Class

<?>

getRepresentedClass

()

Returns the represented Java class.

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

StaticClass

forClass

​(

Class

<?> clazz)

Retrieves the

StaticClass

instance for the specified class.

Class

<?>

getRepresentedClass

()

Returns the represented Java class.

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

Retrieves the

StaticClass

instance for the specified class.

Returns the represented Java class.

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

============ METHOD DETAIL ==========

- Method Detail

- forClass

```java
public static
StaticClass
forClass​(
Class
<?> clazz)
```

Retrieves the

StaticClass

instance for the specified class.

**Parameters:** clazz

- the class for which the static facet is requested.
**Returns:** the

StaticClass

instance representing the specified class.

- getRepresentedClass

```java
public
Class
<?> getRepresentedClass()
```

Returns the represented Java class.

**Returns:** the represented Java class.

Method Detail

- forClass

```java
public static
StaticClass
forClass​(
Class
<?> clazz)
```

Retrieves the

StaticClass

instance for the specified class.

**Parameters:** clazz

- the class for which the static facet is requested.
**Returns:** the

StaticClass

instance representing the specified class.

- getRepresentedClass

```java
public
Class
<?> getRepresentedClass()
```

Returns the represented Java class.

**Returns:** the represented Java class.

---

#### Method Detail

forClass

```java
public static
StaticClass
forClass​(
Class
<?> clazz)
```

Retrieves the

StaticClass

instance for the specified class.

**Parameters:** clazz

- the class for which the static facet is requested.
**Returns:** the

StaticClass

instance representing the specified class.

---

#### forClass

public static

StaticClass

forClass​(

Class

<?> clazz)

Retrieves the

StaticClass

instance for the specified class.

getRepresentedClass

```java
public
Class
<?> getRepresentedClass()
```

Returns the represented Java class.

**Returns:** the represented Java class.

---

#### getRepresentedClass

public

Class

<?> getRepresentedClass()

Returns the represented Java class.

---

