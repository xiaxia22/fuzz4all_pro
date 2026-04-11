# Class PreferenceChangeEvent

**Source:** `java.prefs\java\util\prefs\PreferenceChangeEvent.html`

### Class Description

```java
public class
PreferenceChangeEvent

extends
EventObject
```

An event emitted by a

Preferences

node to indicate that
a preference has been added, removed or has had its value changed.

Note, that although PreferenceChangeEvent inherits Serializable interface
from EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PreferenceChangeEvent​(
Preferences
node,

String
key,

String
newValue)

Constructs a new

PreferenceChangeEvent

instance.

**Parameters:**
- node

- The Preferences node that emitted the event.
- key

- The key of the preference that was changed.
- newValue

- The new value of the preference, or

null

if the preference is being removed.

---

### Method Details

#### public
Preferences
getNode()

Returns the preference node that emitted the event.

**Returns:**
- The preference node that emitted the event.

---

#### public
String
getKey()

Returns the key of the preference that was changed.

**Returns:**
- The key of the preference that was changed.

---

#### public
String
getNewValue()

Returns the new value for the preference.

**Returns:**
- The new value for the preference, or

null

if the
preference was removed.

---

### Additional Sections

#### Class PreferenceChangeEvent

java.lang.Object

- java.util.EventObject
- - java.util.prefs.PreferenceChangeEvent

java.util.EventObject

- java.util.prefs.PreferenceChangeEvent

java.util.prefs.PreferenceChangeEvent

**All Implemented Interfaces:** Serializable

```java
public class
PreferenceChangeEvent

extends
EventObject
```

An event emitted by a

Preferences

node to indicate that
a preference has been added, removed or has had its value changed.

Note, that although PreferenceChangeEvent inherits Serializable interface
from EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.

**Since:** 1.4
**See Also:** Preferences

,

PreferenceChangeListener

,

NodeChangeEvent

public class

PreferenceChangeEvent

extends

EventObject

An event emitted by a

Preferences

node to indicate that
a preference has been added, removed or has had its value changed.

Note, that although PreferenceChangeEvent inherits Serializable interface
from EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.

Note, that although PreferenceChangeEvent inherits Serializable interface
from EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.

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

PreferenceChangeEvent

​(

Preferences

node,

String

key,

String

newValue)

Constructs a new

PreferenceChangeEvent

instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getKey

()

Returns the key of the preference that was changed.

String

getNewValue

()

Returns the new value for the preference.

Preferences

getNode

()

Returns the preference node that emitted the event.

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

PreferenceChangeEvent

​(

Preferences

node,

String

key,

String

newValue)

Constructs a new

PreferenceChangeEvent

instance.

---

#### Constructor Summary

Constructs a new

PreferenceChangeEvent

instance.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getKey

()

Returns the key of the preference that was changed.

String

getNewValue

()

Returns the new value for the preference.

Preferences

getNode

()

Returns the preference node that emitted the event.

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

Returns the key of the preference that was changed.

Returns the new value for the preference.

Returns the preference node that emitted the event.

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

- PreferenceChangeEvent

```java
public PreferenceChangeEvent​(
Preferences
node,

String
key,

String
newValue)
```

Constructs a new

PreferenceChangeEvent

instance.

**Parameters:** node

- The Preferences node that emitted the event.
**Parameters:** key

- The key of the preference that was changed.
**Parameters:** newValue

- The new value of the preference, or

null

if the preference is being removed.

============ METHOD DETAIL ==========

- Method Detail

- getNode

```java
public
Preferences
getNode()
```

Returns the preference node that emitted the event.

**Returns:** The preference node that emitted the event.

- getKey

```java
public
String
getKey()
```

Returns the key of the preference that was changed.

**Returns:** The key of the preference that was changed.

- getNewValue

```java
public
String
getNewValue()
```

Returns the new value for the preference.

**Returns:** The new value for the preference, or

null

if the
preference was removed.

Constructor Detail

- PreferenceChangeEvent

```java
public PreferenceChangeEvent​(
Preferences
node,

String
key,

String
newValue)
```

Constructs a new

PreferenceChangeEvent

instance.

**Parameters:** node

- The Preferences node that emitted the event.
**Parameters:** key

- The key of the preference that was changed.
**Parameters:** newValue

- The new value of the preference, or

null

if the preference is being removed.

---

#### Constructor Detail

PreferenceChangeEvent

```java
public PreferenceChangeEvent​(
Preferences
node,

String
key,

String
newValue)
```

Constructs a new

PreferenceChangeEvent

instance.

**Parameters:** node

- The Preferences node that emitted the event.
**Parameters:** key

- The key of the preference that was changed.
**Parameters:** newValue

- The new value of the preference, or

null

if the preference is being removed.

---

#### PreferenceChangeEvent

public PreferenceChangeEvent​(

Preferences

node,

String

key,

String

newValue)

Constructs a new

PreferenceChangeEvent

instance.

Method Detail

- getNode

```java
public
Preferences
getNode()
```

Returns the preference node that emitted the event.

**Returns:** The preference node that emitted the event.

- getKey

```java
public
String
getKey()
```

Returns the key of the preference that was changed.

**Returns:** The key of the preference that was changed.

- getNewValue

```java
public
String
getNewValue()
```

Returns the new value for the preference.

**Returns:** The new value for the preference, or

null

if the
preference was removed.

---

#### Method Detail

getNode

```java
public
Preferences
getNode()
```

Returns the preference node that emitted the event.

**Returns:** The preference node that emitted the event.

---

#### getNode

public

Preferences

getNode()

Returns the preference node that emitted the event.

getKey

```java
public
String
getKey()
```

Returns the key of the preference that was changed.

**Returns:** The key of the preference that was changed.

---

#### getKey

public

String

getKey()

Returns the key of the preference that was changed.

getNewValue

```java
public
String
getNewValue()
```

Returns the new value for the preference.

**Returns:** The new value for the preference, or

null

if the
preference was removed.

---

#### getNewValue

public

String

getNewValue()

Returns the new value for the preference.

---

