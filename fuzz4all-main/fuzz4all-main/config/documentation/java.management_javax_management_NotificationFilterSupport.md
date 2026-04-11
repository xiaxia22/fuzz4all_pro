# Class NotificationFilterSupport

**Source:** `java.management\javax\management\NotificationFilterSupport.html`

### Class Description

```java
public class
NotificationFilterSupport

extends
Object

implements
NotificationFilter
```

Provides an implementation of the

NotificationFilter

interface.
The filtering is performed on the notification type attribute.

Manages a list of enabled notification types.
A method allows users to enable/disable as many notification types as required.

Then, before sending a notification to a listener registered with a filter,
the notification broadcaster compares this notification type with all notification types
enabled by the filter. The notification will be sent to the listener
only if its filter enables this notification type.

Example:

```java
NotificationFilterSupport myFilter = new NotificationFilterSupport();
myFilter.enableType("my_example.my_type");
myBroadcaster.addListener(myListener, myFilter, null);
```

The listener

myListener

will only receive notifications the type of which equals/starts with "my_example.my_type".

**All Implemented Interfaces:** Serializable

,

NotificationFilter

---

### Field Details

*No entries found.*

### Constructor Details

#### public NotificationFilterSupport()

*No description found.*

---

### Method Details

#### public boolean isNotificationEnabled​(
Notification
notification)

Invoked before sending the specified notification to the listener.

This filter compares the type of the specified notification with each enabled type.
If the notification type matches one of the enabled types,
the notification should be sent to the listener and this method returns

true

.

**Specified by:**
- isNotificationEnabled

in interface

NotificationFilter

**Parameters:**
- notification

- The notification to be sent.

**Returns:**
- true

if the notification should be sent to the listener,

false

otherwise.

---

#### public void enableType​(
String
prefix)
throws
IllegalArgumentException

Enables all the notifications the type of which starts with the specified prefix
to be sent to the listener.

If the specified prefix is already in the list of enabled notification types,
this method has no effect.

Example:

```java
// Enables all notifications the type of which starts with "my_example" to be sent.
myFilter.enableType("my_example");
// Enables all notifications the type of which is "my_example.my_type" to be sent.
myFilter.enableType("my_example.my_type");
```

Note that:

myFilter.enableType("my_example.*");

will no match any notification type.

**Parameters:**
- prefix

- The prefix.

**Throws:**
- IllegalArgumentException

- The prefix parameter is null.

---

#### public void disableType​(
String
prefix)

Removes the given prefix from the prefix list.

If the specified prefix is not in the list of enabled notification types,
this method has no effect.

**Parameters:**
- prefix

- The prefix.

---

#### public void disableAllTypes()

Disables all notification types.

---

#### public
Vector
<
String
> getEnabledTypes()

Gets all the enabled notification types for this filter.

**Returns:**
- The list containing all the enabled notification types.

---

### Additional Sections

#### Class NotificationFilterSupport

java.lang.Object

- javax.management.NotificationFilterSupport

javax.management.NotificationFilterSupport

**All Implemented Interfaces:** Serializable

,

NotificationFilter

**Direct Known Subclasses:** MBeanServerNotificationFilter

```java
public class
NotificationFilterSupport

extends
Object

implements
NotificationFilter
```

Provides an implementation of the

NotificationFilter

interface.
The filtering is performed on the notification type attribute.

Manages a list of enabled notification types.
A method allows users to enable/disable as many notification types as required.

Then, before sending a notification to a listener registered with a filter,
the notification broadcaster compares this notification type with all notification types
enabled by the filter. The notification will be sent to the listener
only if its filter enables this notification type.

Example:

```java
NotificationFilterSupport myFilter = new NotificationFilterSupport();
myFilter.enableType("my_example.my_type");
myBroadcaster.addListener(myListener, myFilter, null);
```

The listener

myListener

will only receive notifications the type of which equals/starts with "my_example.my_type".

**Since:** 1.5
**See Also:** NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

Serialized Form

public class

NotificationFilterSupport

extends

Object

implements

NotificationFilter

Provides an implementation of the

NotificationFilter

interface.
The filtering is performed on the notification type attribute.

Manages a list of enabled notification types.
A method allows users to enable/disable as many notification types as required.

Then, before sending a notification to a listener registered with a filter,
the notification broadcaster compares this notification type with all notification types
enabled by the filter. The notification will be sent to the listener
only if its filter enables this notification type.

Example:

```java
NotificationFilterSupport myFilter = new NotificationFilterSupport();
myFilter.enableType("my_example.my_type");
myBroadcaster.addListener(myListener, myFilter, null);
```

The listener

myListener

will only receive notifications the type of which equals/starts with "my_example.my_type".

Manages a list of enabled notification types.
A method allows users to enable/disable as many notification types as required.

Then, before sending a notification to a listener registered with a filter,
the notification broadcaster compares this notification type with all notification types
enabled by the filter. The notification will be sent to the listener
only if its filter enables this notification type.

Example:

```java
NotificationFilterSupport myFilter = new NotificationFilterSupport();
myFilter.enableType("my_example.my_type");
myBroadcaster.addListener(myListener, myFilter, null);
```

The listener

myListener

will only receive notifications the type of which equals/starts with "my_example.my_type".

Then, before sending a notification to a listener registered with a filter,
the notification broadcaster compares this notification type with all notification types
enabled by the filter. The notification will be sent to the listener
only if its filter enables this notification type.

Example:

```java
NotificationFilterSupport myFilter = new NotificationFilterSupport();
myFilter.enableType("my_example.my_type");
myBroadcaster.addListener(myListener, myFilter, null);
```

The listener

myListener

will only receive notifications the type of which equals/starts with "my_example.my_type".

Example:

```java
NotificationFilterSupport myFilter = new NotificationFilterSupport();
myFilter.enableType("my_example.my_type");
myBroadcaster.addListener(myListener, myFilter, null);
```

The listener

myListener

will only receive notifications the type of which equals/starts with "my_example.my_type".

NotificationFilterSupport myFilter = new NotificationFilterSupport();
myFilter.enableType("my_example.my_type");
myBroadcaster.addListener(myListener, myFilter, null);

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NotificationFilterSupport

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

disableAllTypes

()

Disables all notification types.

void

disableType

​(

String

prefix)

Removes the given prefix from the prefix list.

void

enableType

​(

String

prefix)

Enables all the notifications the type of which starts with the specified prefix
to be sent to the listener.

Vector

<

String

>

getEnabledTypes

()

Gets all the enabled notification types for this filter.

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

NotificationFilterSupport

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

disableAllTypes

()

Disables all notification types.

void

disableType

​(

String

prefix)

Removes the given prefix from the prefix list.

void

enableType

​(

String

prefix)

Enables all the notifications the type of which starts with the specified prefix
to be sent to the listener.

Vector

<

String

>

getEnabledTypes

()

Gets all the enabled notification types for this filter.

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

Disables all notification types.

Removes the given prefix from the prefix list.

Enables all the notifications the type of which starts with the specified prefix
to be sent to the listener.

Gets all the enabled notification types for this filter.

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

- NotificationFilterSupport

```java
public NotificationFilterSupport()
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

This filter compares the type of the specified notification with each enabled type.
If the notification type matches one of the enabled types,
the notification should be sent to the listener and this method returns

true

.

**Specified by:** isNotificationEnabled

in interface

NotificationFilter
**Parameters:** notification

- The notification to be sent.
**Returns:** true

if the notification should be sent to the listener,

false

otherwise.

- enableType

```java
public void enableType​(
String
prefix)
throws
IllegalArgumentException
```

Enables all the notifications the type of which starts with the specified prefix
to be sent to the listener.

If the specified prefix is already in the list of enabled notification types,
this method has no effect.

Example:

```java
// Enables all notifications the type of which starts with "my_example" to be sent.
myFilter.enableType("my_example");
// Enables all notifications the type of which is "my_example.my_type" to be sent.
myFilter.enableType("my_example.my_type");
```

Note that:

myFilter.enableType("my_example.*");

will no match any notification type.

**Parameters:** prefix

- The prefix.
**Throws:** IllegalArgumentException

- The prefix parameter is null.

- disableType

```java
public void disableType​(
String
prefix)
```

Removes the given prefix from the prefix list.

If the specified prefix is not in the list of enabled notification types,
this method has no effect.

**Parameters:** prefix

- The prefix.

- disableAllTypes

```java
public void disableAllTypes()
```

Disables all notification types.

- getEnabledTypes

```java
public
Vector
<
String
> getEnabledTypes()
```

Gets all the enabled notification types for this filter.

**Returns:** The list containing all the enabled notification types.

Constructor Detail

- NotificationFilterSupport

```java
public NotificationFilterSupport()
```

---

#### Constructor Detail

NotificationFilterSupport

```java
public NotificationFilterSupport()
```

---

#### NotificationFilterSupport

public NotificationFilterSupport()

Method Detail

- isNotificationEnabled

```java
public boolean isNotificationEnabled​(
Notification
notification)
```

Invoked before sending the specified notification to the listener.

This filter compares the type of the specified notification with each enabled type.
If the notification type matches one of the enabled types,
the notification should be sent to the listener and this method returns

true

.

**Specified by:** isNotificationEnabled

in interface

NotificationFilter
**Parameters:** notification

- The notification to be sent.
**Returns:** true

if the notification should be sent to the listener,

false

otherwise.

- enableType

```java
public void enableType​(
String
prefix)
throws
IllegalArgumentException
```

Enables all the notifications the type of which starts with the specified prefix
to be sent to the listener.

If the specified prefix is already in the list of enabled notification types,
this method has no effect.

Example:

```java
// Enables all notifications the type of which starts with "my_example" to be sent.
myFilter.enableType("my_example");
// Enables all notifications the type of which is "my_example.my_type" to be sent.
myFilter.enableType("my_example.my_type");
```

Note that:

myFilter.enableType("my_example.*");

will no match any notification type.

**Parameters:** prefix

- The prefix.
**Throws:** IllegalArgumentException

- The prefix parameter is null.

- disableType

```java
public void disableType​(
String
prefix)
```

Removes the given prefix from the prefix list.

If the specified prefix is not in the list of enabled notification types,
this method has no effect.

**Parameters:** prefix

- The prefix.

- disableAllTypes

```java
public void disableAllTypes()
```

Disables all notification types.

- getEnabledTypes

```java
public
Vector
<
String
> getEnabledTypes()
```

Gets all the enabled notification types for this filter.

**Returns:** The list containing all the enabled notification types.

---

#### Method Detail

isNotificationEnabled

```java
public boolean isNotificationEnabled​(
Notification
notification)
```

Invoked before sending the specified notification to the listener.

This filter compares the type of the specified notification with each enabled type.
If the notification type matches one of the enabled types,
the notification should be sent to the listener and this method returns

true

.

**Specified by:** isNotificationEnabled

in interface

NotificationFilter
**Parameters:** notification

- The notification to be sent.
**Returns:** true

if the notification should be sent to the listener,

false

otherwise.

---

#### isNotificationEnabled

public boolean isNotificationEnabled​(

Notification

notification)

Invoked before sending the specified notification to the listener.

This filter compares the type of the specified notification with each enabled type.
If the notification type matches one of the enabled types,
the notification should be sent to the listener and this method returns

true

.

enableType

```java
public void enableType​(
String
prefix)
throws
IllegalArgumentException
```

Enables all the notifications the type of which starts with the specified prefix
to be sent to the listener.

If the specified prefix is already in the list of enabled notification types,
this method has no effect.

Example:

```java
// Enables all notifications the type of which starts with "my_example" to be sent.
myFilter.enableType("my_example");
// Enables all notifications the type of which is "my_example.my_type" to be sent.
myFilter.enableType("my_example.my_type");
```

Note that:

myFilter.enableType("my_example.*");

will no match any notification type.

**Parameters:** prefix

- The prefix.
**Throws:** IllegalArgumentException

- The prefix parameter is null.

---

#### enableType

public void enableType​(

String

prefix)
throws

IllegalArgumentException

Enables all the notifications the type of which starts with the specified prefix
to be sent to the listener.

If the specified prefix is already in the list of enabled notification types,
this method has no effect.

Example:

```java
// Enables all notifications the type of which starts with "my_example" to be sent.
myFilter.enableType("my_example");
// Enables all notifications the type of which is "my_example.my_type" to be sent.
myFilter.enableType("my_example.my_type");
```

Note that:

myFilter.enableType("my_example.*");

will no match any notification type.

Example:

```java
// Enables all notifications the type of which starts with "my_example" to be sent.
myFilter.enableType("my_example");
// Enables all notifications the type of which is "my_example.my_type" to be sent.
myFilter.enableType("my_example.my_type");
```

Note that:

myFilter.enableType("my_example.*");

will no match any notification type.

// Enables all notifications the type of which starts with "my_example" to be sent.
myFilter.enableType("my_example");
// Enables all notifications the type of which is "my_example.my_type" to be sent.
myFilter.enableType("my_example.my_type");

disableType

```java
public void disableType​(
String
prefix)
```

Removes the given prefix from the prefix list.

If the specified prefix is not in the list of enabled notification types,
this method has no effect.

**Parameters:** prefix

- The prefix.

---

#### disableType

public void disableType​(

String

prefix)

Removes the given prefix from the prefix list.

If the specified prefix is not in the list of enabled notification types,
this method has no effect.

disableAllTypes

```java
public void disableAllTypes()
```

Disables all notification types.

---

#### disableAllTypes

public void disableAllTypes()

Disables all notification types.

getEnabledTypes

```java
public
Vector
<
String
> getEnabledTypes()
```

Gets all the enabled notification types for this filter.

**Returns:** The list containing all the enabled notification types.

---

#### getEnabledTypes

public

Vector

<

String

> getEnabledTypes()

Gets all the enabled notification types for this filter.

---

