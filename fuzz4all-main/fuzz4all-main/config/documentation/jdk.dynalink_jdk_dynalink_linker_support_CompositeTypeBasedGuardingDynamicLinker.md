# Class CompositeTypeBasedGuardingDynamicLinker

**Source:** `jdk.dynalink\jdk\dynalink\linker\support\CompositeTypeBasedGuardingDynamicLinker.html`

### Class Description

```java
public class
CompositeTypeBasedGuardingDynamicLinker

extends
Object

implements
TypeBasedGuardingDynamicLinker
```

A composite type-based guarding dynamic linker. When a receiver of a not yet
seen class is encountered, all linkers are queried sequentially on their

TypeBasedGuardingDynamicLinker.canLinkType(Class)

method. The linkers
returning true are then bound to the class, and next time a receiver of same
type is encountered, the linking is delegated to those linkers only, speeding
up dispatch.

**All Implemented Interfaces:** GuardingDynamicLinker

,

TypeBasedGuardingDynamicLinker

---

### Field Details

*No entries found.*

### Constructor Details

#### public CompositeTypeBasedGuardingDynamicLinker​(
Iterable
<? extends
TypeBasedGuardingDynamicLinker
> linkers)

Creates a new composite type-based linker.

**Parameters:**
- linkers

- the component linkers

**Throws:**
- NullPointerException

- if

linkers

or any of its elements
are null.

---

### Method Details

#### public boolean canLinkType​(
Class
<?> type)

Returns true if at least one of the composite linkers returns true from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

for the type.

**Specified by:**
- canLinkType

in interface

TypeBasedGuardingDynamicLinker

**Parameters:**
- type

- the type to link

**Returns:**
- true true if at least one of the composite linkers returns true
from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

, false
otherwise.

---

#### public static
List
<
GuardingDynamicLinker
> optimize​(
Iterable
<? extends
GuardingDynamicLinker
> linkers)

Optimizes a list of type-based linkers. If a group of adjacent linkers in
the list all implement

TypeBasedGuardingDynamicLinker

, they will
be replaced with a single instance of

CompositeTypeBasedGuardingDynamicLinker

that contains them.

**Parameters:**
- linkers

- the list of linkers to optimize

**Returns:**
- the optimized list

**Throws:**
- NullPointerException

- if

linkers

or any of its elements
are null.

---

### Additional Sections

#### Class CompositeTypeBasedGuardingDynamicLinker

java.lang.Object

- jdk.dynalink.linker.support.CompositeTypeBasedGuardingDynamicLinker

jdk.dynalink.linker.support.CompositeTypeBasedGuardingDynamicLinker

**All Implemented Interfaces:** GuardingDynamicLinker

,

TypeBasedGuardingDynamicLinker

```java
public class
CompositeTypeBasedGuardingDynamicLinker

extends
Object

implements
TypeBasedGuardingDynamicLinker
```

A composite type-based guarding dynamic linker. When a receiver of a not yet
seen class is encountered, all linkers are queried sequentially on their

TypeBasedGuardingDynamicLinker.canLinkType(Class)

method. The linkers
returning true are then bound to the class, and next time a receiver of same
type is encountered, the linking is delegated to those linkers only, speeding
up dispatch.

public class

CompositeTypeBasedGuardingDynamicLinker

extends

Object

implements

TypeBasedGuardingDynamicLinker

A composite type-based guarding dynamic linker. When a receiver of a not yet
seen class is encountered, all linkers are queried sequentially on their

TypeBasedGuardingDynamicLinker.canLinkType(Class)

method. The linkers
returning true are then bound to the class, and next time a receiver of same
type is encountered, the linking is delegated to those linkers only, speeding
up dispatch.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CompositeTypeBasedGuardingDynamicLinker

​(

Iterable

<? extends

TypeBasedGuardingDynamicLinker

> linkers)

Creates a new composite type-based linker.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canLinkType

​(

Class

<?> type)

Returns true if at least one of the composite linkers returns true from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

for the type.

static

List

<

GuardingDynamicLinker

>

optimize

​(

Iterable

<? extends

GuardingDynamicLinker

> linkers)

Optimizes a list of type-based linkers.

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

- Methods declared in interface jdk.dynalink.linker.

GuardingDynamicLinker

getGuardedInvocation

Constructor Summary

Constructors

Constructor

Description

CompositeTypeBasedGuardingDynamicLinker

​(

Iterable

<? extends

TypeBasedGuardingDynamicLinker

> linkers)

Creates a new composite type-based linker.

---

#### Constructor Summary

Creates a new composite type-based linker.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canLinkType

​(

Class

<?> type)

Returns true if at least one of the composite linkers returns true from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

for the type.

static

List

<

GuardingDynamicLinker

>

optimize

​(

Iterable

<? extends

GuardingDynamicLinker

> linkers)

Optimizes a list of type-based linkers.

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

- Methods declared in interface jdk.dynalink.linker.

GuardingDynamicLinker

getGuardedInvocation

---

#### Method Summary

Returns true if at least one of the composite linkers returns true from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

for the type.

Optimizes a list of type-based linkers.

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

Methods declared in interface jdk.dynalink.linker.

GuardingDynamicLinker

getGuardedInvocation

---

#### Methods declared in interface jdk.dynalink.linker. GuardingDynamicLinker

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CompositeTypeBasedGuardingDynamicLinker

```java
public CompositeTypeBasedGuardingDynamicLinker​(
Iterable
<? extends
TypeBasedGuardingDynamicLinker
> linkers)
```

Creates a new composite type-based linker.

**Parameters:** linkers

- the component linkers
**Throws:** NullPointerException

- if

linkers

or any of its elements
are null.

============ METHOD DETAIL ==========

- Method Detail

- canLinkType

```java
public boolean canLinkType​(
Class
<?> type)
```

Returns true if at least one of the composite linkers returns true from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

for the type.

**Specified by:** canLinkType

in interface

TypeBasedGuardingDynamicLinker
**Parameters:** type

- the type to link
**Returns:** true true if at least one of the composite linkers returns true
from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

, false
otherwise.

- optimize

```java
public static
List
<
GuardingDynamicLinker
> optimize​(
Iterable
<? extends
GuardingDynamicLinker
> linkers)
```

Optimizes a list of type-based linkers. If a group of adjacent linkers in
the list all implement

TypeBasedGuardingDynamicLinker

, they will
be replaced with a single instance of

CompositeTypeBasedGuardingDynamicLinker

that contains them.

**Parameters:** linkers

- the list of linkers to optimize
**Returns:** the optimized list
**Throws:** NullPointerException

- if

linkers

or any of its elements
are null.

Constructor Detail

- CompositeTypeBasedGuardingDynamicLinker

```java
public CompositeTypeBasedGuardingDynamicLinker​(
Iterable
<? extends
TypeBasedGuardingDynamicLinker
> linkers)
```

Creates a new composite type-based linker.

**Parameters:** linkers

- the component linkers
**Throws:** NullPointerException

- if

linkers

or any of its elements
are null.

---

#### Constructor Detail

CompositeTypeBasedGuardingDynamicLinker

```java
public CompositeTypeBasedGuardingDynamicLinker​(
Iterable
<? extends
TypeBasedGuardingDynamicLinker
> linkers)
```

Creates a new composite type-based linker.

**Parameters:** linkers

- the component linkers
**Throws:** NullPointerException

- if

linkers

or any of its elements
are null.

---

#### CompositeTypeBasedGuardingDynamicLinker

public CompositeTypeBasedGuardingDynamicLinker​(

Iterable

<? extends

TypeBasedGuardingDynamicLinker

> linkers)

Creates a new composite type-based linker.

Method Detail

- canLinkType

```java
public boolean canLinkType​(
Class
<?> type)
```

Returns true if at least one of the composite linkers returns true from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

for the type.

**Specified by:** canLinkType

in interface

TypeBasedGuardingDynamicLinker
**Parameters:** type

- the type to link
**Returns:** true true if at least one of the composite linkers returns true
from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

, false
otherwise.

- optimize

```java
public static
List
<
GuardingDynamicLinker
> optimize​(
Iterable
<? extends
GuardingDynamicLinker
> linkers)
```

Optimizes a list of type-based linkers. If a group of adjacent linkers in
the list all implement

TypeBasedGuardingDynamicLinker

, they will
be replaced with a single instance of

CompositeTypeBasedGuardingDynamicLinker

that contains them.

**Parameters:** linkers

- the list of linkers to optimize
**Returns:** the optimized list
**Throws:** NullPointerException

- if

linkers

or any of its elements
are null.

---

#### Method Detail

canLinkType

```java
public boolean canLinkType​(
Class
<?> type)
```

Returns true if at least one of the composite linkers returns true from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

for the type.

**Specified by:** canLinkType

in interface

TypeBasedGuardingDynamicLinker
**Parameters:** type

- the type to link
**Returns:** true true if at least one of the composite linkers returns true
from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

, false
otherwise.

---

#### canLinkType

public boolean canLinkType​(

Class

<?> type)

Returns true if at least one of the composite linkers returns true from

TypeBasedGuardingDynamicLinker.canLinkType(Class)

for the type.

optimize

```java
public static
List
<
GuardingDynamicLinker
> optimize​(
Iterable
<? extends
GuardingDynamicLinker
> linkers)
```

Optimizes a list of type-based linkers. If a group of adjacent linkers in
the list all implement

TypeBasedGuardingDynamicLinker

, they will
be replaced with a single instance of

CompositeTypeBasedGuardingDynamicLinker

that contains them.

**Parameters:** linkers

- the list of linkers to optimize
**Returns:** the optimized list
**Throws:** NullPointerException

- if

linkers

or any of its elements
are null.

---

#### optimize

public static

List

<

GuardingDynamicLinker

> optimize​(

Iterable

<? extends

GuardingDynamicLinker

> linkers)

Optimizes a list of type-based linkers. If a group of adjacent linkers in
the list all implement

TypeBasedGuardingDynamicLinker

, they will
be replaced with a single instance of

CompositeTypeBasedGuardingDynamicLinker

that contains them.

---

