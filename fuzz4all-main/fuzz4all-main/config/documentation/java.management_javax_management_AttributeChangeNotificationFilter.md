# Class AttributeChangeNotificationFilter

**Source:** `java.management\javax\management\AttributeChangeNotificationFilter.html`

### Class Description

```java
public class
AttributeChangeNotificationFilter

extends
Object

implements
NotificationFilter
```

This class implements of the

NotificationFilter

interface for the

attribute change notification

.
The filtering is performed on the name of the observed attribute.

It manages a list of enabled attribute names.
A method allows users to enable/disable as many attribute names as required.

**All Implemented Interfaces:** Serializable

,

NotificationFilter

---

### Field Details

*No entries found.*

### Constructor Details

#### public AttributeChangeNotificationFilter()

*No description found.*

---

### Method Details

#### public boolean isNotificationEnabled​(
Notification
notification)

Invoked before sending the specified notification to the listener.

This filter compares the attribute name of the specified attribute change notification
with each enabled attribute name.
If the attribute name equals one of the enabled attribute names,
the notification must be sent to the listener and this method returns

true

.

**Specified by:**
- isNotificationEnabled

in interface

NotificationFilter

**Parameters:**
- notification

- The attribute change notification to be sent.

**Returns:**
- true

if the notification has to be sent to the listener,

false

otherwise.

---

#### public void enableAttribute​(
String
name)
throws
IllegalArgumentException

Enables all the attribute change notifications the attribute name of which equals
the specified name to be sent to the listener.

If the specified name is already in the list of enabled attribute names,
this method has no effect.

**Parameters:**
- name

- The attribute name.

**Throws:**
- IllegalArgumentException

- The attribute name parameter is null.

---

#### public void disableAttribute​(
String
name)

Disables all the attribute change notifications the attribute name of which equals
the specified attribute name to be sent to the listener.

If the specified name is not in the list of enabled attribute names,
this method has no effect.

**Parameters:**
- name

- The attribute name.

---

#### public void disableAllAttributes()

Disables all the attribute names.

---

#### public
Vector
<
String
> getEnabledAttributes()

Gets all the enabled attribute names for this filter.

**Returns:**
- The list containing all the enabled attribute names.

---

### Additional Sections

#### Class AttributeChangeNotificationFilter

java.lang.Object

- javax.management.AttributeChangeNotificationFilter

javax.management.AttributeChangeNotificationFilter

**All Implemented Interfaces:** Serializable

,

NotificationFilter

```java
public class
AttributeChangeNotificationFilter

extends
Object

implements
NotificationFilter
```

This class implements of the

NotificationFilter

interface for the

attribute change notification

.
The filtering is performed on the name of the observed attribute.

It manages a list of enabled attribute names.
A method allows users to enable/disable as many attribute names as required.

**Since:** 1.5
**See Also:** Serialized Form

public class

AttributeChangeNotificationFilter

extends

Object

implements

NotificationFilter

This class implements of the

NotificationFilter

interface for the

attribute change notification

.
The filtering is performed on the name of the observed attribute.

It manages a list of enabled attribute names.
A method allows users to enable/disable as many attribute names as required.

It manages a list of enabled attribute names.
A method allows users to enable/disable as many attribute names as required.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AttributeChangeNotificationFilter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

disableAllAttributes

()

Disables all the attribute names.

void

disableAttribute

​(

String

name)

Disables all the attribute change notifications the attribute name of which equals
the specified attribute name to be sent to the listener.

void

enableAttribute

​(

String

name)

Enables all the attribute change notifications the attribute name of which equals
the specified name to be sent to the listener.

Vector

<

String

>

getEnabledAttributes

()

Gets all the enabled attribute names for this filter.

boolean

isNotificationEnabled

​(

Notification

notification)

Invoked before sending the specified notification to the listener.

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

AttributeChangeNotificationFilter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

disableAllAttributes

()

Disables all the attribute names.

void

disableAttribute

​(

String

name)

Disables all the attribute change notifications the attribute name of which equals
the specified attribute name to be sent to the listener.

void

enableAttribute

​(

String

name)

Enables all the attribute change notifications the attribute name of which equals
the specified name to be sent to the listener.

Vector

<

String

>

getEnabledAttributes

()

Gets all the enabled attribute names for this filter.

boolean

isNotificationEnabled

​(

Notification

notification)

Invoked before sending the specified notification to the listener.

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

Disables all the attribute names.

Disables all the attribute change notifications the attribute name of which equals
the specified attribute name to be sent to the listener.

Enables all the attribute change notifications the attribute name of which equals
the specified name to be sent to the listener.

Gets all the enabled attribute names for this filter.

Invoked before sending the specified notification to the listener.

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

- AttributeChangeNotificationFilter

```java
public AttributeChangeNotificationFilter()
```

============ METHOD DETAIL ==========

- Method Detail

- isNotificationEnabled

```java
public boolean isNotificationEnabled​(
Notification
notification)
```

Invoked before sending the specified notification to the listener.

This filter compares the attribute name of the specified attribute change notification
with each enabled attribute name.
If the attribute name equals one of the enabled attribute names,
the notification must be sent to the listener and this method returns

true

.

**Specified by:** isNotificationEnabled

in interface

NotificationFilter
**Parameters:** notification

- The attribute change notification to be sent.
**Returns:** true

if the notification has to be sent to the listener,

false

otherwise.

- enableAttribute

```java
public void enableAttribute​(
String
name)
throws
IllegalArgumentException
```

Enables all the attribute change notifications the attribute name of which equals
the specified name to be sent to the listener.

If the specified name is already in the list of enabled attribute names,
this method has no effect.

**Parameters:** name

- The attribute name.
**Throws:** IllegalArgumentException

- The attribute name parameter is null.

- disableAttribute

```java
public void disableAttribute​(
String
name)
```

Disables all the attribute change notifications the attribute name of which equals
the specified attribute name to be sent to the listener.

If the specified name is not in the list of enabled attribute names,
this method has no effect.

**Parameters:** name

- The attribute name.

- disableAllAttributes

```java
public void disableAllAttributes()
```

Disables all the attribute names.

- getEnabledAttributes

```java
public
Vector
<
String
> getEnabledAttributes()
```

Gets all the enabled attribute names for this filter.

**Returns:** The list containing all the enabled attribute names.

Constructor Detail

- AttributeChangeNotificationFilter

```java
public AttributeChangeNotificationFilter()
```

---

#### Constructor Detail

AttributeChangeNotificationFilter

```java
public AttributeChangeNotificationFilter()
```

---

#### AttributeChangeNotificationFilter

public AttributeChangeNotificationFilter()

Method Detail

- isNotificationEnabled

```java
public boolean isNotificationEnabled​(
Notification
notification)
```

Invoked before sending the specified notification to the listener.

This filter compares the attribute name of the specified attribute change notification
with each enabled attribute name.
If the attribute name equals one of the enabled attribute names,
the notification must be sent to the listener and this method returns

true

.

**Specified by:** isNotificationEnabled

in interface

NotificationFilter
**Parameters:** notification

- The attribute change notification to be sent.
**Returns:** true

if the notification has to be sent to the listener,

false

otherwise.

- enableAttribute

```java
public void enableAttribute​(
String
name)
throws
IllegalArgumentException
```

Enables all the attribute change notifications the attribute name of which equals
the specified name to be sent to the listener.

If the specified name is already in the list of enabled attribute names,
this method has no effect.

**Parameters:** name

- The attribute name.
**Throws:** IllegalArgumentException

- The attribute name parameter is null.

- disableAttribute

```java
public void disableAttribute​(
String
name)
```

Disables all the attribute change notifications the attribute name of which equals
the specified attribute name to be sent to the listener.

If the specified name is not in the list of enabled attribute names,
this method has no effect.

**Parameters:** name

- The attribute name.

- disableAllAttributes

```java
public void disableAllAttributes()
```

Disables all the attribute names.

- getEnabledAttributes

```java
public
Vector
<
String
> getEnabledAttributes()
```

Gets all the enabled attribute names for this filter.

**Returns:** The list containing all the enabled attribute names.

---

#### Method Detail

isNotificationEnabled

```java
public boolean isNotificationEnabled​(
Notification
notification)
```

Invoked before sending the specified notification to the listener.

This filter compares the attribute name of the specified attribute change notification
with each enabled attribute name.
If the attribute name equals one of the enabled attribute names,
the notification must be sent to the listener and this method returns

true

.

**Specified by:** isNotificationEnabled

in interface

NotificationFilter
**Parameters:** notification

- The attribute change notification to be sent.
**Returns:** true

if the notification has to be sent to the listener,

false

otherwise.

---

#### isNotificationEnabled

public boolean isNotificationEnabled​(

Notification

notification)

Invoked before sending the specified notification to the listener.

This filter compares the attribute name of the specified attribute change notification
with each enabled attribute name.
If the attribute name equals one of the enabled attribute names,
the notification must be sent to the listener and this method returns

true

.

enableAttribute

```java
public void enableAttribute​(
String
name)
throws
IllegalArgumentException
```

Enables all the attribute change notifications the attribute name of which equals
the specified name to be sent to the listener.

If the specified name is already in the list of enabled attribute names,
this method has no effect.

**Parameters:** name

- The attribute name.
**Throws:** IllegalArgumentException

- The attribute name parameter is null.

---

#### enableAttribute

public void enableAttribute​(

String

name)
throws

IllegalArgumentException

Enables all the attribute change notifications the attribute name of which equals
the specified name to be sent to the listener.

If the specified name is already in the list of enabled attribute names,
this method has no effect.

disableAttribute

```java
public void disableAttribute​(
String
name)
```

Disables all the attribute change notifications the attribute name of which equals
the specified attribute name to be sent to the listener.

If the specified name is not in the list of enabled attribute names,
this method has no effect.

**Parameters:** name

- The attribute name.

---

#### disableAttribute

public void disableAttribute​(

String

name)

Disables all the attribute change notifications the attribute name of which equals
the specified attribute name to be sent to the listener.

If the specified name is not in the list of enabled attribute names,
this method has no effect.

disableAllAttributes

```java
public void disableAllAttributes()
```

Disables all the attribute names.

---

#### disableAllAttributes

public void disableAllAttributes()

Disables all the attribute names.

getEnabledAttributes

```java
public
Vector
<
String
> getEnabledAttributes()
```

Gets all the enabled attribute names for this filter.

**Returns:** The list containing all the enabled attribute names.

---

#### getEnabledAttributes

public

Vector

<

String

> getEnabledAttributes()

Gets all the enabled attribute names for this filter.

---

