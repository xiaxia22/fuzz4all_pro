# Class FeatureDescriptor

**Source:** `java.desktop\java\beans\FeatureDescriptor.html`

### Class Description

```java
public class
FeatureDescriptor

extends
Object
```

The FeatureDescriptor class is the common baseclass for PropertyDescriptor,
EventSetDescriptor, and MethodDescriptor, etc.

It supports some common information that can be set and retrieved for
any of the introspection descriptors.

In addition it provides an extension mechanism so that arbitrary
attribute/value pairs can be associated with a design feature.

**Direct Known Subclasses:** BeanDescriptor

,

EventSetDescriptor

,

MethodDescriptor

,

ParameterDescriptor

,

PropertyDescriptor

---

### Field Details

*No entries found.*

### Constructor Details

#### public FeatureDescriptor()

Constructs a

FeatureDescriptor

.

---

### Method Details

#### public
String
getName()

Gets the programmatic name of this feature.

**Returns:**
- The programmatic name of the property/method/event

---

#### public void setName​(
String
name)

Sets the programmatic name of this feature.

**Parameters:**
- name

- The programmatic name of the property/method/event

---

#### public
String
getDisplayName()

Gets the localized display name of this feature.

**Returns:**
- The localized display name for the property/method/event.
This defaults to the same as its programmatic name from getName.

---

#### public void setDisplayName​(
String
displayName)

Sets the localized display name of this feature.

**Parameters:**
- displayName

- The localized display name for the
property/method/event.

---

#### public boolean isExpert()

The "expert" flag is used to distinguish between those features that are
intended for expert users from those that are intended for normal users.

**Returns:**
- True if this feature is intended for use by experts only.

---

#### public void setExpert​(boolean expert)

The "expert" flag is used to distinguish between features that are
intended for expert users from those that are intended for normal users.

**Parameters:**
- expert

- True if this feature is intended for use by experts only.

---

#### public boolean isHidden()

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

**Returns:**
- True if this feature should be hidden from human users.

---

#### public void setHidden​(boolean hidden)

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

**Parameters:**
- hidden

- True if this feature should be hidden from human users.

---

#### public boolean isPreferred()

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

**Returns:**
- True if this feature should be preferentially shown to human users.

**Since:**
- 1.2

---

#### public void setPreferred​(boolean preferred)

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

**Parameters:**
- preferred

- True if this feature should be preferentially shown
to human users.

**Since:**
- 1.2

---

#### public
String
getShortDescription()

Gets the short description of this feature.

**Returns:**
- A localized short description associated with this
property/method/event. This defaults to be the display name.

---

#### public void setShortDescription​(
String
text)

You can associate a short descriptive string with a feature. Normally
these descriptive strings should be less than about 40 characters.

**Parameters:**
- text

- A (localized) short description to be associated with
this property/method/event.

---

#### public void setValue​(
String
attributeName,

Object
value)

Associate a named attribute with this feature.

**Parameters:**
- attributeName

- The locale-independent name of the attribute
- value

- The value.

---

#### public
Object
getValue​(
String
attributeName)

Retrieve a named attribute with this feature.

**Parameters:**
- attributeName

- The locale-independent name of the attribute

**Returns:**
- The value of the attribute. May be null if
the attribute is unknown.

---

#### public
Enumeration
<
String
> attributeNames()

Gets an enumeration of the locale-independent names of this
feature.

**Returns:**
- An enumeration of the locale-independent names of any
attributes that have been registered with setValue.

---

#### public
String
toString()

Returns a string representation of the object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object

**Since:**
- 1.7

---

### Additional Sections

#### Class FeatureDescriptor

java.lang.Object

- java.beans.FeatureDescriptor

java.beans.FeatureDescriptor

**Direct Known Subclasses:** BeanDescriptor

,

EventSetDescriptor

,

MethodDescriptor

,

ParameterDescriptor

,

PropertyDescriptor

```java
public class
FeatureDescriptor

extends
Object
```

The FeatureDescriptor class is the common baseclass for PropertyDescriptor,
EventSetDescriptor, and MethodDescriptor, etc.

It supports some common information that can be set and retrieved for
any of the introspection descriptors.

In addition it provides an extension mechanism so that arbitrary
attribute/value pairs can be associated with a design feature.

**Since:** 1.1

public class

FeatureDescriptor

extends

Object

The FeatureDescriptor class is the common baseclass for PropertyDescriptor,
EventSetDescriptor, and MethodDescriptor, etc.

It supports some common information that can be set and retrieved for
any of the introspection descriptors.

In addition it provides an extension mechanism so that arbitrary
attribute/value pairs can be associated with a design feature.

It supports some common information that can be set and retrieved for
any of the introspection descriptors.

In addition it provides an extension mechanism so that arbitrary
attribute/value pairs can be associated with a design feature.

In addition it provides an extension mechanism so that arbitrary
attribute/value pairs can be associated with a design feature.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FeatureDescriptor

()

Constructs a

FeatureDescriptor

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Enumeration

<

String

>

attributeNames

()

Gets an enumeration of the locale-independent names of this
feature.

String

getDisplayName

()

Gets the localized display name of this feature.

String

getName

()

Gets the programmatic name of this feature.

String

getShortDescription

()

Gets the short description of this feature.

Object

getValue

​(

String

attributeName)

Retrieve a named attribute with this feature.

boolean

isExpert

()

The "expert" flag is used to distinguish between those features that are
intended for expert users from those that are intended for normal users.

boolean

isHidden

()

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

boolean

isPreferred

()

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

void

setDisplayName

​(

String

displayName)

Sets the localized display name of this feature.

void

setExpert

​(boolean expert)

The "expert" flag is used to distinguish between features that are
intended for expert users from those that are intended for normal users.

void

setHidden

​(boolean hidden)

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

void

setName

​(

String

name)

Sets the programmatic name of this feature.

void

setPreferred

​(boolean preferred)

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

void

setShortDescription

​(

String

text)

You can associate a short descriptive string with a feature.

void

setValue

​(

String

attributeName,

Object

value)

Associate a named attribute with this feature.

String

toString

()

Returns a string representation of the object.

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

FeatureDescriptor

()

Constructs a

FeatureDescriptor

.

---

#### Constructor Summary

Constructs a

FeatureDescriptor

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Enumeration

<

String

>

attributeNames

()

Gets an enumeration of the locale-independent names of this
feature.

String

getDisplayName

()

Gets the localized display name of this feature.

String

getName

()

Gets the programmatic name of this feature.

String

getShortDescription

()

Gets the short description of this feature.

Object

getValue

​(

String

attributeName)

Retrieve a named attribute with this feature.

boolean

isExpert

()

The "expert" flag is used to distinguish between those features that are
intended for expert users from those that are intended for normal users.

boolean

isHidden

()

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

boolean

isPreferred

()

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

void

setDisplayName

​(

String

displayName)

Sets the localized display name of this feature.

void

setExpert

​(boolean expert)

The "expert" flag is used to distinguish between features that are
intended for expert users from those that are intended for normal users.

void

setHidden

​(boolean hidden)

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

void

setName

​(

String

name)

Sets the programmatic name of this feature.

void

setPreferred

​(boolean preferred)

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

void

setShortDescription

​(

String

text)

You can associate a short descriptive string with a feature.

void

setValue

​(

String

attributeName,

Object

value)

Associate a named attribute with this feature.

String

toString

()

Returns a string representation of the object.

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

Gets an enumeration of the locale-independent names of this
feature.

Gets the localized display name of this feature.

Gets the programmatic name of this feature.

Gets the short description of this feature.

Retrieve a named attribute with this feature.

The "expert" flag is used to distinguish between those features that are
intended for expert users from those that are intended for normal users.

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

Sets the localized display name of this feature.

The "expert" flag is used to distinguish between features that are
intended for expert users from those that are intended for normal users.

Sets the programmatic name of this feature.

You can associate a short descriptive string with a feature.

Associate a named attribute with this feature.

Returns a string representation of the object.

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

- FeatureDescriptor

```java
public FeatureDescriptor()
```

Constructs a

FeatureDescriptor

.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Gets the programmatic name of this feature.

**Returns:** The programmatic name of the property/method/event

- setName

```java
public void setName​(
String
name)
```

Sets the programmatic name of this feature.

**Parameters:** name

- The programmatic name of the property/method/event

- getDisplayName

```java
public
String
getDisplayName()
```

Gets the localized display name of this feature.

**Returns:** The localized display name for the property/method/event.
This defaults to the same as its programmatic name from getName.

- setDisplayName

```java
public void setDisplayName​(
String
displayName)
```

Sets the localized display name of this feature.

**Parameters:** displayName

- The localized display name for the
property/method/event.

- isExpert

```java
public boolean isExpert()
```

The "expert" flag is used to distinguish between those features that are
intended for expert users from those that are intended for normal users.

**Returns:** True if this feature is intended for use by experts only.

- setExpert

```java
public void setExpert​(boolean expert)
```

The "expert" flag is used to distinguish between features that are
intended for expert users from those that are intended for normal users.

**Parameters:** expert

- True if this feature is intended for use by experts only.

- isHidden

```java
public boolean isHidden()
```

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

**Returns:** True if this feature should be hidden from human users.

- setHidden

```java
public void setHidden​(boolean hidden)
```

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

**Parameters:** hidden

- True if this feature should be hidden from human users.

- isPreferred

```java
public boolean isPreferred()
```

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

**Returns:** True if this feature should be preferentially shown to human users.
**Since:** 1.2

- setPreferred

```java
public void setPreferred​(boolean preferred)
```

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

**Parameters:** preferred

- True if this feature should be preferentially shown
to human users.
**Since:** 1.2

- getShortDescription

```java
public
String
getShortDescription()
```

Gets the short description of this feature.

**Returns:** A localized short description associated with this
property/method/event. This defaults to be the display name.

- setShortDescription

```java
public void setShortDescription​(
String
text)
```

You can associate a short descriptive string with a feature. Normally
these descriptive strings should be less than about 40 characters.

**Parameters:** text

- A (localized) short description to be associated with
this property/method/event.

- setValue

```java
public void setValue​(
String
attributeName,

Object
value)
```

Associate a named attribute with this feature.

**Parameters:** attributeName

- The locale-independent name of the attribute
**Parameters:** value

- The value.

- getValue

```java
public
Object
getValue​(
String
attributeName)
```

Retrieve a named attribute with this feature.

**Parameters:** attributeName

- The locale-independent name of the attribute
**Returns:** The value of the attribute. May be null if
the attribute is unknown.

- attributeNames

```java
public
Enumeration
<
String
> attributeNames()
```

Gets an enumeration of the locale-independent names of this
feature.

**Returns:** An enumeration of the locale-independent names of any
attributes that have been registered with setValue.

- toString

```java
public
String
toString()
```

Returns a string representation of the object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object
**Since:** 1.7

Constructor Detail

- FeatureDescriptor

```java
public FeatureDescriptor()
```

Constructs a

FeatureDescriptor

.

---

#### Constructor Detail

FeatureDescriptor

```java
public FeatureDescriptor()
```

Constructs a

FeatureDescriptor

.

---

#### FeatureDescriptor

public FeatureDescriptor()

Constructs a

FeatureDescriptor

.

Method Detail

- getName

```java
public
String
getName()
```

Gets the programmatic name of this feature.

**Returns:** The programmatic name of the property/method/event

- setName

```java
public void setName​(
String
name)
```

Sets the programmatic name of this feature.

**Parameters:** name

- The programmatic name of the property/method/event

- getDisplayName

```java
public
String
getDisplayName()
```

Gets the localized display name of this feature.

**Returns:** The localized display name for the property/method/event.
This defaults to the same as its programmatic name from getName.

- setDisplayName

```java
public void setDisplayName​(
String
displayName)
```

Sets the localized display name of this feature.

**Parameters:** displayName

- The localized display name for the
property/method/event.

- isExpert

```java
public boolean isExpert()
```

The "expert" flag is used to distinguish between those features that are
intended for expert users from those that are intended for normal users.

**Returns:** True if this feature is intended for use by experts only.

- setExpert

```java
public void setExpert​(boolean expert)
```

The "expert" flag is used to distinguish between features that are
intended for expert users from those that are intended for normal users.

**Parameters:** expert

- True if this feature is intended for use by experts only.

- isHidden

```java
public boolean isHidden()
```

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

**Returns:** True if this feature should be hidden from human users.

- setHidden

```java
public void setHidden​(boolean hidden)
```

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

**Parameters:** hidden

- True if this feature should be hidden from human users.

- isPreferred

```java
public boolean isPreferred()
```

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

**Returns:** True if this feature should be preferentially shown to human users.
**Since:** 1.2

- setPreferred

```java
public void setPreferred​(boolean preferred)
```

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

**Parameters:** preferred

- True if this feature should be preferentially shown
to human users.
**Since:** 1.2

- getShortDescription

```java
public
String
getShortDescription()
```

Gets the short description of this feature.

**Returns:** A localized short description associated with this
property/method/event. This defaults to be the display name.

- setShortDescription

```java
public void setShortDescription​(
String
text)
```

You can associate a short descriptive string with a feature. Normally
these descriptive strings should be less than about 40 characters.

**Parameters:** text

- A (localized) short description to be associated with
this property/method/event.

- setValue

```java
public void setValue​(
String
attributeName,

Object
value)
```

Associate a named attribute with this feature.

**Parameters:** attributeName

- The locale-independent name of the attribute
**Parameters:** value

- The value.

- getValue

```java
public
Object
getValue​(
String
attributeName)
```

Retrieve a named attribute with this feature.

**Parameters:** attributeName

- The locale-independent name of the attribute
**Returns:** The value of the attribute. May be null if
the attribute is unknown.

- attributeNames

```java
public
Enumeration
<
String
> attributeNames()
```

Gets an enumeration of the locale-independent names of this
feature.

**Returns:** An enumeration of the locale-independent names of any
attributes that have been registered with setValue.

- toString

```java
public
String
toString()
```

Returns a string representation of the object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object
**Since:** 1.7

---

#### Method Detail

getName

```java
public
String
getName()
```

Gets the programmatic name of this feature.

**Returns:** The programmatic name of the property/method/event

---

#### getName

public

String

getName()

Gets the programmatic name of this feature.

setName

```java
public void setName​(
String
name)
```

Sets the programmatic name of this feature.

**Parameters:** name

- The programmatic name of the property/method/event

---

#### setName

public void setName​(

String

name)

Sets the programmatic name of this feature.

getDisplayName

```java
public
String
getDisplayName()
```

Gets the localized display name of this feature.

**Returns:** The localized display name for the property/method/event.
This defaults to the same as its programmatic name from getName.

---

#### getDisplayName

public

String

getDisplayName()

Gets the localized display name of this feature.

setDisplayName

```java
public void setDisplayName​(
String
displayName)
```

Sets the localized display name of this feature.

**Parameters:** displayName

- The localized display name for the
property/method/event.

---

#### setDisplayName

public void setDisplayName​(

String

displayName)

Sets the localized display name of this feature.

isExpert

```java
public boolean isExpert()
```

The "expert" flag is used to distinguish between those features that are
intended for expert users from those that are intended for normal users.

**Returns:** True if this feature is intended for use by experts only.

---

#### isExpert

public boolean isExpert()

The "expert" flag is used to distinguish between those features that are
intended for expert users from those that are intended for normal users.

setExpert

```java
public void setExpert​(boolean expert)
```

The "expert" flag is used to distinguish between features that are
intended for expert users from those that are intended for normal users.

**Parameters:** expert

- True if this feature is intended for use by experts only.

---

#### setExpert

public void setExpert​(boolean expert)

The "expert" flag is used to distinguish between features that are
intended for expert users from those that are intended for normal users.

isHidden

```java
public boolean isHidden()
```

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

**Returns:** True if this feature should be hidden from human users.

---

#### isHidden

public boolean isHidden()

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

setHidden

```java
public void setHidden​(boolean hidden)
```

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

**Parameters:** hidden

- True if this feature should be hidden from human users.

---

#### setHidden

public void setHidden​(boolean hidden)

The "hidden" flag is used to identify features that are intended only
for tool use, and which should not be exposed to humans.

isPreferred

```java
public boolean isPreferred()
```

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

**Returns:** True if this feature should be preferentially shown to human users.
**Since:** 1.2

---

#### isPreferred

public boolean isPreferred()

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

setPreferred

```java
public void setPreferred​(boolean preferred)
```

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

**Parameters:** preferred

- True if this feature should be preferentially shown
to human users.
**Since:** 1.2

---

#### setPreferred

public void setPreferred​(boolean preferred)

The "preferred" flag is used to identify features that are particularly
important for presenting to humans.

getShortDescription

```java
public
String
getShortDescription()
```

Gets the short description of this feature.

**Returns:** A localized short description associated with this
property/method/event. This defaults to be the display name.

---

#### getShortDescription

public

String

getShortDescription()

Gets the short description of this feature.

setShortDescription

```java
public void setShortDescription​(
String
text)
```

You can associate a short descriptive string with a feature. Normally
these descriptive strings should be less than about 40 characters.

**Parameters:** text

- A (localized) short description to be associated with
this property/method/event.

---

#### setShortDescription

public void setShortDescription​(

String

text)

You can associate a short descriptive string with a feature. Normally
these descriptive strings should be less than about 40 characters.

setValue

```java
public void setValue​(
String
attributeName,

Object
value)
```

Associate a named attribute with this feature.

**Parameters:** attributeName

- The locale-independent name of the attribute
**Parameters:** value

- The value.

---

#### setValue

public void setValue​(

String

attributeName,

Object

value)

Associate a named attribute with this feature.

getValue

```java
public
Object
getValue​(
String
attributeName)
```

Retrieve a named attribute with this feature.

**Parameters:** attributeName

- The locale-independent name of the attribute
**Returns:** The value of the attribute. May be null if
the attribute is unknown.

---

#### getValue

public

Object

getValue​(

String

attributeName)

Retrieve a named attribute with this feature.

attributeNames

```java
public
Enumeration
<
String
> attributeNames()
```

Gets an enumeration of the locale-independent names of this
feature.

**Returns:** An enumeration of the locale-independent names of any
attributes that have been registered with setValue.

---

#### attributeNames

public

Enumeration

<

String

> attributeNames()

Gets an enumeration of the locale-independent names of this
feature.

toString

```java
public
String
toString()
```

Returns a string representation of the object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object
**Since:** 1.7

---

#### toString

public

String

toString()

Returns a string representation of the object.

---

