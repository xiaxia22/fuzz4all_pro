# Class AttributeSetUtilities

**Source:** `java.desktop\javax\print\attribute\AttributeSetUtilities.html`

### Class Description

```java
public final class
AttributeSetUtilities

extends
Object
```

Class

AttributeSetUtilities

provides static methods for manipulating

AttributeSets

.

- Methods for creating unmodifiable and synchronized views of attribute
sets.

operations useful for building implementations of interface

AttributeSet

An

unmodifiable view

U

of an

AttributeSet

S

provides a client with "read-only" access to

S

. Query operations on

U

"read through" to

S

; thus, changes in

S

are reflected
in

U

. However, any attempt to modify

U

, results in an

UnmodifiableSetException

. The unmodifiable view object

U

will
be serializable if the attribute set object

S

is serializable.

A

synchronized view

V

of an attribute set

S

provides a
client with synchronized (multiple thread safe) access to

S

. Each
operation of

V

is synchronized using

V

itself as the lock
object and then merely invokes the corresponding operation of

S

. In
order to guarantee mutually exclusive access, it is critical that all access
to

S

is accomplished through

V

. The synchronized view object

V

will be serializable if the attribute set object

S

is
serializable.

As mentioned in the package description of

javax.print

, a

null

reference parameter to methods is incorrect unless explicitly
documented on the method as having a meaningful interpretation. Usage to the
contrary is incorrect coding and may result in a run time exception either
immediately or at some later time.

IllegalArgumentException

and

NullPointerException

are examples of typical and acceptable run time
exceptions for such cases.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
AttributeSet
unmodifiableView​(
AttributeSet
attributeSet)

Creates an unmodifiable view of the given attribute set.

**Parameters:**
- attributeSet

- underlying attribute set

**Returns:**
- unmodifiable view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
DocAttributeSet
unmodifiableView​(
DocAttributeSet
attributeSet)

Creates an unmodifiable view of the given doc attribute set.

**Parameters:**
- attributeSet

- underlying doc attribute set

**Returns:**
- unmodifiable view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
PrintRequestAttributeSet
unmodifiableView​(
PrintRequestAttributeSet
attributeSet)

Creates an unmodifiable view of the given print request attribute set.

**Parameters:**
- attributeSet

- underlying print request attribute set

**Returns:**
- unmodifiable view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
PrintJobAttributeSet
unmodifiableView​(
PrintJobAttributeSet
attributeSet)

Creates an unmodifiable view of the given print job attribute set.

**Parameters:**
- attributeSet

- underlying print job attribute set

**Returns:**
- unmodifiable view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
PrintServiceAttributeSet
unmodifiableView​(
PrintServiceAttributeSet
attributeSet)

Creates an unmodifiable view of the given print service attribute set.

**Parameters:**
- attributeSet

- underlying print service attribute set

**Returns:**
- unmodifiable view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
AttributeSet
synchronizedView​(
AttributeSet
attributeSet)

Creates a synchronized view of the given attribute set.

**Parameters:**
- attributeSet

- underlying attribute set

**Returns:**
- synchronized view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
DocAttributeSet
synchronizedView​(
DocAttributeSet
attributeSet)

Creates a synchronized view of the given doc attribute set.

**Parameters:**
- attributeSet

- underlying doc attribute set

**Returns:**
- synchronized view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
PrintRequestAttributeSet
synchronizedView​(
PrintRequestAttributeSet
attributeSet)

Creates a synchronized view of the given print request attribute set.

**Parameters:**
- attributeSet

- underlying print request attribute set

**Returns:**
- synchronized view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
PrintJobAttributeSet
synchronizedView​(
PrintJobAttributeSet
attributeSet)

Creates a synchronized view of the given print job attribute set.

**Parameters:**
- attributeSet

- underlying print job attribute set

**Returns:**
- synchronized view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
PrintServiceAttributeSet
synchronizedView​(
PrintServiceAttributeSet
attributeSet)

Creates a synchronized view of the given print service attribute set.

**Parameters:**
- attributeSet

- underlying print service attribute set

**Returns:**
- synchronized view of

attributeSet

**Throws:**
- NullPointerException

- if

attributeSet

is

null

---

#### public static
Class
<?> verifyAttributeCategory​(
Object
object,

Class
<?> interfaceName)

Verify that the given object is a

Class

that implements the
given interface, which is assumed to be interface

Attribute

or a subinterface thereof.

**Parameters:**
- object

-

Object

to test
- interfaceName

- interface the object must implement

**Returns:**
- if

object

is a

Class

that implements

interfaceName

,

object

is returned downcast to
type

Class

; otherwise an exception is thrown

**Throws:**
- NullPointerException

- if

object

is

null
- ClassCastException

- if

object

is not a

Class

that implements

interfaceName

---

#### public static
Attribute
verifyAttributeValue​(
Object
object,

Class
<?> interfaceName)

Verify that the given object is an instance of the given interface, which
is assumed to be interface

Attribute

or a subinterface
thereof.

**Parameters:**
- object

-

Object

to test
- interfaceName

- interface of which the object must be an instance

**Returns:**
- if

object

is an instance of

interfaceName

,

object

is returned downcast to type

Attribute

; otherwise an exception is thrown

**Throws:**
- NullPointerException

- if

object

is

null
- ClassCastException

- if

object

is not an instance of

interfaceName

---

#### public static void verifyCategoryForValue​(
Class
<?> category,

Attribute
attribute)

Verify that the given attribute category object is equal to the category
of the given attribute value object. If so, this method returns doing
nothing. If not, this method throws an exception.

**Parameters:**
- category

- attribute category to test
- attribute

- attribute value to test

**Throws:**
- NullPointerException

- if the

category

or

attribute

are

null
- IllegalArgumentException

- if the

category

is not equal to
the category of the

attribute

---

### Additional Sections

#### Class AttributeSetUtilities

java.lang.Object

- javax.print.attribute.AttributeSetUtilities

javax.print.attribute.AttributeSetUtilities

```java
public final class
AttributeSetUtilities

extends
Object
```

Class

AttributeSetUtilities

provides static methods for manipulating

AttributeSets

.

- Methods for creating unmodifiable and synchronized views of attribute
sets.

operations useful for building implementations of interface

AttributeSet

An

unmodifiable view

U

of an

AttributeSet

S

provides a client with "read-only" access to

S

. Query operations on

U

"read through" to

S

; thus, changes in

S

are reflected
in

U

. However, any attempt to modify

U

, results in an

UnmodifiableSetException

. The unmodifiable view object

U

will
be serializable if the attribute set object

S

is serializable.

A

synchronized view

V

of an attribute set

S

provides a
client with synchronized (multiple thread safe) access to

S

. Each
operation of

V

is synchronized using

V

itself as the lock
object and then merely invokes the corresponding operation of

S

. In
order to guarantee mutually exclusive access, it is critical that all access
to

S

is accomplished through

V

. The synchronized view object

V

will be serializable if the attribute set object

S

is
serializable.

As mentioned in the package description of

javax.print

, a

null

reference parameter to methods is incorrect unless explicitly
documented on the method as having a meaningful interpretation. Usage to the
contrary is incorrect coding and may result in a run time exception either
immediately or at some later time.

IllegalArgumentException

and

NullPointerException

are examples of typical and acceptable run time
exceptions for such cases.

public final class

AttributeSetUtilities

extends

Object

Class

AttributeSetUtilities

provides static methods for manipulating

AttributeSets

.

- Methods for creating unmodifiable and synchronized views of attribute
sets.

operations useful for building implementations of interface

AttributeSet

An

unmodifiable view

U

of an

AttributeSet

S

provides a client with "read-only" access to

S

. Query operations on

U

"read through" to

S

; thus, changes in

S

are reflected
in

U

. However, any attempt to modify

U

, results in an

UnmodifiableSetException

. The unmodifiable view object

U

will
be serializable if the attribute set object

S

is serializable.

A

synchronized view

V

of an attribute set

S

provides a
client with synchronized (multiple thread safe) access to

S

. Each
operation of

V

is synchronized using

V

itself as the lock
object and then merely invokes the corresponding operation of

S

. In
order to guarantee mutually exclusive access, it is critical that all access
to

S

is accomplished through

V

. The synchronized view object

V

will be serializable if the attribute set object

S

is
serializable.

As mentioned in the package description of

javax.print

, a

null

reference parameter to methods is incorrect unless explicitly
documented on the method as having a meaningful interpretation. Usage to the
contrary is incorrect coding and may result in a run time exception either
immediately or at some later time.

IllegalArgumentException

and

NullPointerException

are examples of typical and acceptable run time
exceptions for such cases.

Methods for creating unmodifiable and synchronized views of attribute
sets.

operations useful for building implementations of interface

AttributeSet

A

synchronized view

V

of an attribute set

S

provides a
client with synchronized (multiple thread safe) access to

S

. Each
operation of

V

is synchronized using

V

itself as the lock
object and then merely invokes the corresponding operation of

S

. In
order to guarantee mutually exclusive access, it is critical that all access
to

S

is accomplished through

V

. The synchronized view object

V

will be serializable if the attribute set object

S

is
serializable.

As mentioned in the package description of

javax.print

, a

null

reference parameter to methods is incorrect unless explicitly
documented on the method as having a meaningful interpretation. Usage to the
contrary is incorrect coding and may result in a run time exception either
immediately or at some later time.

IllegalArgumentException

and

NullPointerException

are examples of typical and acceptable run time
exceptions for such cases.

As mentioned in the package description of

javax.print

, a

null

reference parameter to methods is incorrect unless explicitly
documented on the method as having a meaningful interpretation. Usage to the
contrary is incorrect coding and may result in a run time exception either
immediately or at some later time.

IllegalArgumentException

and

NullPointerException

are examples of typical and acceptable run time
exceptions for such cases.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AttributeSet

synchronizedView

​(

AttributeSet

attributeSet)

Creates a synchronized view of the given attribute set.

static

DocAttributeSet

synchronizedView

​(

DocAttributeSet

attributeSet)

Creates a synchronized view of the given doc attribute set.

static

PrintJobAttributeSet

synchronizedView

​(

PrintJobAttributeSet

attributeSet)

Creates a synchronized view of the given print job attribute set.

static

PrintRequestAttributeSet

synchronizedView

​(

PrintRequestAttributeSet

attributeSet)

Creates a synchronized view of the given print request attribute set.

static

PrintServiceAttributeSet

synchronizedView

​(

PrintServiceAttributeSet

attributeSet)

Creates a synchronized view of the given print service attribute set.

static

AttributeSet

unmodifiableView

​(

AttributeSet

attributeSet)

Creates an unmodifiable view of the given attribute set.

static

DocAttributeSet

unmodifiableView

​(

DocAttributeSet

attributeSet)

Creates an unmodifiable view of the given doc attribute set.

static

PrintJobAttributeSet

unmodifiableView

​(

PrintJobAttributeSet

attributeSet)

Creates an unmodifiable view of the given print job attribute set.

static

PrintRequestAttributeSet

unmodifiableView

​(

PrintRequestAttributeSet

attributeSet)

Creates an unmodifiable view of the given print request attribute set.

static

PrintServiceAttributeSet

unmodifiableView

​(

PrintServiceAttributeSet

attributeSet)

Creates an unmodifiable view of the given print service attribute set.

static

Class

<?>

verifyAttributeCategory

​(

Object

object,

Class

<?> interfaceName)

Verify that the given object is a

Class

that implements the
given interface, which is assumed to be interface

Attribute

or a subinterface thereof.

static

Attribute

verifyAttributeValue

​(

Object

object,

Class

<?> interfaceName)

Verify that the given object is an instance of the given interface, which
is assumed to be interface

Attribute

or a subinterface
thereof.

static void

verifyCategoryForValue

​(

Class

<?> category,

Attribute

attribute)

Verify that the given attribute category object is equal to the category
of the given attribute value object.

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

Concrete Methods

Modifier and Type

Method

Description

static

AttributeSet

synchronizedView

​(

AttributeSet

attributeSet)

Creates a synchronized view of the given attribute set.

static

DocAttributeSet

synchronizedView

​(

DocAttributeSet

attributeSet)

Creates a synchronized view of the given doc attribute set.

static

PrintJobAttributeSet

synchronizedView

​(

PrintJobAttributeSet

attributeSet)

Creates a synchronized view of the given print job attribute set.

static

PrintRequestAttributeSet

synchronizedView

​(

PrintRequestAttributeSet

attributeSet)

Creates a synchronized view of the given print request attribute set.

static

PrintServiceAttributeSet

synchronizedView

​(

PrintServiceAttributeSet

attributeSet)

Creates a synchronized view of the given print service attribute set.

static

AttributeSet

unmodifiableView

​(

AttributeSet

attributeSet)

Creates an unmodifiable view of the given attribute set.

static

DocAttributeSet

unmodifiableView

​(

DocAttributeSet

attributeSet)

Creates an unmodifiable view of the given doc attribute set.

static

PrintJobAttributeSet

unmodifiableView

​(

PrintJobAttributeSet

attributeSet)

Creates an unmodifiable view of the given print job attribute set.

static

PrintRequestAttributeSet

unmodifiableView

​(

PrintRequestAttributeSet

attributeSet)

Creates an unmodifiable view of the given print request attribute set.

static

PrintServiceAttributeSet

unmodifiableView

​(

PrintServiceAttributeSet

attributeSet)

Creates an unmodifiable view of the given print service attribute set.

static

Class

<?>

verifyAttributeCategory

​(

Object

object,

Class

<?> interfaceName)

Verify that the given object is a

Class

that implements the
given interface, which is assumed to be interface

Attribute

or a subinterface thereof.

static

Attribute

verifyAttributeValue

​(

Object

object,

Class

<?> interfaceName)

Verify that the given object is an instance of the given interface, which
is assumed to be interface

Attribute

or a subinterface
thereof.

static void

verifyCategoryForValue

​(

Class

<?> category,

Attribute

attribute)

Verify that the given attribute category object is equal to the category
of the given attribute value object.

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

Creates a synchronized view of the given attribute set.

Creates a synchronized view of the given doc attribute set.

Creates a synchronized view of the given print job attribute set.

Creates a synchronized view of the given print request attribute set.

Creates a synchronized view of the given print service attribute set.

Creates an unmodifiable view of the given attribute set.

Creates an unmodifiable view of the given doc attribute set.

Creates an unmodifiable view of the given print job attribute set.

Creates an unmodifiable view of the given print request attribute set.

Creates an unmodifiable view of the given print service attribute set.

Verify that the given object is a

Class

that implements the
given interface, which is assumed to be interface

Attribute

or a subinterface thereof.

Verify that the given object is an instance of the given interface, which
is assumed to be interface

Attribute

or a subinterface
thereof.

Verify that the given attribute category object is equal to the category
of the given attribute value object.

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

- unmodifiableView

```java
public static
AttributeSet
unmodifiableView​(
AttributeSet
attributeSet)
```

Creates an unmodifiable view of the given attribute set.

**Parameters:** attributeSet

- underlying attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- unmodifiableView

```java
public static
DocAttributeSet
unmodifiableView​(
DocAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given doc attribute set.

**Parameters:** attributeSet

- underlying doc attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- unmodifiableView

```java
public static
PrintRequestAttributeSet
unmodifiableView​(
PrintRequestAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given print request attribute set.

**Parameters:** attributeSet

- underlying print request attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- unmodifiableView

```java
public static
PrintJobAttributeSet
unmodifiableView​(
PrintJobAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given print job attribute set.

**Parameters:** attributeSet

- underlying print job attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- unmodifiableView

```java
public static
PrintServiceAttributeSet
unmodifiableView​(
PrintServiceAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given print service attribute set.

**Parameters:** attributeSet

- underlying print service attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
AttributeSet
synchronizedView​(
AttributeSet
attributeSet)
```

Creates a synchronized view of the given attribute set.

**Parameters:** attributeSet

- underlying attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
DocAttributeSet
synchronizedView​(
DocAttributeSet
attributeSet)
```

Creates a synchronized view of the given doc attribute set.

**Parameters:** attributeSet

- underlying doc attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
PrintRequestAttributeSet
synchronizedView​(
PrintRequestAttributeSet
attributeSet)
```

Creates a synchronized view of the given print request attribute set.

**Parameters:** attributeSet

- underlying print request attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
PrintJobAttributeSet
synchronizedView​(
PrintJobAttributeSet
attributeSet)
```

Creates a synchronized view of the given print job attribute set.

**Parameters:** attributeSet

- underlying print job attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
PrintServiceAttributeSet
synchronizedView​(
PrintServiceAttributeSet
attributeSet)
```

Creates a synchronized view of the given print service attribute set.

**Parameters:** attributeSet

- underlying print service attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- verifyAttributeCategory

```java
public static
Class
<?> verifyAttributeCategory​(
Object
object,

Class
<?> interfaceName)
```

Verify that the given object is a

Class

that implements the
given interface, which is assumed to be interface

Attribute

or a subinterface thereof.

**Parameters:** object

-

Object

to test
**Parameters:** interfaceName

- interface the object must implement
**Returns:** if

object

is a

Class

that implements

interfaceName

,

object

is returned downcast to
type

Class

; otherwise an exception is thrown
**Throws:** NullPointerException

- if

object

is

null
**Throws:** ClassCastException

- if

object

is not a

Class

that implements

interfaceName

- verifyAttributeValue

```java
public static
Attribute
verifyAttributeValue​(
Object
object,

Class
<?> interfaceName)
```

Verify that the given object is an instance of the given interface, which
is assumed to be interface

Attribute

or a subinterface
thereof.

**Parameters:** object

-

Object

to test
**Parameters:** interfaceName

- interface of which the object must be an instance
**Returns:** if

object

is an instance of

interfaceName

,

object

is returned downcast to type

Attribute

; otherwise an exception is thrown
**Throws:** NullPointerException

- if

object

is

null
**Throws:** ClassCastException

- if

object

is not an instance of

interfaceName

- verifyCategoryForValue

```java
public static void verifyCategoryForValue​(
Class
<?> category,

Attribute
attribute)
```

Verify that the given attribute category object is equal to the category
of the given attribute value object. If so, this method returns doing
nothing. If not, this method throws an exception.

**Parameters:** category

- attribute category to test
**Parameters:** attribute

- attribute value to test
**Throws:** NullPointerException

- if the

category

or

attribute

are

null
**Throws:** IllegalArgumentException

- if the

category

is not equal to
the category of the

attribute

Method Detail

- unmodifiableView

```java
public static
AttributeSet
unmodifiableView​(
AttributeSet
attributeSet)
```

Creates an unmodifiable view of the given attribute set.

**Parameters:** attributeSet

- underlying attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- unmodifiableView

```java
public static
DocAttributeSet
unmodifiableView​(
DocAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given doc attribute set.

**Parameters:** attributeSet

- underlying doc attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- unmodifiableView

```java
public static
PrintRequestAttributeSet
unmodifiableView​(
PrintRequestAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given print request attribute set.

**Parameters:** attributeSet

- underlying print request attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- unmodifiableView

```java
public static
PrintJobAttributeSet
unmodifiableView​(
PrintJobAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given print job attribute set.

**Parameters:** attributeSet

- underlying print job attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- unmodifiableView

```java
public static
PrintServiceAttributeSet
unmodifiableView​(
PrintServiceAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given print service attribute set.

**Parameters:** attributeSet

- underlying print service attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
AttributeSet
synchronizedView​(
AttributeSet
attributeSet)
```

Creates a synchronized view of the given attribute set.

**Parameters:** attributeSet

- underlying attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
DocAttributeSet
synchronizedView​(
DocAttributeSet
attributeSet)
```

Creates a synchronized view of the given doc attribute set.

**Parameters:** attributeSet

- underlying doc attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
PrintRequestAttributeSet
synchronizedView​(
PrintRequestAttributeSet
attributeSet)
```

Creates a synchronized view of the given print request attribute set.

**Parameters:** attributeSet

- underlying print request attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
PrintJobAttributeSet
synchronizedView​(
PrintJobAttributeSet
attributeSet)
```

Creates a synchronized view of the given print job attribute set.

**Parameters:** attributeSet

- underlying print job attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- synchronizedView

```java
public static
PrintServiceAttributeSet
synchronizedView​(
PrintServiceAttributeSet
attributeSet)
```

Creates a synchronized view of the given print service attribute set.

**Parameters:** attributeSet

- underlying print service attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

- verifyAttributeCategory

```java
public static
Class
<?> verifyAttributeCategory​(
Object
object,

Class
<?> interfaceName)
```

Verify that the given object is a

Class

that implements the
given interface, which is assumed to be interface

Attribute

or a subinterface thereof.

**Parameters:** object

-

Object

to test
**Parameters:** interfaceName

- interface the object must implement
**Returns:** if

object

is a

Class

that implements

interfaceName

,

object

is returned downcast to
type

Class

; otherwise an exception is thrown
**Throws:** NullPointerException

- if

object

is

null
**Throws:** ClassCastException

- if

object

is not a

Class

that implements

interfaceName

- verifyAttributeValue

```java
public static
Attribute
verifyAttributeValue​(
Object
object,

Class
<?> interfaceName)
```

Verify that the given object is an instance of the given interface, which
is assumed to be interface

Attribute

or a subinterface
thereof.

**Parameters:** object

-

Object

to test
**Parameters:** interfaceName

- interface of which the object must be an instance
**Returns:** if

object

is an instance of

interfaceName

,

object

is returned downcast to type

Attribute

; otherwise an exception is thrown
**Throws:** NullPointerException

- if

object

is

null
**Throws:** ClassCastException

- if

object

is not an instance of

interfaceName

- verifyCategoryForValue

```java
public static void verifyCategoryForValue​(
Class
<?> category,

Attribute
attribute)
```

Verify that the given attribute category object is equal to the category
of the given attribute value object. If so, this method returns doing
nothing. If not, this method throws an exception.

**Parameters:** category

- attribute category to test
**Parameters:** attribute

- attribute value to test
**Throws:** NullPointerException

- if the

category

or

attribute

are

null
**Throws:** IllegalArgumentException

- if the

category

is not equal to
the category of the

attribute

---

#### Method Detail

unmodifiableView

```java
public static
AttributeSet
unmodifiableView​(
AttributeSet
attributeSet)
```

Creates an unmodifiable view of the given attribute set.

**Parameters:** attributeSet

- underlying attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### unmodifiableView

public static

AttributeSet

unmodifiableView​(

AttributeSet

attributeSet)

Creates an unmodifiable view of the given attribute set.

unmodifiableView

```java
public static
DocAttributeSet
unmodifiableView​(
DocAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given doc attribute set.

**Parameters:** attributeSet

- underlying doc attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### unmodifiableView

public static

DocAttributeSet

unmodifiableView​(

DocAttributeSet

attributeSet)

Creates an unmodifiable view of the given doc attribute set.

unmodifiableView

```java
public static
PrintRequestAttributeSet
unmodifiableView​(
PrintRequestAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given print request attribute set.

**Parameters:** attributeSet

- underlying print request attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### unmodifiableView

public static

PrintRequestAttributeSet

unmodifiableView​(

PrintRequestAttributeSet

attributeSet)

Creates an unmodifiable view of the given print request attribute set.

unmodifiableView

```java
public static
PrintJobAttributeSet
unmodifiableView​(
PrintJobAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given print job attribute set.

**Parameters:** attributeSet

- underlying print job attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### unmodifiableView

public static

PrintJobAttributeSet

unmodifiableView​(

PrintJobAttributeSet

attributeSet)

Creates an unmodifiable view of the given print job attribute set.

unmodifiableView

```java
public static
PrintServiceAttributeSet
unmodifiableView​(
PrintServiceAttributeSet
attributeSet)
```

Creates an unmodifiable view of the given print service attribute set.

**Parameters:** attributeSet

- underlying print service attribute set
**Returns:** unmodifiable view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### unmodifiableView

public static

PrintServiceAttributeSet

unmodifiableView​(

PrintServiceAttributeSet

attributeSet)

Creates an unmodifiable view of the given print service attribute set.

synchronizedView

```java
public static
AttributeSet
synchronizedView​(
AttributeSet
attributeSet)
```

Creates a synchronized view of the given attribute set.

**Parameters:** attributeSet

- underlying attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### synchronizedView

public static

AttributeSet

synchronizedView​(

AttributeSet

attributeSet)

Creates a synchronized view of the given attribute set.

synchronizedView

```java
public static
DocAttributeSet
synchronizedView​(
DocAttributeSet
attributeSet)
```

Creates a synchronized view of the given doc attribute set.

**Parameters:** attributeSet

- underlying doc attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### synchronizedView

public static

DocAttributeSet

synchronizedView​(

DocAttributeSet

attributeSet)

Creates a synchronized view of the given doc attribute set.

synchronizedView

```java
public static
PrintRequestAttributeSet
synchronizedView​(
PrintRequestAttributeSet
attributeSet)
```

Creates a synchronized view of the given print request attribute set.

**Parameters:** attributeSet

- underlying print request attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### synchronizedView

public static

PrintRequestAttributeSet

synchronizedView​(

PrintRequestAttributeSet

attributeSet)

Creates a synchronized view of the given print request attribute set.

synchronizedView

```java
public static
PrintJobAttributeSet
synchronizedView​(
PrintJobAttributeSet
attributeSet)
```

Creates a synchronized view of the given print job attribute set.

**Parameters:** attributeSet

- underlying print job attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### synchronizedView

public static

PrintJobAttributeSet

synchronizedView​(

PrintJobAttributeSet

attributeSet)

Creates a synchronized view of the given print job attribute set.

synchronizedView

```java
public static
PrintServiceAttributeSet
synchronizedView​(
PrintServiceAttributeSet
attributeSet)
```

Creates a synchronized view of the given print service attribute set.

**Parameters:** attributeSet

- underlying print service attribute set
**Returns:** synchronized view of

attributeSet
**Throws:** NullPointerException

- if

attributeSet

is

null

---

#### synchronizedView

public static

PrintServiceAttributeSet

synchronizedView​(

PrintServiceAttributeSet

attributeSet)

Creates a synchronized view of the given print service attribute set.

verifyAttributeCategory

```java
public static
Class
<?> verifyAttributeCategory​(
Object
object,

Class
<?> interfaceName)
```

Verify that the given object is a

Class

that implements the
given interface, which is assumed to be interface

Attribute

or a subinterface thereof.

**Parameters:** object

-

Object

to test
**Parameters:** interfaceName

- interface the object must implement
**Returns:** if

object

is a

Class

that implements

interfaceName

,

object

is returned downcast to
type

Class

; otherwise an exception is thrown
**Throws:** NullPointerException

- if

object

is

null
**Throws:** ClassCastException

- if

object

is not a

Class

that implements

interfaceName

---

#### verifyAttributeCategory

public static

Class

<?> verifyAttributeCategory​(

Object

object,

Class

<?> interfaceName)

Verify that the given object is a

Class

that implements the
given interface, which is assumed to be interface

Attribute

or a subinterface thereof.

verifyAttributeValue

```java
public static
Attribute
verifyAttributeValue​(
Object
object,

Class
<?> interfaceName)
```

Verify that the given object is an instance of the given interface, which
is assumed to be interface

Attribute

or a subinterface
thereof.

**Parameters:** object

-

Object

to test
**Parameters:** interfaceName

- interface of which the object must be an instance
**Returns:** if

object

is an instance of

interfaceName

,

object

is returned downcast to type

Attribute

; otherwise an exception is thrown
**Throws:** NullPointerException

- if

object

is

null
**Throws:** ClassCastException

- if

object

is not an instance of

interfaceName

---

#### verifyAttributeValue

public static

Attribute

verifyAttributeValue​(

Object

object,

Class

<?> interfaceName)

Verify that the given object is an instance of the given interface, which
is assumed to be interface

Attribute

or a subinterface
thereof.

verifyCategoryForValue

```java
public static void verifyCategoryForValue​(
Class
<?> category,

Attribute
attribute)
```

Verify that the given attribute category object is equal to the category
of the given attribute value object. If so, this method returns doing
nothing. If not, this method throws an exception.

**Parameters:** category

- attribute category to test
**Parameters:** attribute

- attribute value to test
**Throws:** NullPointerException

- if the

category

or

attribute

are

null
**Throws:** IllegalArgumentException

- if the

category

is not equal to
the category of the

attribute

---

#### verifyCategoryForValue

public static void verifyCategoryForValue​(

Class

<?> category,

Attribute

attribute)

Verify that the given attribute category object is equal to the category
of the given attribute value object. If so, this method returns doing
nothing. If not, this method throws an exception.

---

