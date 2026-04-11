# Class ModificationItem

**Source:** `java.naming\javax\naming\directory\ModificationItem.html`

### Class Description

```java
public class
ModificationItem

extends
Object

implements
Serializable
```

This class represents a modification item.
It consists of a modification code and an attribute on which to operate.

A ModificationItem instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single ModificationItem instance should lock the object.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ModificationItem​(int mod_op,

Attribute
attr)

Creates a new instance of ModificationItem.

**Parameters:**
- mod_op

- Modification to apply. It must be one of:
DirContext.ADD_ATTRIBUTE
DirContext.REPLACE_ATTRIBUTE
DirContext.REMOVE_ATTRIBUTE
- attr

- The non-null attribute to use for modification.

**Throws:**
- IllegalArgumentException

- If attr is null, or if mod_op is
not one of the ones specified above.

---

### Method Details

#### public int getModificationOp()

Retrieves the modification code of this modification item.

**Returns:**
- The modification code. It is one of:
DirContext.ADD_ATTRIBUTE
DirContext.REPLACE_ATTRIBUTE
DirContext.REMOVE_ATTRIBUTE

---

#### public
Attribute
getAttribute()

Retrieves the attribute associated with this modification item.

**Returns:**
- The non-null attribute to use for the modification.

---

#### public
String
toString()

Generates the string representation of this modification item,
which consists of the modification operation and its related attribute.
The string representation is meant for debugging and not to be
interpreted programmatically.

**Overrides:**
- toString

in class

Object

**Returns:**
- The non-null string representation of this modification item.

---

### Additional Sections

#### Class ModificationItem

java.lang.Object

- javax.naming.directory.ModificationItem

javax.naming.directory.ModificationItem

**All Implemented Interfaces:** Serializable

```java
public class
ModificationItem

extends
Object

implements
Serializable
```

This class represents a modification item.
It consists of a modification code and an attribute on which to operate.

A ModificationItem instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single ModificationItem instance should lock the object.

**Since:** 1.3
**See Also:** Serialized Form

public class

ModificationItem

extends

Object

implements

Serializable

This class represents a modification item.
It consists of a modification code and an attribute on which to operate.

A ModificationItem instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single ModificationItem instance should lock the object.

A ModificationItem instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single ModificationItem instance should lock the object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ModificationItem

​(int mod_op,

Attribute

attr)

Creates a new instance of ModificationItem.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Attribute

getAttribute

()

Retrieves the attribute associated with this modification item.

int

getModificationOp

()

Retrieves the modification code of this modification item.

String

toString

()

Generates the string representation of this modification item,
which consists of the modification operation and its related attribute.

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

ModificationItem

​(int mod_op,

Attribute

attr)

Creates a new instance of ModificationItem.

---

#### Constructor Summary

Creates a new instance of ModificationItem.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Attribute

getAttribute

()

Retrieves the attribute associated with this modification item.

int

getModificationOp

()

Retrieves the modification code of this modification item.

String

toString

()

Generates the string representation of this modification item,
which consists of the modification operation and its related attribute.

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

Retrieves the attribute associated with this modification item.

Retrieves the modification code of this modification item.

Generates the string representation of this modification item,
which consists of the modification operation and its related attribute.

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

- ModificationItem

```java
public ModificationItem​(int mod_op,

Attribute
attr)
```

Creates a new instance of ModificationItem.

**Parameters:** mod_op

- Modification to apply. It must be one of:
DirContext.ADD_ATTRIBUTE
DirContext.REPLACE_ATTRIBUTE
DirContext.REMOVE_ATTRIBUTE
**Parameters:** attr

- The non-null attribute to use for modification.
**Throws:** IllegalArgumentException

- If attr is null, or if mod_op is
not one of the ones specified above.

============ METHOD DETAIL ==========

- Method Detail

- getModificationOp

```java
public int getModificationOp()
```

Retrieves the modification code of this modification item.

**Returns:** The modification code. It is one of:
DirContext.ADD_ATTRIBUTE
DirContext.REPLACE_ATTRIBUTE
DirContext.REMOVE_ATTRIBUTE

- getAttribute

```java
public
Attribute
getAttribute()
```

Retrieves the attribute associated with this modification item.

**Returns:** The non-null attribute to use for the modification.

- toString

```java
public
String
toString()
```

Generates the string representation of this modification item,
which consists of the modification operation and its related attribute.
The string representation is meant for debugging and not to be
interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this modification item.

Constructor Detail

- ModificationItem

```java
public ModificationItem​(int mod_op,

Attribute
attr)
```

Creates a new instance of ModificationItem.

**Parameters:** mod_op

- Modification to apply. It must be one of:
DirContext.ADD_ATTRIBUTE
DirContext.REPLACE_ATTRIBUTE
DirContext.REMOVE_ATTRIBUTE
**Parameters:** attr

- The non-null attribute to use for modification.
**Throws:** IllegalArgumentException

- If attr is null, or if mod_op is
not one of the ones specified above.

---

#### Constructor Detail

ModificationItem

```java
public ModificationItem​(int mod_op,

Attribute
attr)
```

Creates a new instance of ModificationItem.

**Parameters:** mod_op

- Modification to apply. It must be one of:
DirContext.ADD_ATTRIBUTE
DirContext.REPLACE_ATTRIBUTE
DirContext.REMOVE_ATTRIBUTE
**Parameters:** attr

- The non-null attribute to use for modification.
**Throws:** IllegalArgumentException

- If attr is null, or if mod_op is
not one of the ones specified above.

---

#### ModificationItem

public ModificationItem​(int mod_op,

Attribute

attr)

Creates a new instance of ModificationItem.

Method Detail

- getModificationOp

```java
public int getModificationOp()
```

Retrieves the modification code of this modification item.

**Returns:** The modification code. It is one of:
DirContext.ADD_ATTRIBUTE
DirContext.REPLACE_ATTRIBUTE
DirContext.REMOVE_ATTRIBUTE

- getAttribute

```java
public
Attribute
getAttribute()
```

Retrieves the attribute associated with this modification item.

**Returns:** The non-null attribute to use for the modification.

- toString

```java
public
String
toString()
```

Generates the string representation of this modification item,
which consists of the modification operation and its related attribute.
The string representation is meant for debugging and not to be
interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this modification item.

---

#### Method Detail

getModificationOp

```java
public int getModificationOp()
```

Retrieves the modification code of this modification item.

**Returns:** The modification code. It is one of:
DirContext.ADD_ATTRIBUTE
DirContext.REPLACE_ATTRIBUTE
DirContext.REMOVE_ATTRIBUTE

---

#### getModificationOp

public int getModificationOp()

Retrieves the modification code of this modification item.

getAttribute

```java
public
Attribute
getAttribute()
```

Retrieves the attribute associated with this modification item.

**Returns:** The non-null attribute to use for the modification.

---

#### getAttribute

public

Attribute

getAttribute()

Retrieves the attribute associated with this modification item.

toString

```java
public
String
toString()
```

Generates the string representation of this modification item,
which consists of the modification operation and its related attribute.
The string representation is meant for debugging and not to be
interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this modification item.

---

#### toString

public

String

toString()

Generates the string representation of this modification item,
which consists of the modification operation and its related attribute.
The string representation is meant for debugging and not to be
interpreted programmatically.

---

