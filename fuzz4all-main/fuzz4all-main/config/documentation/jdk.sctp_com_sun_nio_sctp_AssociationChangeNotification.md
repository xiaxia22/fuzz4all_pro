# Class AssociationChangeNotification

**Source:** `jdk.sctp\com\sun\nio\sctp\AssociationChangeNotification.html`

### Class Description

```java
public abstract class
AssociationChangeNotification

extends
Object

implements
Notification
```

Notification emitted when an association has either opened or closed.

**All Implemented Interfaces:** Notification

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AssociationChangeNotification()

Initializes a new instance of this class.

---

### Method Details

#### public abstract
Association
association()

Returns the association that this notification is applicable to.

**Specified by:**
- association

in interface

Notification

**Returns:**
- The association whose state has changed, or

null

if
there is no association, that is

CANT_START

---

#### public abstract
AssociationChangeNotification.AssocChangeEvent
event()

Returns the type of change event.

**Returns:**
- The event

---

### Additional Sections

#### Class AssociationChangeNotification

java.lang.Object

- com.sun.nio.sctp.AssociationChangeNotification

com.sun.nio.sctp.AssociationChangeNotification

**All Implemented Interfaces:** Notification

```java
public abstract class
AssociationChangeNotification

extends
Object

implements
Notification
```

Notification emitted when an association has either opened or closed.

**Since:** 1.7

public abstract class

AssociationChangeNotification

extends

Object

implements

Notification

Notification emitted when an association has either opened or closed.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

AssociationChangeNotification.AssocChangeEvent

Defines the type of change event that happened to the association.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AssociationChangeNotification

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Association

association

()

Returns the association that this notification is applicable to.

abstract

AssociationChangeNotification.AssocChangeEvent

event

()

Returns the type of change event.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

AssociationChangeNotification.AssocChangeEvent

Defines the type of change event that happened to the association.

---

#### Nested Class Summary

Defines the type of change event that happened to the association.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AssociationChangeNotification

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Association

association

()

Returns the association that this notification is applicable to.

abstract

AssociationChangeNotification.AssocChangeEvent

event

()

Returns the type of change event.

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

Returns the association that this notification is applicable to.

Returns the type of change event.

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

- AssociationChangeNotification

```java
protected AssociationChangeNotification()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- association

```java
public abstract
Association
association()
```

Returns the association that this notification is applicable to.

**Specified by:** association

in interface

Notification
**Returns:** The association whose state has changed, or

null

if
there is no association, that is

CANT_START

- event

```java
public abstract
AssociationChangeNotification.AssocChangeEvent
event()
```

Returns the type of change event.

**Returns:** The event

Constructor Detail

- AssociationChangeNotification

```java
protected AssociationChangeNotification()
```

Initializes a new instance of this class.

---

#### Constructor Detail

AssociationChangeNotification

```java
protected AssociationChangeNotification()
```

Initializes a new instance of this class.

---

#### AssociationChangeNotification

protected AssociationChangeNotification()

Initializes a new instance of this class.

Method Detail

- association

```java
public abstract
Association
association()
```

Returns the association that this notification is applicable to.

**Specified by:** association

in interface

Notification
**Returns:** The association whose state has changed, or

null

if
there is no association, that is

CANT_START

- event

```java
public abstract
AssociationChangeNotification.AssocChangeEvent
event()
```

Returns the type of change event.

**Returns:** The event

---

#### Method Detail

association

```java
public abstract
Association
association()
```

Returns the association that this notification is applicable to.

**Specified by:** association

in interface

Notification
**Returns:** The association whose state has changed, or

null

if
there is no association, that is

CANT_START

---

#### association

public abstract

Association

association()

Returns the association that this notification is applicable to.

event

```java
public abstract
AssociationChangeNotification.AssocChangeEvent
event()
```

Returns the type of change event.

**Returns:** The event

---

#### event

public abstract

AssociationChangeNotification.AssocChangeEvent

event()

Returns the type of change event.

---

