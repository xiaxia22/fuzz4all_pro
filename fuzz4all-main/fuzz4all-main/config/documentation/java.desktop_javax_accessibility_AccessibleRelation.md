# Class AccessibleRelation

**Source:** `java.desktop\javax\accessibility\AccessibleRelation.html`

### Class Description

```java
public class
AccessibleRelation

extends
AccessibleBundle
```

Class

AccessibleRelation

describes a relation between the object that
implements the

AccessibleRelation

and one or more other objects. The
actual relations that an object has with other objects are defined as an

AccessibleRelationSet

, which is a composed set of

AccessibleRelations

.

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. If the constants in this class are not sufficient to describe
the role of an object, a subclass should be generated from this class and it
should provide constants in a similar manner.

**Since:** 1.3

---

### Field Details

#### public static final
String
LABEL_FOR

Indicates an object is a label for one or more target objects.

**See Also:**
- getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABELED_BY

,

MEMBER_OF

---

#### public static final
String
LABELED_BY

Indicates an object is labeled by one or more target objects.

**See Also:**
- getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

MEMBER_OF

---

#### public static final
String
MEMBER_OF

Indicates an object is a member of a group of one or more target objects.

**See Also:**
- getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

---

#### public static final
String
CONTROLLER_FOR

Indicates an object is a controller for one or more target objects.

**See Also:**
- getTarget()

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

---

#### public static final
String
CONTROLLED_BY

Indicates an object is controlled by one or more target objects.

**See Also:**
- getTarget()

,

CONTROLLER_FOR

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

---

#### public static final
String
FLOWS_TO

Indicates an object is logically contiguous with a second object where
the second object occurs after the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the first
element "flows to" the second element.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
FLOWS_FROM

Indicates an object is logically contiguous with a second object where
the second object occurs before the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the
second element "flows from" the second element.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
SUBWINDOW_OF

Indicates that an object is a subwindow of one or more objects.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
PARENT_WINDOW_OF

Indicates that an object is a parent window of one or more objects.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
EMBEDS

Indicates that an object has one or more objects embedded in it.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
EMBEDDED_BY

Indicates that an object is embedded in one or more objects.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
CHILD_NODE_OF

Indicates that an object is a child node of one or more objects.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
LABEL_FOR_PROPERTY

Identifies that the target group for a label has changed.

**See Also:**
- Constant Field Values

---

#### public static final
String
LABELED_BY_PROPERTY

Identifies that the objects that are doing the labeling have changed.

**See Also:**
- Constant Field Values

---

#### public static final
String
MEMBER_OF_PROPERTY

Identifies that group membership has changed.

**See Also:**
- Constant Field Values

---

#### public static final
String
CONTROLLER_FOR_PROPERTY

Identifies that the controller for the target object has changed.

**See Also:**
- Constant Field Values

---

#### public static final
String
CONTROLLED_BY_PROPERTY

Identifies that the target object that is doing the controlling has
changed.

**See Also:**
- Constant Field Values

---

#### public static final
String
FLOWS_TO_PROPERTY

Indicates the

FLOWS_TO

relation between two objects has changed.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
FLOWS_FROM_PROPERTY

Indicates the

FLOWS_FROM

relation between two objects has
changed.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
SUBWINDOW_OF_PROPERTY

Indicates the

SUBWINDOW_OF

relation between two or more objects
has changed.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
PARENT_WINDOW_OF_PROPERTY

Indicates the

PARENT_WINDOW_OF

relation between two or more
objects has changed.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
EMBEDS_PROPERTY

Indicates the

EMBEDS

relation between two or more objects has
changed.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
EMBEDDED_BY_PROPERTY

Indicates the

EMBEDDED_BY

relation between two or more objects
has changed.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
CHILD_NODE_OF_PROPERTY

Indicates the

CHILD_NODE_OF

relation between two or more objects
has changed.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

### Constructor Details

#### public AccessibleRelation​(
String
key)

Create a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:**
- key

- the locale independent name of the relation

**See Also:**
- AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### public AccessibleRelation​(
String
key,

Object
target)

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:**
- key

- the locale independent name of the relation
- target

- the target object for this relation

**See Also:**
- AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### public AccessibleRelation​(
String
key,

Object
[] target)

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:**
- key

- the locale independent name of the relation
- target

- the target object(s) for this relation

**See Also:**
- AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

### Method Details

#### public
String
getKey()

Returns the key for this relation.

**Returns:**
- the key for this relation

**See Also:**
- CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

---

#### public
Object
[] getTarget()

Returns the target objects for this relation.

**Returns:**
- an array containing the target objects for this relation

---

#### public void setTarget​(
Object
target)

Sets the target object for this relation.

**Parameters:**
- target

- the target object for this relation

---

#### public void setTarget​(
Object
[] target)

Sets the target objects for this relation.

**Parameters:**
- target

- an array containing the target objects for this relation

---

### Additional Sections

#### Class AccessibleRelation

java.lang.Object

- javax.accessibility.AccessibleBundle
- - javax.accessibility.AccessibleRelation

javax.accessibility.AccessibleBundle

- javax.accessibility.AccessibleRelation

javax.accessibility.AccessibleRelation

```java
public class
AccessibleRelation

extends
AccessibleBundle
```

Class

AccessibleRelation

describes a relation between the object that
implements the

AccessibleRelation

and one or more other objects. The
actual relations that an object has with other objects are defined as an

AccessibleRelationSet

, which is a composed set of

AccessibleRelations

.

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. If the constants in this class are not sufficient to describe
the role of an object, a subclass should be generated from this class and it
should provide constants in a similar manner.

**Since:** 1.3

public class

AccessibleRelation

extends

AccessibleBundle

Class

AccessibleRelation

describes a relation between the object that
implements the

AccessibleRelation

and one or more other objects. The
actual relations that an object has with other objects are defined as an

AccessibleRelationSet

, which is a composed set of

AccessibleRelations

.

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. If the constants in this class are not sufficient to describe
the role of an object, a subclass should be generated from this class and it
should provide constants in a similar manner.

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. If the constants in this class are not sufficient to describe
the role of an object, a subclass should be generated from this class and it
should provide constants in a similar manner.

The constants in this class present a strongly typed enumeration of common
object roles. If the constants in this class are not sufficient to describe
the role of an object, a subclass should be generated from this class and it
should provide constants in a similar manner.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

CHILD_NODE_OF

Indicates that an object is a child node of one or more objects.

static

String

CHILD_NODE_OF_PROPERTY

Indicates the

CHILD_NODE_OF

relation between two or more objects
has changed.

static

String

CONTROLLED_BY

Indicates an object is controlled by one or more target objects.

static

String

CONTROLLED_BY_PROPERTY

Identifies that the target object that is doing the controlling has
changed.

static

String

CONTROLLER_FOR

Indicates an object is a controller for one or more target objects.

static

String

CONTROLLER_FOR_PROPERTY

Identifies that the controller for the target object has changed.

static

String

EMBEDDED_BY

Indicates that an object is embedded in one or more objects.

static

String

EMBEDDED_BY_PROPERTY

Indicates the

EMBEDDED_BY

relation between two or more objects
has changed.

static

String

EMBEDS

Indicates that an object has one or more objects embedded in it.

static

String

EMBEDS_PROPERTY

Indicates the

EMBEDS

relation between two or more objects has
changed.

static

String

FLOWS_FROM

Indicates an object is logically contiguous with a second object where
the second object occurs before the object.

static

String

FLOWS_FROM_PROPERTY

Indicates the

FLOWS_FROM

relation between two objects has
changed.

static

String

FLOWS_TO

Indicates an object is logically contiguous with a second object where
the second object occurs after the object.

static

String

FLOWS_TO_PROPERTY

Indicates the

FLOWS_TO

relation between two objects has changed.

static

String

LABEL_FOR

Indicates an object is a label for one or more target objects.

static

String

LABEL_FOR_PROPERTY

Identifies that the target group for a label has changed.

static

String

LABELED_BY

Indicates an object is labeled by one or more target objects.

static

String

LABELED_BY_PROPERTY

Identifies that the objects that are doing the labeling have changed.

static

String

MEMBER_OF

Indicates an object is a member of a group of one or more target objects.

static

String

MEMBER_OF_PROPERTY

Identifies that group membership has changed.

static

String

PARENT_WINDOW_OF

Indicates that an object is a parent window of one or more objects.

static

String

PARENT_WINDOW_OF_PROPERTY

Indicates the

PARENT_WINDOW_OF

relation between two or more
objects has changed.

static

String

SUBWINDOW_OF

Indicates that an object is a subwindow of one or more objects.

static

String

SUBWINDOW_OF_PROPERTY

Indicates the

SUBWINDOW_OF

relation between two or more objects
has changed.

- Fields declared in class javax.accessibility.

AccessibleBundle

key

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessibleRelation

​(

String

key)

Create a new

AccessibleRelation

using the given locale
independent key.

AccessibleRelation

​(

String

key,

Object

target)

Creates a new

AccessibleRelation

using the given locale
independent key.

AccessibleRelation

​(

String

key,

Object

[] target)

Creates a new

AccessibleRelation

using the given locale
independent key.

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

Returns the key for this relation.

Object

[]

getTarget

()

Returns the target objects for this relation.

void

setTarget

​(

Object

target)

Sets the target object for this relation.

void

setTarget

​(

Object

[] target)

Sets the target objects for this relation.

- Methods declared in class javax.accessibility.

AccessibleBundle

toDisplayString

,

toDisplayString

,

toDisplayString

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

Fields

Modifier and Type

Field

Description

static

String

CHILD_NODE_OF

Indicates that an object is a child node of one or more objects.

static

String

CHILD_NODE_OF_PROPERTY

Indicates the

CHILD_NODE_OF

relation between two or more objects
has changed.

static

String

CONTROLLED_BY

Indicates an object is controlled by one or more target objects.

static

String

CONTROLLED_BY_PROPERTY

Identifies that the target object that is doing the controlling has
changed.

static

String

CONTROLLER_FOR

Indicates an object is a controller for one or more target objects.

static

String

CONTROLLER_FOR_PROPERTY

Identifies that the controller for the target object has changed.

static

String

EMBEDDED_BY

Indicates that an object is embedded in one or more objects.

static

String

EMBEDDED_BY_PROPERTY

Indicates the

EMBEDDED_BY

relation between two or more objects
has changed.

static

String

EMBEDS

Indicates that an object has one or more objects embedded in it.

static

String

EMBEDS_PROPERTY

Indicates the

EMBEDS

relation between two or more objects has
changed.

static

String

FLOWS_FROM

Indicates an object is logically contiguous with a second object where
the second object occurs before the object.

static

String

FLOWS_FROM_PROPERTY

Indicates the

FLOWS_FROM

relation between two objects has
changed.

static

String

FLOWS_TO

Indicates an object is logically contiguous with a second object where
the second object occurs after the object.

static

String

FLOWS_TO_PROPERTY

Indicates the

FLOWS_TO

relation between two objects has changed.

static

String

LABEL_FOR

Indicates an object is a label for one or more target objects.

static

String

LABEL_FOR_PROPERTY

Identifies that the target group for a label has changed.

static

String

LABELED_BY

Indicates an object is labeled by one or more target objects.

static

String

LABELED_BY_PROPERTY

Identifies that the objects that are doing the labeling have changed.

static

String

MEMBER_OF

Indicates an object is a member of a group of one or more target objects.

static

String

MEMBER_OF_PROPERTY

Identifies that group membership has changed.

static

String

PARENT_WINDOW_OF

Indicates that an object is a parent window of one or more objects.

static

String

PARENT_WINDOW_OF_PROPERTY

Indicates the

PARENT_WINDOW_OF

relation between two or more
objects has changed.

static

String

SUBWINDOW_OF

Indicates that an object is a subwindow of one or more objects.

static

String

SUBWINDOW_OF_PROPERTY

Indicates the

SUBWINDOW_OF

relation between two or more objects
has changed.

- Fields declared in class javax.accessibility.

AccessibleBundle

key

---

#### Field Summary

Indicates that an object is a child node of one or more objects.

Indicates the

CHILD_NODE_OF

relation between two or more objects
has changed.

Indicates an object is controlled by one or more target objects.

Identifies that the target object that is doing the controlling has
changed.

Indicates an object is a controller for one or more target objects.

Identifies that the controller for the target object has changed.

Indicates that an object is embedded in one or more objects.

Indicates the

EMBEDDED_BY

relation between two or more objects
has changed.

Indicates that an object has one or more objects embedded in it.

Indicates the

EMBEDS

relation between two or more objects has
changed.

Indicates an object is logically contiguous with a second object where
the second object occurs before the object.

Indicates the

FLOWS_FROM

relation between two objects has
changed.

Indicates an object is logically contiguous with a second object where
the second object occurs after the object.

Indicates the

FLOWS_TO

relation between two objects has changed.

Indicates an object is a label for one or more target objects.

Identifies that the target group for a label has changed.

Indicates an object is labeled by one or more target objects.

Identifies that the objects that are doing the labeling have changed.

Indicates an object is a member of a group of one or more target objects.

Identifies that group membership has changed.

Indicates that an object is a parent window of one or more objects.

Indicates the

PARENT_WINDOW_OF

relation between two or more
objects has changed.

Indicates that an object is a subwindow of one or more objects.

Indicates the

SUBWINDOW_OF

relation between two or more objects
has changed.

Fields declared in class javax.accessibility.

AccessibleBundle

key

---

#### Fields declared in class javax.accessibility. AccessibleBundle

Constructor Summary

Constructors

Constructor

Description

AccessibleRelation

​(

String

key)

Create a new

AccessibleRelation

using the given locale
independent key.

AccessibleRelation

​(

String

key,

Object

target)

Creates a new

AccessibleRelation

using the given locale
independent key.

AccessibleRelation

​(

String

key,

Object

[] target)

Creates a new

AccessibleRelation

using the given locale
independent key.

---

#### Constructor Summary

Create a new

AccessibleRelation

using the given locale
independent key.

Creates a new

AccessibleRelation

using the given locale
independent key.

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

Returns the key for this relation.

Object

[]

getTarget

()

Returns the target objects for this relation.

void

setTarget

​(

Object

target)

Sets the target object for this relation.

void

setTarget

​(

Object

[] target)

Sets the target objects for this relation.

- Methods declared in class javax.accessibility.

AccessibleBundle

toDisplayString

,

toDisplayString

,

toDisplayString

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

Returns the key for this relation.

Returns the target objects for this relation.

Sets the target object for this relation.

Sets the target objects for this relation.

Methods declared in class javax.accessibility.

AccessibleBundle

toDisplayString

,

toDisplayString

,

toDisplayString

,

toString

---

#### Methods declared in class javax.accessibility. AccessibleBundle

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

============ FIELD DETAIL ===========

- Field Detail

- LABEL_FOR

```java
public static final
String
LABEL_FOR
```

Indicates an object is a label for one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABELED_BY

,

MEMBER_OF

- LABELED_BY

```java
public static final
String
LABELED_BY
```

Indicates an object is labeled by one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

MEMBER_OF

- MEMBER_OF

```java
public static final
String
MEMBER_OF
```

Indicates an object is a member of a group of one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

- CONTROLLER_FOR

```java
public static final
String
CONTROLLER_FOR
```

Indicates an object is a controller for one or more target objects.

**See Also:** getTarget()

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

- CONTROLLED_BY

```java
public static final
String
CONTROLLED_BY
```

Indicates an object is controlled by one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

- FLOWS_TO

```java
public static final
String
FLOWS_TO
```

Indicates an object is logically contiguous with a second object where
the second object occurs after the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the first
element "flows to" the second element.

**Since:** 1.5
**See Also:** Constant Field Values

- FLOWS_FROM

```java
public static final
String
FLOWS_FROM
```

Indicates an object is logically contiguous with a second object where
the second object occurs before the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the
second element "flows from" the second element.

**Since:** 1.5
**See Also:** Constant Field Values

- SUBWINDOW_OF

```java
public static final
String
SUBWINDOW_OF
```

Indicates that an object is a subwindow of one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

- PARENT_WINDOW_OF

```java
public static final
String
PARENT_WINDOW_OF
```

Indicates that an object is a parent window of one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

- EMBEDS

```java
public static final
String
EMBEDS
```

Indicates that an object has one or more objects embedded in it.

**Since:** 1.5
**See Also:** Constant Field Values

- EMBEDDED_BY

```java
public static final
String
EMBEDDED_BY
```

Indicates that an object is embedded in one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

- CHILD_NODE_OF

```java
public static final
String
CHILD_NODE_OF
```

Indicates that an object is a child node of one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

- LABEL_FOR_PROPERTY

```java
public static final
String
LABEL_FOR_PROPERTY
```

Identifies that the target group for a label has changed.

**See Also:** Constant Field Values

- LABELED_BY_PROPERTY

```java
public static final
String
LABELED_BY_PROPERTY
```

Identifies that the objects that are doing the labeling have changed.

**See Also:** Constant Field Values

- MEMBER_OF_PROPERTY

```java
public static final
String
MEMBER_OF_PROPERTY
```

Identifies that group membership has changed.

**See Also:** Constant Field Values

- CONTROLLER_FOR_PROPERTY

```java
public static final
String
CONTROLLER_FOR_PROPERTY
```

Identifies that the controller for the target object has changed.

**See Also:** Constant Field Values

- CONTROLLED_BY_PROPERTY

```java
public static final
String
CONTROLLED_BY_PROPERTY
```

Identifies that the target object that is doing the controlling has
changed.

**See Also:** Constant Field Values

- FLOWS_TO_PROPERTY

```java
public static final
String
FLOWS_TO_PROPERTY
```

Indicates the

FLOWS_TO

relation between two objects has changed.

**Since:** 1.5
**See Also:** Constant Field Values

- FLOWS_FROM_PROPERTY

```java
public static final
String
FLOWS_FROM_PROPERTY
```

Indicates the

FLOWS_FROM

relation between two objects has
changed.

**Since:** 1.5
**See Also:** Constant Field Values

- SUBWINDOW_OF_PROPERTY

```java
public static final
String
SUBWINDOW_OF_PROPERTY
```

Indicates the

SUBWINDOW_OF

relation between two or more objects
has changed.

**Since:** 1.5
**See Also:** Constant Field Values

- PARENT_WINDOW_OF_PROPERTY

```java
public static final
String
PARENT_WINDOW_OF_PROPERTY
```

Indicates the

PARENT_WINDOW_OF

relation between two or more
objects has changed.

**Since:** 1.5
**See Also:** Constant Field Values

- EMBEDS_PROPERTY

```java
public static final
String
EMBEDS_PROPERTY
```

Indicates the

EMBEDS

relation between two or more objects has
changed.

**Since:** 1.5
**See Also:** Constant Field Values

- EMBEDDED_BY_PROPERTY

```java
public static final
String
EMBEDDED_BY_PROPERTY
```

Indicates the

EMBEDDED_BY

relation between two or more objects
has changed.

**Since:** 1.5
**See Also:** Constant Field Values

- CHILD_NODE_OF_PROPERTY

```java
public static final
String
CHILD_NODE_OF_PROPERTY
```

Indicates the

CHILD_NODE_OF

relation between two or more objects
has changed.

**Since:** 1.5
**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibleRelation

```java
public AccessibleRelation​(
String
key)
```

Create a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the relation
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

- AccessibleRelation

```java
public AccessibleRelation​(
String
key,

Object
target)
```

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the relation
**Parameters:** target

- the target object for this relation
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

- AccessibleRelation

```java
public AccessibleRelation​(
String
key,

Object
[] target)
```

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the relation
**Parameters:** target

- the target object(s) for this relation
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

============ METHOD DETAIL ==========

- Method Detail

- getKey

```java
public
String
getKey()
```

Returns the key for this relation.

**Returns:** the key for this relation
**See Also:** CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

- getTarget

```java
public
Object
[] getTarget()
```

Returns the target objects for this relation.

**Returns:** an array containing the target objects for this relation

- setTarget

```java
public void setTarget​(
Object
target)
```

Sets the target object for this relation.

**Parameters:** target

- the target object for this relation

- setTarget

```java
public void setTarget​(
Object
[] target)
```

Sets the target objects for this relation.

**Parameters:** target

- an array containing the target objects for this relation

Field Detail

- LABEL_FOR

```java
public static final
String
LABEL_FOR
```

Indicates an object is a label for one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABELED_BY

,

MEMBER_OF

- LABELED_BY

```java
public static final
String
LABELED_BY
```

Indicates an object is labeled by one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

MEMBER_OF

- MEMBER_OF

```java
public static final
String
MEMBER_OF
```

Indicates an object is a member of a group of one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

- CONTROLLER_FOR

```java
public static final
String
CONTROLLER_FOR
```

Indicates an object is a controller for one or more target objects.

**See Also:** getTarget()

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

- CONTROLLED_BY

```java
public static final
String
CONTROLLED_BY
```

Indicates an object is controlled by one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

- FLOWS_TO

```java
public static final
String
FLOWS_TO
```

Indicates an object is logically contiguous with a second object where
the second object occurs after the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the first
element "flows to" the second element.

**Since:** 1.5
**See Also:** Constant Field Values

- FLOWS_FROM

```java
public static final
String
FLOWS_FROM
```

Indicates an object is logically contiguous with a second object where
the second object occurs before the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the
second element "flows from" the second element.

**Since:** 1.5
**See Also:** Constant Field Values

- SUBWINDOW_OF

```java
public static final
String
SUBWINDOW_OF
```

Indicates that an object is a subwindow of one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

- PARENT_WINDOW_OF

```java
public static final
String
PARENT_WINDOW_OF
```

Indicates that an object is a parent window of one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

- EMBEDS

```java
public static final
String
EMBEDS
```

Indicates that an object has one or more objects embedded in it.

**Since:** 1.5
**See Also:** Constant Field Values

- EMBEDDED_BY

```java
public static final
String
EMBEDDED_BY
```

Indicates that an object is embedded in one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

- CHILD_NODE_OF

```java
public static final
String
CHILD_NODE_OF
```

Indicates that an object is a child node of one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

- LABEL_FOR_PROPERTY

```java
public static final
String
LABEL_FOR_PROPERTY
```

Identifies that the target group for a label has changed.

**See Also:** Constant Field Values

- LABELED_BY_PROPERTY

```java
public static final
String
LABELED_BY_PROPERTY
```

Identifies that the objects that are doing the labeling have changed.

**See Also:** Constant Field Values

- MEMBER_OF_PROPERTY

```java
public static final
String
MEMBER_OF_PROPERTY
```

Identifies that group membership has changed.

**See Also:** Constant Field Values

- CONTROLLER_FOR_PROPERTY

```java
public static final
String
CONTROLLER_FOR_PROPERTY
```

Identifies that the controller for the target object has changed.

**See Also:** Constant Field Values

- CONTROLLED_BY_PROPERTY

```java
public static final
String
CONTROLLED_BY_PROPERTY
```

Identifies that the target object that is doing the controlling has
changed.

**See Also:** Constant Field Values

- FLOWS_TO_PROPERTY

```java
public static final
String
FLOWS_TO_PROPERTY
```

Indicates the

FLOWS_TO

relation between two objects has changed.

**Since:** 1.5
**See Also:** Constant Field Values

- FLOWS_FROM_PROPERTY

```java
public static final
String
FLOWS_FROM_PROPERTY
```

Indicates the

FLOWS_FROM

relation between two objects has
changed.

**Since:** 1.5
**See Also:** Constant Field Values

- SUBWINDOW_OF_PROPERTY

```java
public static final
String
SUBWINDOW_OF_PROPERTY
```

Indicates the

SUBWINDOW_OF

relation between two or more objects
has changed.

**Since:** 1.5
**See Also:** Constant Field Values

- PARENT_WINDOW_OF_PROPERTY

```java
public static final
String
PARENT_WINDOW_OF_PROPERTY
```

Indicates the

PARENT_WINDOW_OF

relation between two or more
objects has changed.

**Since:** 1.5
**See Also:** Constant Field Values

- EMBEDS_PROPERTY

```java
public static final
String
EMBEDS_PROPERTY
```

Indicates the

EMBEDS

relation between two or more objects has
changed.

**Since:** 1.5
**See Also:** Constant Field Values

- EMBEDDED_BY_PROPERTY

```java
public static final
String
EMBEDDED_BY_PROPERTY
```

Indicates the

EMBEDDED_BY

relation between two or more objects
has changed.

**Since:** 1.5
**See Also:** Constant Field Values

- CHILD_NODE_OF_PROPERTY

```java
public static final
String
CHILD_NODE_OF_PROPERTY
```

Indicates the

CHILD_NODE_OF

relation between two or more objects
has changed.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### Field Detail

LABEL_FOR

```java
public static final
String
LABEL_FOR
```

Indicates an object is a label for one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABELED_BY

,

MEMBER_OF

---

#### LABEL_FOR

public static final

String

LABEL_FOR

Indicates an object is a label for one or more target objects.

LABELED_BY

```java
public static final
String
LABELED_BY
```

Indicates an object is labeled by one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

MEMBER_OF

---

#### LABELED_BY

public static final

String

LABELED_BY

Indicates an object is labeled by one or more target objects.

MEMBER_OF

```java
public static final
String
MEMBER_OF
```

Indicates an object is a member of a group of one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

---

#### MEMBER_OF

public static final

String

MEMBER_OF

Indicates an object is a member of a group of one or more target objects.

CONTROLLER_FOR

```java
public static final
String
CONTROLLER_FOR
```

Indicates an object is a controller for one or more target objects.

**See Also:** getTarget()

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

---

#### CONTROLLER_FOR

public static final

String

CONTROLLER_FOR

Indicates an object is a controller for one or more target objects.

CONTROLLED_BY

```java
public static final
String
CONTROLLED_BY
```

Indicates an object is controlled by one or more target objects.

**See Also:** getTarget()

,

CONTROLLER_FOR

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

---

#### CONTROLLED_BY

public static final

String

CONTROLLED_BY

Indicates an object is controlled by one or more target objects.

FLOWS_TO

```java
public static final
String
FLOWS_TO
```

Indicates an object is logically contiguous with a second object where
the second object occurs after the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the first
element "flows to" the second element.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### FLOWS_TO

public static final

String

FLOWS_TO

Indicates an object is logically contiguous with a second object where
the second object occurs after the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the first
element "flows to" the second element.

FLOWS_FROM

```java
public static final
String
FLOWS_FROM
```

Indicates an object is logically contiguous with a second object where
the second object occurs before the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the
second element "flows from" the second element.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### FLOWS_FROM

public static final

String

FLOWS_FROM

Indicates an object is logically contiguous with a second object where
the second object occurs before the object. An example is a paragraph of
text that runs to the end of a page and continues on the next page with
an intervening text footer and/or text header. The two parts of the
paragraph are separate text elements but are related in that the second
element is a continuation of the first element. In other words, the
second element "flows from" the second element.

SUBWINDOW_OF

```java
public static final
String
SUBWINDOW_OF
```

Indicates that an object is a subwindow of one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### SUBWINDOW_OF

public static final

String

SUBWINDOW_OF

Indicates that an object is a subwindow of one or more objects.

PARENT_WINDOW_OF

```java
public static final
String
PARENT_WINDOW_OF
```

Indicates that an object is a parent window of one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### PARENT_WINDOW_OF

public static final

String

PARENT_WINDOW_OF

Indicates that an object is a parent window of one or more objects.

EMBEDS

```java
public static final
String
EMBEDS
```

Indicates that an object has one or more objects embedded in it.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### EMBEDS

public static final

String

EMBEDS

Indicates that an object has one or more objects embedded in it.

EMBEDDED_BY

```java
public static final
String
EMBEDDED_BY
```

Indicates that an object is embedded in one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### EMBEDDED_BY

public static final

String

EMBEDDED_BY

Indicates that an object is embedded in one or more objects.

CHILD_NODE_OF

```java
public static final
String
CHILD_NODE_OF
```

Indicates that an object is a child node of one or more objects.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### CHILD_NODE_OF

public static final

String

CHILD_NODE_OF

Indicates that an object is a child node of one or more objects.

LABEL_FOR_PROPERTY

```java
public static final
String
LABEL_FOR_PROPERTY
```

Identifies that the target group for a label has changed.

**See Also:** Constant Field Values

---

#### LABEL_FOR_PROPERTY

public static final

String

LABEL_FOR_PROPERTY

Identifies that the target group for a label has changed.

LABELED_BY_PROPERTY

```java
public static final
String
LABELED_BY_PROPERTY
```

Identifies that the objects that are doing the labeling have changed.

**See Also:** Constant Field Values

---

#### LABELED_BY_PROPERTY

public static final

String

LABELED_BY_PROPERTY

Identifies that the objects that are doing the labeling have changed.

MEMBER_OF_PROPERTY

```java
public static final
String
MEMBER_OF_PROPERTY
```

Identifies that group membership has changed.

**See Also:** Constant Field Values

---

#### MEMBER_OF_PROPERTY

public static final

String

MEMBER_OF_PROPERTY

Identifies that group membership has changed.

CONTROLLER_FOR_PROPERTY

```java
public static final
String
CONTROLLER_FOR_PROPERTY
```

Identifies that the controller for the target object has changed.

**See Also:** Constant Field Values

---

#### CONTROLLER_FOR_PROPERTY

public static final

String

CONTROLLER_FOR_PROPERTY

Identifies that the controller for the target object has changed.

CONTROLLED_BY_PROPERTY

```java
public static final
String
CONTROLLED_BY_PROPERTY
```

Identifies that the target object that is doing the controlling has
changed.

**See Also:** Constant Field Values

---

#### CONTROLLED_BY_PROPERTY

public static final

String

CONTROLLED_BY_PROPERTY

Identifies that the target object that is doing the controlling has
changed.

FLOWS_TO_PROPERTY

```java
public static final
String
FLOWS_TO_PROPERTY
```

Indicates the

FLOWS_TO

relation between two objects has changed.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### FLOWS_TO_PROPERTY

public static final

String

FLOWS_TO_PROPERTY

Indicates the

FLOWS_TO

relation between two objects has changed.

FLOWS_FROM_PROPERTY

```java
public static final
String
FLOWS_FROM_PROPERTY
```

Indicates the

FLOWS_FROM

relation between two objects has
changed.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### FLOWS_FROM_PROPERTY

public static final

String

FLOWS_FROM_PROPERTY

Indicates the

FLOWS_FROM

relation between two objects has
changed.

SUBWINDOW_OF_PROPERTY

```java
public static final
String
SUBWINDOW_OF_PROPERTY
```

Indicates the

SUBWINDOW_OF

relation between two or more objects
has changed.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### SUBWINDOW_OF_PROPERTY

public static final

String

SUBWINDOW_OF_PROPERTY

Indicates the

SUBWINDOW_OF

relation between two or more objects
has changed.

PARENT_WINDOW_OF_PROPERTY

```java
public static final
String
PARENT_WINDOW_OF_PROPERTY
```

Indicates the

PARENT_WINDOW_OF

relation between two or more
objects has changed.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### PARENT_WINDOW_OF_PROPERTY

public static final

String

PARENT_WINDOW_OF_PROPERTY

Indicates the

PARENT_WINDOW_OF

relation between two or more
objects has changed.

EMBEDS_PROPERTY

```java
public static final
String
EMBEDS_PROPERTY
```

Indicates the

EMBEDS

relation between two or more objects has
changed.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### EMBEDS_PROPERTY

public static final

String

EMBEDS_PROPERTY

Indicates the

EMBEDS

relation between two or more objects has
changed.

EMBEDDED_BY_PROPERTY

```java
public static final
String
EMBEDDED_BY_PROPERTY
```

Indicates the

EMBEDDED_BY

relation between two or more objects
has changed.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### EMBEDDED_BY_PROPERTY

public static final

String

EMBEDDED_BY_PROPERTY

Indicates the

EMBEDDED_BY

relation between two or more objects
has changed.

CHILD_NODE_OF_PROPERTY

```java
public static final
String
CHILD_NODE_OF_PROPERTY
```

Indicates the

CHILD_NODE_OF

relation between two or more objects
has changed.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### CHILD_NODE_OF_PROPERTY

public static final

String

CHILD_NODE_OF_PROPERTY

Indicates the

CHILD_NODE_OF

relation between two or more objects
has changed.

Constructor Detail

- AccessibleRelation

```java
public AccessibleRelation​(
String
key)
```

Create a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the relation
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

- AccessibleRelation

```java
public AccessibleRelation​(
String
key,

Object
target)
```

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the relation
**Parameters:** target

- the target object for this relation
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

- AccessibleRelation

```java
public AccessibleRelation​(
String
key,

Object
[] target)
```

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the relation
**Parameters:** target

- the target object(s) for this relation
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### Constructor Detail

AccessibleRelation

```java
public AccessibleRelation​(
String
key)
```

Create a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the relation
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### AccessibleRelation

public AccessibleRelation​(

String

key)

Create a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

AccessibleRelation

```java
public AccessibleRelation​(
String
key,

Object
target)
```

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the relation
**Parameters:** target

- the target object for this relation
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### AccessibleRelation

public AccessibleRelation​(

String

key,

Object

target)

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

AccessibleRelation

```java
public AccessibleRelation​(
String
key,

Object
[] target)
```

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the relation
**Parameters:** target

- the target object(s) for this relation
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### AccessibleRelation

public AccessibleRelation​(

String

key,

Object

[] target)

Creates a new

AccessibleRelation

using the given locale
independent key. The key

String

should be a locale independent
key for the relation. It is not intended to be used as the actual

String

to display to the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

Method Detail

- getKey

```java
public
String
getKey()
```

Returns the key for this relation.

**Returns:** the key for this relation
**See Also:** CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

- getTarget

```java
public
Object
[] getTarget()
```

Returns the target objects for this relation.

**Returns:** an array containing the target objects for this relation

- setTarget

```java
public void setTarget​(
Object
target)
```

Sets the target object for this relation.

**Parameters:** target

- the target object for this relation

- setTarget

```java
public void setTarget​(
Object
[] target)
```

Sets the target objects for this relation.

**Parameters:** target

- an array containing the target objects for this relation

---

#### Method Detail

getKey

```java
public
String
getKey()
```

Returns the key for this relation.

**Returns:** the key for this relation
**See Also:** CONTROLLER_FOR

,

CONTROLLED_BY

,

LABEL_FOR

,

LABELED_BY

,

MEMBER_OF

---

#### getKey

public

String

getKey()

Returns the key for this relation.

getTarget

```java
public
Object
[] getTarget()
```

Returns the target objects for this relation.

**Returns:** an array containing the target objects for this relation

---

#### getTarget

public

Object

[] getTarget()

Returns the target objects for this relation.

setTarget

```java
public void setTarget​(
Object
target)
```

Sets the target object for this relation.

**Parameters:** target

- the target object for this relation

---

#### setTarget

public void setTarget​(

Object

target)

Sets the target object for this relation.

setTarget

```java
public void setTarget​(
Object
[] target)
```

Sets the target objects for this relation.

**Parameters:** target

- an array containing the target objects for this relation

---

#### setTarget

public void setTarget​(

Object

[] target)

Sets the target objects for this relation.

---

