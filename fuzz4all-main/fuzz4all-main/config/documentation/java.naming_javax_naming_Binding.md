# Class Binding

**Source:** `java.naming\javax\naming\Binding.html`

### Class Description

```java
public class
Binding

extends
NameClassPair
```

This class represents a name-to-object binding found in a context.

A context consists of name-to-object bindings.
The Binding class represents such a binding. It consists
of a name and an object. The

Context.listBindings()

method returns an enumeration of Binding.

Use subclassing for naming systems that generate contents of
a binding dynamically.

A Binding instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a Binding concurrently should
synchronize amongst themselves and provide the necessary locking.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Binding​(
String
name,

Object
obj)

Constructs an instance of a Binding given its name and object.

getClassName()

will return
the class name of

obj

(or null if

obj

is null)
unless the class name has been explicitly set using

setClassName()

**Parameters:**
- name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

listBindings()

method)
- obj

- The possibly null object bound to name.

**See Also:**
- NameClassPair.setClassName(java.lang.String)

---

#### public Binding​(
String
name,

Object
obj,
boolean isRelative)

Constructs an instance of a Binding given its name, object, and whether
the name is relative.

getClassName()

will return the class name of

obj

(or null if

obj

is null) unless the class name has been
explicitly set using

setClassName()

**Parameters:**
- name

- The non-null string name of the object.
- obj

- The possibly null object bound to name.
- isRelative

- true if

name

is a name relative
to the target context (which is named by
the first parameter of the

listBindings()

method);
false if

name

is a URL string.

**See Also:**
- NameClassPair.isRelative()

,

NameClassPair.setRelative(boolean)

,

NameClassPair.setClassName(java.lang.String)

---

#### public Binding​(
String
name,

String
className,

Object
obj)

Constructs an instance of a Binding given its name, class name, and object.

**Parameters:**
- name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

listBindings()

method)
- className

- The possibly null class name of the object
bound to

name

. If null, the class name of

obj

is
returned by

getClassName()

. If

obj

is also
null,

getClassName()

will return null.
- obj

- The possibly null object bound to name.

**See Also:**
- NameClassPair.setClassName(java.lang.String)

---

#### public Binding​(
String
name,

String
className,

Object
obj,
boolean isRelative)

Constructs an instance of a Binding given its
name, class name, object, and whether the name is relative.

**Parameters:**
- name

- The non-null string name of the object.
- className

- The possibly null class name of the object
bound to

name

. If null, the class name of

obj

is
returned by

getClassName()

. If

obj

is also
null,

getClassName()

will return null.
- obj

- The possibly null object bound to name.
- isRelative

- true if

name

is a name relative
to the target context (which is named by
the first parameter of the

listBindings()

method);
false if

name

is a URL string.

**See Also:**
- NameClassPair.isRelative()

,

NameClassPair.setRelative(boolean)

,

NameClassPair.setClassName(java.lang.String)

---

### Method Details

#### public
String
getClassName()

Retrieves the class name of the object bound to the name of this binding.
If the class name has been set explicitly, return it.
Otherwise, if this binding contains a non-null object,
that object's class name is used. Otherwise, null is returned.

**Overrides:**
- getClassName

in class

NameClassPair

**Returns:**
- A possibly null string containing class name of object bound.

**See Also:**
- getObject()

,

getClassName()

,

NameClassPair.setClassName(java.lang.String)

---

#### public
Object
getObject()

Retrieves the object bound to the name of this binding.

**Returns:**
- The object bound; null if this binding does not contain an object.

**See Also:**
- setObject(java.lang.Object)

---

#### public void setObject​(
Object
obj)

Sets the object associated with this binding.

**Parameters:**
- obj

- The possibly null object to use.

**See Also:**
- getObject()

---

#### public
String
toString()

Generates the string representation of this binding.
The string representation consists of the string representation
of the name/class pair and the string representation of
this binding's object, separated by ':'.
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:**
- toString

in class

NameClassPair

**Returns:**
- The non-null string representation of this binding.

---

### Additional Sections

#### Class Binding

java.lang.Object

- javax.naming.NameClassPair
- - javax.naming.Binding

javax.naming.NameClassPair

- javax.naming.Binding

javax.naming.Binding

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** SearchResult

```java
public class
Binding

extends
NameClassPair
```

This class represents a name-to-object binding found in a context.

A context consists of name-to-object bindings.
The Binding class represents such a binding. It consists
of a name and an object. The

Context.listBindings()

method returns an enumeration of Binding.

Use subclassing for naming systems that generate contents of
a binding dynamically.

A Binding instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a Binding concurrently should
synchronize amongst themselves and provide the necessary locking.

**Since:** 1.3
**See Also:** Serialized Form

public class

Binding

extends

NameClassPair

This class represents a name-to-object binding found in a context.

A context consists of name-to-object bindings.
The Binding class represents such a binding. It consists
of a name and an object. The

Context.listBindings()

method returns an enumeration of Binding.

Use subclassing for naming systems that generate contents of
a binding dynamically.

A Binding instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a Binding concurrently should
synchronize amongst themselves and provide the necessary locking.

A context consists of name-to-object bindings.
The Binding class represents such a binding. It consists
of a name and an object. The

Context.listBindings()

method returns an enumeration of Binding.

Use subclassing for naming systems that generate contents of
a binding dynamically.

A Binding instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a Binding concurrently should
synchronize amongst themselves and provide the necessary locking.

Use subclassing for naming systems that generate contents of
a binding dynamically.

A Binding instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a Binding concurrently should
synchronize amongst themselves and provide the necessary locking.

A Binding instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a Binding concurrently should
synchronize amongst themselves and provide the necessary locking.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Binding

​(

String

name,

Object

obj)

Constructs an instance of a Binding given its name and object.

Binding

​(

String

name,

Object

obj,
boolean isRelative)

Constructs an instance of a Binding given its name, object, and whether
the name is relative.

Binding

​(

String

name,

String

className,

Object

obj)

Constructs an instance of a Binding given its name, class name, and object.

Binding

​(

String

name,

String

className,

Object

obj,
boolean isRelative)

Constructs an instance of a Binding given its
name, class name, object, and whether the name is relative.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getClassName

()

Retrieves the class name of the object bound to the name of this binding.

Object

getObject

()

Retrieves the object bound to the name of this binding.

void

setObject

​(

Object

obj)

Sets the object associated with this binding.

String

toString

()

Generates the string representation of this binding.

- Methods declared in class javax.naming.

NameClassPair

getName

,

getNameInNamespace

,

isRelative

,

setClassName

,

setName

,

setNameInNamespace

,

setRelative

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

Binding

​(

String

name,

Object

obj)

Constructs an instance of a Binding given its name and object.

Binding

​(

String

name,

Object

obj,
boolean isRelative)

Constructs an instance of a Binding given its name, object, and whether
the name is relative.

Binding

​(

String

name,

String

className,

Object

obj)

Constructs an instance of a Binding given its name, class name, and object.

Binding

​(

String

name,

String

className,

Object

obj,
boolean isRelative)

Constructs an instance of a Binding given its
name, class name, object, and whether the name is relative.

---

#### Constructor Summary

Constructs an instance of a Binding given its name and object.

Constructs an instance of a Binding given its name, object, and whether
the name is relative.

Constructs an instance of a Binding given its name, class name, and object.

Constructs an instance of a Binding given its
name, class name, object, and whether the name is relative.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getClassName

()

Retrieves the class name of the object bound to the name of this binding.

Object

getObject

()

Retrieves the object bound to the name of this binding.

void

setObject

​(

Object

obj)

Sets the object associated with this binding.

String

toString

()

Generates the string representation of this binding.

- Methods declared in class javax.naming.

NameClassPair

getName

,

getNameInNamespace

,

isRelative

,

setClassName

,

setName

,

setNameInNamespace

,

setRelative

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

wait

,

wait

,

wait

---

#### Method Summary

Retrieves the class name of the object bound to the name of this binding.

Retrieves the object bound to the name of this binding.

Sets the object associated with this binding.

Generates the string representation of this binding.

Methods declared in class javax.naming.

NameClassPair

getName

,

getNameInNamespace

,

isRelative

,

setClassName

,

setName

,

setNameInNamespace

,

setRelative

---

#### Methods declared in class javax.naming. NameClassPair

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Binding

```java
public Binding​(
String
name,

Object
obj)
```

Constructs an instance of a Binding given its name and object.

getClassName()

will return
the class name of

obj

(or null if

obj

is null)
unless the class name has been explicitly set using

setClassName()

**Parameters:** name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

listBindings()

method)
**Parameters:** obj

- The possibly null object bound to name.
**See Also:** NameClassPair.setClassName(java.lang.String)

- Binding

```java
public Binding​(
String
name,

Object
obj,
boolean isRelative)
```

Constructs an instance of a Binding given its name, object, and whether
the name is relative.

getClassName()

will return the class name of

obj

(or null if

obj

is null) unless the class name has been
explicitly set using

setClassName()

**Parameters:** name

- The non-null string name of the object.
**Parameters:** obj

- The possibly null object bound to name.
**Parameters:** isRelative

- true if

name

is a name relative
to the target context (which is named by
the first parameter of the

listBindings()

method);
false if

name

is a URL string.
**See Also:** NameClassPair.isRelative()

,

NameClassPair.setRelative(boolean)

,

NameClassPair.setClassName(java.lang.String)

- Binding

```java
public Binding​(
String
name,

String
className,

Object
obj)
```

Constructs an instance of a Binding given its name, class name, and object.

**Parameters:** name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

listBindings()

method)
**Parameters:** className

- The possibly null class name of the object
bound to

name

. If null, the class name of

obj

is
returned by

getClassName()

. If

obj

is also
null,

getClassName()

will return null.
**Parameters:** obj

- The possibly null object bound to name.
**See Also:** NameClassPair.setClassName(java.lang.String)

- Binding

```java
public Binding​(
String
name,

String
className,

Object
obj,
boolean isRelative)
```

Constructs an instance of a Binding given its
name, class name, object, and whether the name is relative.

**Parameters:** name

- The non-null string name of the object.
**Parameters:** className

- The possibly null class name of the object
bound to

name

. If null, the class name of

obj

is
returned by

getClassName()

. If

obj

is also
null,

getClassName()

will return null.
**Parameters:** obj

- The possibly null object bound to name.
**Parameters:** isRelative

- true if

name

is a name relative
to the target context (which is named by
the first parameter of the

listBindings()

method);
false if

name

is a URL string.
**See Also:** NameClassPair.isRelative()

,

NameClassPair.setRelative(boolean)

,

NameClassPair.setClassName(java.lang.String)

============ METHOD DETAIL ==========

- Method Detail

- getClassName

```java
public
String
getClassName()
```

Retrieves the class name of the object bound to the name of this binding.
If the class name has been set explicitly, return it.
Otherwise, if this binding contains a non-null object,
that object's class name is used. Otherwise, null is returned.

**Overrides:** getClassName

in class

NameClassPair
**Returns:** A possibly null string containing class name of object bound.
**See Also:** getObject()

,

getClassName()

,

NameClassPair.setClassName(java.lang.String)

- getObject

```java
public
Object
getObject()
```

Retrieves the object bound to the name of this binding.

**Returns:** The object bound; null if this binding does not contain an object.
**See Also:** setObject(java.lang.Object)

- setObject

```java
public void setObject​(
Object
obj)
```

Sets the object associated with this binding.

**Parameters:** obj

- The possibly null object to use.
**See Also:** getObject()

- toString

```java
public
String
toString()
```

Generates the string representation of this binding.
The string representation consists of the string representation
of the name/class pair and the string representation of
this binding's object, separated by ':'.
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:** toString

in class

NameClassPair
**Returns:** The non-null string representation of this binding.

Constructor Detail

- Binding

```java
public Binding​(
String
name,

Object
obj)
```

Constructs an instance of a Binding given its name and object.

getClassName()

will return
the class name of

obj

(or null if

obj

is null)
unless the class name has been explicitly set using

setClassName()

**Parameters:** name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

listBindings()

method)
**Parameters:** obj

- The possibly null object bound to name.
**See Also:** NameClassPair.setClassName(java.lang.String)

- Binding

```java
public Binding​(
String
name,

Object
obj,
boolean isRelative)
```

Constructs an instance of a Binding given its name, object, and whether
the name is relative.

getClassName()

will return the class name of

obj

(or null if

obj

is null) unless the class name has been
explicitly set using

setClassName()

**Parameters:** name

- The non-null string name of the object.
**Parameters:** obj

- The possibly null object bound to name.
**Parameters:** isRelative

- true if

name

is a name relative
to the target context (which is named by
the first parameter of the

listBindings()

method);
false if

name

is a URL string.
**See Also:** NameClassPair.isRelative()

,

NameClassPair.setRelative(boolean)

,

NameClassPair.setClassName(java.lang.String)

- Binding

```java
public Binding​(
String
name,

String
className,

Object
obj)
```

Constructs an instance of a Binding given its name, class name, and object.

**Parameters:** name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

listBindings()

method)
**Parameters:** className

- The possibly null class name of the object
bound to

name

. If null, the class name of

obj

is
returned by

getClassName()

. If

obj

is also
null,

getClassName()

will return null.
**Parameters:** obj

- The possibly null object bound to name.
**See Also:** NameClassPair.setClassName(java.lang.String)

- Binding

```java
public Binding​(
String
name,

String
className,

Object
obj,
boolean isRelative)
```

Constructs an instance of a Binding given its
name, class name, object, and whether the name is relative.

**Parameters:** name

- The non-null string name of the object.
**Parameters:** className

- The possibly null class name of the object
bound to

name

. If null, the class name of

obj

is
returned by

getClassName()

. If

obj

is also
null,

getClassName()

will return null.
**Parameters:** obj

- The possibly null object bound to name.
**Parameters:** isRelative

- true if

name

is a name relative
to the target context (which is named by
the first parameter of the

listBindings()

method);
false if

name

is a URL string.
**See Also:** NameClassPair.isRelative()

,

NameClassPair.setRelative(boolean)

,

NameClassPair.setClassName(java.lang.String)

---

#### Constructor Detail

Binding

```java
public Binding​(
String
name,

Object
obj)
```

Constructs an instance of a Binding given its name and object.

getClassName()

will return
the class name of

obj

(or null if

obj

is null)
unless the class name has been explicitly set using

setClassName()

**Parameters:** name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

listBindings()

method)
**Parameters:** obj

- The possibly null object bound to name.
**See Also:** NameClassPair.setClassName(java.lang.String)

---

#### Binding

public Binding​(

String

name,

Object

obj)

Constructs an instance of a Binding given its name and object.

getClassName()

will return
the class name of

obj

(or null if

obj

is null)
unless the class name has been explicitly set using

setClassName()

getClassName()

will return
the class name of

obj

(or null if

obj

is null)
unless the class name has been explicitly set using

setClassName()

Binding

```java
public Binding​(
String
name,

Object
obj,
boolean isRelative)
```

Constructs an instance of a Binding given its name, object, and whether
the name is relative.

getClassName()

will return the class name of

obj

(or null if

obj

is null) unless the class name has been
explicitly set using

setClassName()

**Parameters:** name

- The non-null string name of the object.
**Parameters:** obj

- The possibly null object bound to name.
**Parameters:** isRelative

- true if

name

is a name relative
to the target context (which is named by
the first parameter of the

listBindings()

method);
false if

name

is a URL string.
**See Also:** NameClassPair.isRelative()

,

NameClassPair.setRelative(boolean)

,

NameClassPair.setClassName(java.lang.String)

---

#### Binding

public Binding​(

String

name,

Object

obj,
boolean isRelative)

Constructs an instance of a Binding given its name, object, and whether
the name is relative.

getClassName()

will return the class name of

obj

(or null if

obj

is null) unless the class name has been
explicitly set using

setClassName()

getClassName()

will return the class name of

obj

(or null if

obj

is null) unless the class name has been
explicitly set using

setClassName()

Binding

```java
public Binding​(
String
name,

String
className,

Object
obj)
```

Constructs an instance of a Binding given its name, class name, and object.

**Parameters:** name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

listBindings()

method)
**Parameters:** className

- The possibly null class name of the object
bound to

name

. If null, the class name of

obj

is
returned by

getClassName()

. If

obj

is also
null,

getClassName()

will return null.
**Parameters:** obj

- The possibly null object bound to name.
**See Also:** NameClassPair.setClassName(java.lang.String)

---

#### Binding

public Binding​(

String

name,

String

className,

Object

obj)

Constructs an instance of a Binding given its name, class name, and object.

Binding

```java
public Binding​(
String
name,

String
className,

Object
obj,
boolean isRelative)
```

Constructs an instance of a Binding given its
name, class name, object, and whether the name is relative.

**Parameters:** name

- The non-null string name of the object.
**Parameters:** className

- The possibly null class name of the object
bound to

name

. If null, the class name of

obj

is
returned by

getClassName()

. If

obj

is also
null,

getClassName()

will return null.
**Parameters:** obj

- The possibly null object bound to name.
**Parameters:** isRelative

- true if

name

is a name relative
to the target context (which is named by
the first parameter of the

listBindings()

method);
false if

name

is a URL string.
**See Also:** NameClassPair.isRelative()

,

NameClassPair.setRelative(boolean)

,

NameClassPair.setClassName(java.lang.String)

---

#### Binding

public Binding​(

String

name,

String

className,

Object

obj,
boolean isRelative)

Constructs an instance of a Binding given its
name, class name, object, and whether the name is relative.

Method Detail

- getClassName

```java
public
String
getClassName()
```

Retrieves the class name of the object bound to the name of this binding.
If the class name has been set explicitly, return it.
Otherwise, if this binding contains a non-null object,
that object's class name is used. Otherwise, null is returned.

**Overrides:** getClassName

in class

NameClassPair
**Returns:** A possibly null string containing class name of object bound.
**See Also:** getObject()

,

getClassName()

,

NameClassPair.setClassName(java.lang.String)

- getObject

```java
public
Object
getObject()
```

Retrieves the object bound to the name of this binding.

**Returns:** The object bound; null if this binding does not contain an object.
**See Also:** setObject(java.lang.Object)

- setObject

```java
public void setObject​(
Object
obj)
```

Sets the object associated with this binding.

**Parameters:** obj

- The possibly null object to use.
**See Also:** getObject()

- toString

```java
public
String
toString()
```

Generates the string representation of this binding.
The string representation consists of the string representation
of the name/class pair and the string representation of
this binding's object, separated by ':'.
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:** toString

in class

NameClassPair
**Returns:** The non-null string representation of this binding.

---

#### Method Detail

getClassName

```java
public
String
getClassName()
```

Retrieves the class name of the object bound to the name of this binding.
If the class name has been set explicitly, return it.
Otherwise, if this binding contains a non-null object,
that object's class name is used. Otherwise, null is returned.

**Overrides:** getClassName

in class

NameClassPair
**Returns:** A possibly null string containing class name of object bound.
**See Also:** getObject()

,

getClassName()

,

NameClassPair.setClassName(java.lang.String)

---

#### getClassName

public

String

getClassName()

Retrieves the class name of the object bound to the name of this binding.
If the class name has been set explicitly, return it.
Otherwise, if this binding contains a non-null object,
that object's class name is used. Otherwise, null is returned.

getObject

```java
public
Object
getObject()
```

Retrieves the object bound to the name of this binding.

**Returns:** The object bound; null if this binding does not contain an object.
**See Also:** setObject(java.lang.Object)

---

#### getObject

public

Object

getObject()

Retrieves the object bound to the name of this binding.

setObject

```java
public void setObject​(
Object
obj)
```

Sets the object associated with this binding.

**Parameters:** obj

- The possibly null object to use.
**See Also:** getObject()

---

#### setObject

public void setObject​(

Object

obj)

Sets the object associated with this binding.

toString

```java
public
String
toString()
```

Generates the string representation of this binding.
The string representation consists of the string representation
of the name/class pair and the string representation of
this binding's object, separated by ':'.
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:** toString

in class

NameClassPair
**Returns:** The non-null string representation of this binding.

---

#### toString

public

String

toString()

Generates the string representation of this binding.
The string representation consists of the string representation
of the name/class pair and the string representation of
this binding's object, separated by ':'.
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

---

