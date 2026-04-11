# Class SSLSessionBindingEvent

**Source:** `java.base\javax\net\ssl\SSLSessionBindingEvent.html`

### Class Description

```java
public class
SSLSessionBindingEvent

extends
EventObject
```

This event is propagated to a SSLSessionBindingListener.
When a listener object is bound or unbound to an SSLSession by

SSLSession.putValue(String, Object)

or

SSLSession.removeValue(String)

, objects which
implement the SSLSessionBindingListener will be receive an
event of this type. The event's

name

field is the
key in which the listener is being bound or unbound.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SSLSessionBindingEvent​(
SSLSession
session,

String
name)

Constructs a new SSLSessionBindingEvent.

**Parameters:**
- session

- the SSLSession acting as the source of the event
- name

- the name to which the object is being bound or unbound

**Throws:**
- IllegalArgumentException

- if

session

is null.

---

### Method Details

#### public
String
getName()

Returns the name to which the object is being bound, or the name
from which the object is being unbound.

**Returns:**
- the name to which the object is being bound or unbound

---

#### public
SSLSession
getSession()

Returns the SSLSession into which the listener is being bound or
from which the listener is being unbound.

**Returns:**
- the

SSLSession

---

### Additional Sections

#### Class SSLSessionBindingEvent

java.lang.Object

- java.util.EventObject
- - javax.net.ssl.SSLSessionBindingEvent

java.util.EventObject

- javax.net.ssl.SSLSessionBindingEvent

javax.net.ssl.SSLSessionBindingEvent

**All Implemented Interfaces:** Serializable

```java
public class
SSLSessionBindingEvent

extends
EventObject
```

This event is propagated to a SSLSessionBindingListener.
When a listener object is bound or unbound to an SSLSession by

SSLSession.putValue(String, Object)

or

SSLSession.removeValue(String)

, objects which
implement the SSLSessionBindingListener will be receive an
event of this type. The event's

name

field is the
key in which the listener is being bound or unbound.

**Since:** 1.4
**See Also:** SSLSession

,

SSLSessionBindingListener

,

Serialized Form

public class

SSLSessionBindingEvent

extends

EventObject

This event is propagated to a SSLSessionBindingListener.
When a listener object is bound or unbound to an SSLSession by

SSLSession.putValue(String, Object)

or

SSLSession.removeValue(String)

, objects which
implement the SSLSessionBindingListener will be receive an
event of this type. The event's

name

field is the
key in which the listener is being bound or unbound.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SSLSessionBindingEvent

​(

SSLSession

session,

String

name)

Constructs a new SSLSessionBindingEvent.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name to which the object is being bound, or the name
from which the object is being unbound.

SSLSession

getSession

()

Returns the SSLSession into which the listener is being bound or
from which the listener is being unbound.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

SSLSessionBindingEvent

​(

SSLSession

session,

String

name)

Constructs a new SSLSessionBindingEvent.

---

#### Constructor Summary

Constructs a new SSLSessionBindingEvent.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name to which the object is being bound, or the name
from which the object is being unbound.

SSLSession

getSession

()

Returns the SSLSession into which the listener is being bound or
from which the listener is being unbound.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

Returns the name to which the object is being bound, or the name
from which the object is being unbound.

Returns the SSLSession into which the listener is being bound or
from which the listener is being unbound.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

- SSLSessionBindingEvent

```java
public SSLSessionBindingEvent​(
SSLSession
session,

String
name)
```

Constructs a new SSLSessionBindingEvent.

**Parameters:** session

- the SSLSession acting as the source of the event
**Parameters:** name

- the name to which the object is being bound or unbound
**Throws:** IllegalArgumentException

- if

session

is null.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the name to which the object is being bound, or the name
from which the object is being unbound.

**Returns:** the name to which the object is being bound or unbound

- getSession

```java
public
SSLSession
getSession()
```

Returns the SSLSession into which the listener is being bound or
from which the listener is being unbound.

**Returns:** the

SSLSession

Constructor Detail

- SSLSessionBindingEvent

```java
public SSLSessionBindingEvent​(
SSLSession
session,

String
name)
```

Constructs a new SSLSessionBindingEvent.

**Parameters:** session

- the SSLSession acting as the source of the event
**Parameters:** name

- the name to which the object is being bound or unbound
**Throws:** IllegalArgumentException

- if

session

is null.

---

#### Constructor Detail

SSLSessionBindingEvent

```java
public SSLSessionBindingEvent​(
SSLSession
session,

String
name)
```

Constructs a new SSLSessionBindingEvent.

**Parameters:** session

- the SSLSession acting as the source of the event
**Parameters:** name

- the name to which the object is being bound or unbound
**Throws:** IllegalArgumentException

- if

session

is null.

---

#### SSLSessionBindingEvent

public SSLSessionBindingEvent​(

SSLSession

session,

String

name)

Constructs a new SSLSessionBindingEvent.

Method Detail

- getName

```java
public
String
getName()
```

Returns the name to which the object is being bound, or the name
from which the object is being unbound.

**Returns:** the name to which the object is being bound or unbound

- getSession

```java
public
SSLSession
getSession()
```

Returns the SSLSession into which the listener is being bound or
from which the listener is being unbound.

**Returns:** the

SSLSession

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the name to which the object is being bound, or the name
from which the object is being unbound.

**Returns:** the name to which the object is being bound or unbound

---

#### getName

public

String

getName()

Returns the name to which the object is being bound, or the name
from which the object is being unbound.

getSession

```java
public
SSLSession
getSession()
```

Returns the SSLSession into which the listener is being bound or
from which the listener is being unbound.

**Returns:** the

SSLSession

---

#### getSession

public

SSLSession

getSession()

Returns the SSLSession into which the listener is being bound or
from which the listener is being unbound.

---

