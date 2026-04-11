# Class NameClassPair

**Source:** `java.naming\javax\naming\NameClassPair.html`

### Class Description

```java
public class
NameClassPair

extends
Object

implements
Serializable
```

This class represents the object name and class name pair of a binding
found in a context.

A context consists of name-to-object bindings.
The NameClassPair class represents the name and the
class of the bound object. It consists
of a name and a string representing the
package-qualified class name.

Use subclassing for naming systems that generate contents of
a name/class pair dynamically.

A NameClassPair instance is not synchronized against concurrent
access by multiple threads. Threads that need to access a NameClassPair
concurrently should synchronize amongst themselves and provide
the necessary locking.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NameClassPair​(
String
name,

String
className)

Constructs an instance of a NameClassPair given its
name and class name.

**Parameters:**
- name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

list()

method)
- className

- The possibly null class name of the object
bound to name. It is null if the object bound is null.

**See Also:**
- getClassName()

,

setClassName(java.lang.String)

,

getName()

,

setName(java.lang.String)

---

#### public NameClassPair​(
String
name,

String
className,
boolean isRelative)

Constructs an instance of a NameClassPair given its
name, class name, and whether it is relative to the listing context.

**Parameters:**
- name

- The non-null name of the object.
- className

- The possibly null class name of the object
bound to name. It is null if the object bound is null.
- isRelative

- true if

name

is a name relative
to the target context (which is named by the first parameter
of the

list()

method); false if

name

is a URL string.

**See Also:**
- getClassName()

,

setClassName(java.lang.String)

,

getName()

,

setName(java.lang.String)

,

isRelative()

,

setRelative(boolean)

---

### Method Details

#### public
String
getClassName()

Retrieves the class name of the object bound to the name of this binding.
If a reference or some other indirect information is bound,
retrieves the class name of the eventual object that
will be returned by

Binding.getObject()

.

**Returns:**
- The possibly null class name of object bound.
It is null if the object bound is null.

**See Also:**
- Binding.getObject()

,

Binding.getClassName()

,

setClassName(java.lang.String)

---

#### public
String
getName()

Retrieves the name of this binding.
If

isRelative()

is true, this name is relative to the
target context (which is named by the first parameter of the

list()

).
If

isRelative()

is false, this name is a URL string.

**Returns:**
- The non-null name of this binding.

**See Also:**
- isRelative()

,

setName(java.lang.String)

---

#### public void setName​(
String
name)

Sets the name of this binding.

**Parameters:**
- name

- the non-null string to use as the name.

**See Also:**
- getName()

,

setRelative(boolean)

---

#### public void setClassName​(
String
name)

Sets the class name of this binding.

**Parameters:**
- name

- the possibly null string to use as the class name.
If null,

Binding.getClassName()

will return
the actual class name of the object in the binding.
The class name will be null if the object bound is null.

**See Also:**
- getClassName()

,

Binding.getClassName()

---

#### public boolean isRelative()

Determines whether the name of this binding is
relative to the target context (which is named by
the first parameter of the

list()

method).

**Returns:**
- true if the name of this binding is relative to the
target context;
false if the name of this binding is a URL string.

**See Also:**
- setRelative(boolean)

,

getName()

---

#### public void setRelative​(boolean r)

Sets whether the name of this binding is relative to the target
context (which is named by the first parameter of the

list()

method).

**Parameters:**
- r

- If true, the name of binding is relative to the target context;
if false, the name of binding is a URL string.

**See Also:**
- isRelative()

,

setName(java.lang.String)

---

#### public
String
getNameInNamespace()

Retrieves the full name of this binding.
The full name is the absolute name of this binding within
its own namespace. See

Context.getNameInNamespace()

.

In naming systems for which the notion of full name does not
apply to this binding an

UnsupportedOperationException

is thrown.
This exception is also thrown when a service provider written before
the introduction of the method is in use.

The string returned by this method is not a JNDI composite name and
should not be passed directly to context methods.

**Returns:**
- The full name of this binding.

**Throws:**
- UnsupportedOperationException

- if the notion of full name
does not apply to this binding in the naming system.

**See Also:**
- setNameInNamespace(java.lang.String)

,

getName()

**Since:**
- 1.5

---

#### public void setNameInNamespace​(
String
fullName)

Sets the full name of this binding.
This method must be called to set the full name whenever a

NameClassPair

is created and a full name is
applicable to this binding.

Setting the full name to null, or not setting it at all, will
cause

getNameInNamespace()

to throw an exception.

**Parameters:**
- fullName

- The full name to use.

**See Also:**
- getNameInNamespace()

,

setName(java.lang.String)

**Since:**
- 1.5

---

#### public
String
toString()

Generates the string representation of this name/class pair.
The string representation consists of the name and class name separated
by a colon (':').
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:**
- toString

in class

Object

**Returns:**
- The string representation of this name/class pair.

---

### Additional Sections

#### Class NameClassPair

java.lang.Object

- javax.naming.NameClassPair

javax.naming.NameClassPair

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** Binding

```java
public class
NameClassPair

extends
Object

implements
Serializable
```

This class represents the object name and class name pair of a binding
found in a context.

A context consists of name-to-object bindings.
The NameClassPair class represents the name and the
class of the bound object. It consists
of a name and a string representing the
package-qualified class name.

Use subclassing for naming systems that generate contents of
a name/class pair dynamically.

A NameClassPair instance is not synchronized against concurrent
access by multiple threads. Threads that need to access a NameClassPair
concurrently should synchronize amongst themselves and provide
the necessary locking.

**Since:** 1.3
**See Also:** Context.list(javax.naming.Name)

,

Serialized Form

public class

NameClassPair

extends

Object

implements

Serializable

This class represents the object name and class name pair of a binding
found in a context.

A context consists of name-to-object bindings.
The NameClassPair class represents the name and the
class of the bound object. It consists
of a name and a string representing the
package-qualified class name.

Use subclassing for naming systems that generate contents of
a name/class pair dynamically.

A NameClassPair instance is not synchronized against concurrent
access by multiple threads. Threads that need to access a NameClassPair
concurrently should synchronize amongst themselves and provide
the necessary locking.

A context consists of name-to-object bindings.
The NameClassPair class represents the name and the
class of the bound object. It consists
of a name and a string representing the
package-qualified class name.

Use subclassing for naming systems that generate contents of
a name/class pair dynamically.

A NameClassPair instance is not synchronized against concurrent
access by multiple threads. Threads that need to access a NameClassPair
concurrently should synchronize amongst themselves and provide
the necessary locking.

Use subclassing for naming systems that generate contents of
a name/class pair dynamically.

A NameClassPair instance is not synchronized against concurrent
access by multiple threads. Threads that need to access a NameClassPair
concurrently should synchronize amongst themselves and provide
the necessary locking.

A NameClassPair instance is not synchronized against concurrent
access by multiple threads. Threads that need to access a NameClassPair
concurrently should synchronize amongst themselves and provide
the necessary locking.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NameClassPair

​(

String

name,

String

className)

Constructs an instance of a NameClassPair given its
name and class name.

NameClassPair

​(

String

name,

String

className,
boolean isRelative)

Constructs an instance of a NameClassPair given its
name, class name, and whether it is relative to the listing context.

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

String

getName

()

Retrieves the name of this binding.

String

getNameInNamespace

()

Retrieves the full name of this binding.

boolean

isRelative

()

Determines whether the name of this binding is
relative to the target context (which is named by
the first parameter of the

list()

method).

void

setClassName

​(

String

name)

Sets the class name of this binding.

void

setName

​(

String

name)

Sets the name of this binding.

void

setNameInNamespace

​(

String

fullName)

Sets the full name of this binding.

void

setRelative

​(boolean r)

Sets whether the name of this binding is relative to the target
context (which is named by the first parameter of the

list()

method).

String

toString

()

Generates the string representation of this name/class pair.

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

NameClassPair

​(

String

name,

String

className)

Constructs an instance of a NameClassPair given its
name and class name.

NameClassPair

​(

String

name,

String

className,
boolean isRelative)

Constructs an instance of a NameClassPair given its
name, class name, and whether it is relative to the listing context.

---

#### Constructor Summary

Constructs an instance of a NameClassPair given its
name and class name.

Constructs an instance of a NameClassPair given its
name, class name, and whether it is relative to the listing context.

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

String

getName

()

Retrieves the name of this binding.

String

getNameInNamespace

()

Retrieves the full name of this binding.

boolean

isRelative

()

Determines whether the name of this binding is
relative to the target context (which is named by
the first parameter of the

list()

method).

void

setClassName

​(

String

name)

Sets the class name of this binding.

void

setName

​(

String

name)

Sets the name of this binding.

void

setNameInNamespace

​(

String

fullName)

Sets the full name of this binding.

void

setRelative

​(boolean r)

Sets whether the name of this binding is relative to the target
context (which is named by the first parameter of the

list()

method).

String

toString

()

Generates the string representation of this name/class pair.

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

Retrieves the name of this binding.

Retrieves the full name of this binding.

Determines whether the name of this binding is
relative to the target context (which is named by
the first parameter of the

list()

method).

Sets the class name of this binding.

Sets the name of this binding.

Sets the full name of this binding.

Sets whether the name of this binding is relative to the target
context (which is named by the first parameter of the

list()

method).

Generates the string representation of this name/class pair.

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

- NameClassPair

```java
public NameClassPair​(
String
name,

String
className)
```

Constructs an instance of a NameClassPair given its
name and class name.

**Parameters:** name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

list()

method)
**Parameters:** className

- The possibly null class name of the object
bound to name. It is null if the object bound is null.
**See Also:** getClassName()

,

setClassName(java.lang.String)

,

getName()

,

setName(java.lang.String)

- NameClassPair

```java
public NameClassPair​(
String
name,

String
className,
boolean isRelative)
```

Constructs an instance of a NameClassPair given its
name, class name, and whether it is relative to the listing context.

**Parameters:** name

- The non-null name of the object.
**Parameters:** className

- The possibly null class name of the object
bound to name. It is null if the object bound is null.
**Parameters:** isRelative

- true if

name

is a name relative
to the target context (which is named by the first parameter
of the

list()

method); false if

name

is a URL string.
**See Also:** getClassName()

,

setClassName(java.lang.String)

,

getName()

,

setName(java.lang.String)

,

isRelative()

,

setRelative(boolean)

============ METHOD DETAIL ==========

- Method Detail

- getClassName

```java
public
String
getClassName()
```

Retrieves the class name of the object bound to the name of this binding.
If a reference or some other indirect information is bound,
retrieves the class name of the eventual object that
will be returned by

Binding.getObject()

.

**Returns:** The possibly null class name of object bound.
It is null if the object bound is null.
**See Also:** Binding.getObject()

,

Binding.getClassName()

,

setClassName(java.lang.String)

- getName

```java
public
String
getName()
```

Retrieves the name of this binding.
If

isRelative()

is true, this name is relative to the
target context (which is named by the first parameter of the

list()

).
If

isRelative()

is false, this name is a URL string.

**Returns:** The non-null name of this binding.
**See Also:** isRelative()

,

setName(java.lang.String)

- setName

```java
public void setName​(
String
name)
```

Sets the name of this binding.

**Parameters:** name

- the non-null string to use as the name.
**See Also:** getName()

,

setRelative(boolean)

- setClassName

```java
public void setClassName​(
String
name)
```

Sets the class name of this binding.

**Parameters:** name

- the possibly null string to use as the class name.
If null,

Binding.getClassName()

will return
the actual class name of the object in the binding.
The class name will be null if the object bound is null.
**See Also:** getClassName()

,

Binding.getClassName()

- isRelative

```java
public boolean isRelative()
```

Determines whether the name of this binding is
relative to the target context (which is named by
the first parameter of the

list()

method).

**Returns:** true if the name of this binding is relative to the
target context;
false if the name of this binding is a URL string.
**See Also:** setRelative(boolean)

,

getName()

- setRelative

```java
public void setRelative​(boolean r)
```

Sets whether the name of this binding is relative to the target
context (which is named by the first parameter of the

list()

method).

**Parameters:** r

- If true, the name of binding is relative to the target context;
if false, the name of binding is a URL string.
**See Also:** isRelative()

,

setName(java.lang.String)

- getNameInNamespace

```java
public
String
getNameInNamespace()
```

Retrieves the full name of this binding.
The full name is the absolute name of this binding within
its own namespace. See

Context.getNameInNamespace()

.

In naming systems for which the notion of full name does not
apply to this binding an

UnsupportedOperationException

is thrown.
This exception is also thrown when a service provider written before
the introduction of the method is in use.

The string returned by this method is not a JNDI composite name and
should not be passed directly to context methods.

**Returns:** The full name of this binding.
**Throws:** UnsupportedOperationException

- if the notion of full name
does not apply to this binding in the naming system.
**Since:** 1.5
**See Also:** setNameInNamespace(java.lang.String)

,

getName()

- setNameInNamespace

```java
public void setNameInNamespace​(
String
fullName)
```

Sets the full name of this binding.
This method must be called to set the full name whenever a

NameClassPair

is created and a full name is
applicable to this binding.

Setting the full name to null, or not setting it at all, will
cause

getNameInNamespace()

to throw an exception.

**Parameters:** fullName

- The full name to use.
**Since:** 1.5
**See Also:** getNameInNamespace()

,

setName(java.lang.String)

- toString

```java
public
String
toString()
```

Generates the string representation of this name/class pair.
The string representation consists of the name and class name separated
by a colon (':').
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** The string representation of this name/class pair.

Constructor Detail

- NameClassPair

```java
public NameClassPair​(
String
name,

String
className)
```

Constructs an instance of a NameClassPair given its
name and class name.

**Parameters:** name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

list()

method)
**Parameters:** className

- The possibly null class name of the object
bound to name. It is null if the object bound is null.
**See Also:** getClassName()

,

setClassName(java.lang.String)

,

getName()

,

setName(java.lang.String)

- NameClassPair

```java
public NameClassPair​(
String
name,

String
className,
boolean isRelative)
```

Constructs an instance of a NameClassPair given its
name, class name, and whether it is relative to the listing context.

**Parameters:** name

- The non-null name of the object.
**Parameters:** className

- The possibly null class name of the object
bound to name. It is null if the object bound is null.
**Parameters:** isRelative

- true if

name

is a name relative
to the target context (which is named by the first parameter
of the

list()

method); false if

name

is a URL string.
**See Also:** getClassName()

,

setClassName(java.lang.String)

,

getName()

,

setName(java.lang.String)

,

isRelative()

,

setRelative(boolean)

---

#### Constructor Detail

NameClassPair

```java
public NameClassPair​(
String
name,

String
className)
```

Constructs an instance of a NameClassPair given its
name and class name.

**Parameters:** name

- The non-null name of the object. It is relative
to the

target context

(which is
named by the first parameter of the

list()

method)
**Parameters:** className

- The possibly null class name of the object
bound to name. It is null if the object bound is null.
**See Also:** getClassName()

,

setClassName(java.lang.String)

,

getName()

,

setName(java.lang.String)

---

#### NameClassPair

public NameClassPair​(

String

name,

String

className)

Constructs an instance of a NameClassPair given its
name and class name.

NameClassPair

```java
public NameClassPair​(
String
name,

String
className,
boolean isRelative)
```

Constructs an instance of a NameClassPair given its
name, class name, and whether it is relative to the listing context.

**Parameters:** name

- The non-null name of the object.
**Parameters:** className

- The possibly null class name of the object
bound to name. It is null if the object bound is null.
**Parameters:** isRelative

- true if

name

is a name relative
to the target context (which is named by the first parameter
of the

list()

method); false if

name

is a URL string.
**See Also:** getClassName()

,

setClassName(java.lang.String)

,

getName()

,

setName(java.lang.String)

,

isRelative()

,

setRelative(boolean)

---

#### NameClassPair

public NameClassPair​(

String

name,

String

className,
boolean isRelative)

Constructs an instance of a NameClassPair given its
name, class name, and whether it is relative to the listing context.

Method Detail

- getClassName

```java
public
String
getClassName()
```

Retrieves the class name of the object bound to the name of this binding.
If a reference or some other indirect information is bound,
retrieves the class name of the eventual object that
will be returned by

Binding.getObject()

.

**Returns:** The possibly null class name of object bound.
It is null if the object bound is null.
**See Also:** Binding.getObject()

,

Binding.getClassName()

,

setClassName(java.lang.String)

- getName

```java
public
String
getName()
```

Retrieves the name of this binding.
If

isRelative()

is true, this name is relative to the
target context (which is named by the first parameter of the

list()

).
If

isRelative()

is false, this name is a URL string.

**Returns:** The non-null name of this binding.
**See Also:** isRelative()

,

setName(java.lang.String)

- setName

```java
public void setName​(
String
name)
```

Sets the name of this binding.

**Parameters:** name

- the non-null string to use as the name.
**See Also:** getName()

,

setRelative(boolean)

- setClassName

```java
public void setClassName​(
String
name)
```

Sets the class name of this binding.

**Parameters:** name

- the possibly null string to use as the class name.
If null,

Binding.getClassName()

will return
the actual class name of the object in the binding.
The class name will be null if the object bound is null.
**See Also:** getClassName()

,

Binding.getClassName()

- isRelative

```java
public boolean isRelative()
```

Determines whether the name of this binding is
relative to the target context (which is named by
the first parameter of the

list()

method).

**Returns:** true if the name of this binding is relative to the
target context;
false if the name of this binding is a URL string.
**See Also:** setRelative(boolean)

,

getName()

- setRelative

```java
public void setRelative​(boolean r)
```

Sets whether the name of this binding is relative to the target
context (which is named by the first parameter of the

list()

method).

**Parameters:** r

- If true, the name of binding is relative to the target context;
if false, the name of binding is a URL string.
**See Also:** isRelative()

,

setName(java.lang.String)

- getNameInNamespace

```java
public
String
getNameInNamespace()
```

Retrieves the full name of this binding.
The full name is the absolute name of this binding within
its own namespace. See

Context.getNameInNamespace()

.

In naming systems for which the notion of full name does not
apply to this binding an

UnsupportedOperationException

is thrown.
This exception is also thrown when a service provider written before
the introduction of the method is in use.

The string returned by this method is not a JNDI composite name and
should not be passed directly to context methods.

**Returns:** The full name of this binding.
**Throws:** UnsupportedOperationException

- if the notion of full name
does not apply to this binding in the naming system.
**Since:** 1.5
**See Also:** setNameInNamespace(java.lang.String)

,

getName()

- setNameInNamespace

```java
public void setNameInNamespace​(
String
fullName)
```

Sets the full name of this binding.
This method must be called to set the full name whenever a

NameClassPair

is created and a full name is
applicable to this binding.

Setting the full name to null, or not setting it at all, will
cause

getNameInNamespace()

to throw an exception.

**Parameters:** fullName

- The full name to use.
**Since:** 1.5
**See Also:** getNameInNamespace()

,

setName(java.lang.String)

- toString

```java
public
String
toString()
```

Generates the string representation of this name/class pair.
The string representation consists of the name and class name separated
by a colon (':').
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** The string representation of this name/class pair.

---

#### Method Detail

getClassName

```java
public
String
getClassName()
```

Retrieves the class name of the object bound to the name of this binding.
If a reference or some other indirect information is bound,
retrieves the class name of the eventual object that
will be returned by

Binding.getObject()

.

**Returns:** The possibly null class name of object bound.
It is null if the object bound is null.
**See Also:** Binding.getObject()

,

Binding.getClassName()

,

setClassName(java.lang.String)

---

#### getClassName

public

String

getClassName()

Retrieves the class name of the object bound to the name of this binding.
If a reference or some other indirect information is bound,
retrieves the class name of the eventual object that
will be returned by

Binding.getObject()

.

getName

```java
public
String
getName()
```

Retrieves the name of this binding.
If

isRelative()

is true, this name is relative to the
target context (which is named by the first parameter of the

list()

).
If

isRelative()

is false, this name is a URL string.

**Returns:** The non-null name of this binding.
**See Also:** isRelative()

,

setName(java.lang.String)

---

#### getName

public

String

getName()

Retrieves the name of this binding.
If

isRelative()

is true, this name is relative to the
target context (which is named by the first parameter of the

list()

).
If

isRelative()

is false, this name is a URL string.

setName

```java
public void setName​(
String
name)
```

Sets the name of this binding.

**Parameters:** name

- the non-null string to use as the name.
**See Also:** getName()

,

setRelative(boolean)

---

#### setName

public void setName​(

String

name)

Sets the name of this binding.

setClassName

```java
public void setClassName​(
String
name)
```

Sets the class name of this binding.

**Parameters:** name

- the possibly null string to use as the class name.
If null,

Binding.getClassName()

will return
the actual class name of the object in the binding.
The class name will be null if the object bound is null.
**See Also:** getClassName()

,

Binding.getClassName()

---

#### setClassName

public void setClassName​(

String

name)

Sets the class name of this binding.

isRelative

```java
public boolean isRelative()
```

Determines whether the name of this binding is
relative to the target context (which is named by
the first parameter of the

list()

method).

**Returns:** true if the name of this binding is relative to the
target context;
false if the name of this binding is a URL string.
**See Also:** setRelative(boolean)

,

getName()

---

#### isRelative

public boolean isRelative()

Determines whether the name of this binding is
relative to the target context (which is named by
the first parameter of the

list()

method).

setRelative

```java
public void setRelative​(boolean r)
```

Sets whether the name of this binding is relative to the target
context (which is named by the first parameter of the

list()

method).

**Parameters:** r

- If true, the name of binding is relative to the target context;
if false, the name of binding is a URL string.
**See Also:** isRelative()

,

setName(java.lang.String)

---

#### setRelative

public void setRelative​(boolean r)

Sets whether the name of this binding is relative to the target
context (which is named by the first parameter of the

list()

method).

getNameInNamespace

```java
public
String
getNameInNamespace()
```

Retrieves the full name of this binding.
The full name is the absolute name of this binding within
its own namespace. See

Context.getNameInNamespace()

.

In naming systems for which the notion of full name does not
apply to this binding an

UnsupportedOperationException

is thrown.
This exception is also thrown when a service provider written before
the introduction of the method is in use.

The string returned by this method is not a JNDI composite name and
should not be passed directly to context methods.

**Returns:** The full name of this binding.
**Throws:** UnsupportedOperationException

- if the notion of full name
does not apply to this binding in the naming system.
**Since:** 1.5
**See Also:** setNameInNamespace(java.lang.String)

,

getName()

---

#### getNameInNamespace

public

String

getNameInNamespace()

Retrieves the full name of this binding.
The full name is the absolute name of this binding within
its own namespace. See

Context.getNameInNamespace()

.

In naming systems for which the notion of full name does not
apply to this binding an

UnsupportedOperationException

is thrown.
This exception is also thrown when a service provider written before
the introduction of the method is in use.

The string returned by this method is not a JNDI composite name and
should not be passed directly to context methods.

In naming systems for which the notion of full name does not
apply to this binding an

UnsupportedOperationException

is thrown.
This exception is also thrown when a service provider written before
the introduction of the method is in use.

The string returned by this method is not a JNDI composite name and
should not be passed directly to context methods.

The string returned by this method is not a JNDI composite name and
should not be passed directly to context methods.

setNameInNamespace

```java
public void setNameInNamespace​(
String
fullName)
```

Sets the full name of this binding.
This method must be called to set the full name whenever a

NameClassPair

is created and a full name is
applicable to this binding.

Setting the full name to null, or not setting it at all, will
cause

getNameInNamespace()

to throw an exception.

**Parameters:** fullName

- The full name to use.
**Since:** 1.5
**See Also:** getNameInNamespace()

,

setName(java.lang.String)

---

#### setNameInNamespace

public void setNameInNamespace​(

String

fullName)

Sets the full name of this binding.
This method must be called to set the full name whenever a

NameClassPair

is created and a full name is
applicable to this binding.

Setting the full name to null, or not setting it at all, will
cause

getNameInNamespace()

to throw an exception.

Setting the full name to null, or not setting it at all, will
cause

getNameInNamespace()

to throw an exception.

toString

```java
public
String
toString()
```

Generates the string representation of this name/class pair.
The string representation consists of the name and class name separated
by a colon (':').
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** The string representation of this name/class pair.

---

#### toString

public

String

toString()

Generates the string representation of this name/class pair.
The string representation consists of the name and class name separated
by a colon (':').
The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

---

