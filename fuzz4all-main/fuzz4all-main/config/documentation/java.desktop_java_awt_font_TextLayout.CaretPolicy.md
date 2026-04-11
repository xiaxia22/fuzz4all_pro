# Class TextLayout.CaretPolicy

**Source:** `java.desktop\java\awt\font\TextLayout.CaretPolicy.html`

### Class Description

```java
public static class
TextLayout.CaretPolicy

extends
Object
```

Defines a policy for determining the strong caret location.
This class contains one method,

getStrongCaret

, which
is used to specify the policy that determines the strong caret in
dual-caret text. The strong caret is used to move the caret to the
left or right. Instances of this class can be passed to

getCaretShapes

,

getNextLeftHit

and

getNextRightHit

to customize strong caret
selection.

To specify alternate caret policies, subclass

CaretPolicy

and override

getStrongCaret

.

getStrongCaret

should inspect the two

TextHitInfo

arguments and choose
one of them as the strong caret.

Most clients do not need to use this class.

**Enclosing class:** TextLayout

---

### Field Details

*No entries found.*

### Constructor Details

#### public CaretPolicy()

Constructs a

CaretPolicy

.

---

### Method Details

#### public
TextHitInfo
getStrongCaret​(
TextHitInfo
hit1,

TextHitInfo
hit2,

TextLayout
layout)

Chooses one of the specified

TextHitInfo

instances as
a strong caret in the specified

TextLayout

.

**Parameters:**
- hit1

- a valid hit in

layout
- hit2

- a valid hit in

layout
- layout

- the

TextLayout

in which

hit1

and

hit2

are used

**Returns:**
- hit1

or

hit2

(or an equivalent

TextHitInfo

), indicating the
strong caret.

---

### Additional Sections

#### Class TextLayout.CaretPolicy

java.lang.Object

- java.awt.font.TextLayout.CaretPolicy

java.awt.font.TextLayout.CaretPolicy

**Enclosing class:** TextLayout

```java
public static class
TextLayout.CaretPolicy

extends
Object
```

Defines a policy for determining the strong caret location.
This class contains one method,

getStrongCaret

, which
is used to specify the policy that determines the strong caret in
dual-caret text. The strong caret is used to move the caret to the
left or right. Instances of this class can be passed to

getCaretShapes

,

getNextLeftHit

and

getNextRightHit

to customize strong caret
selection.

To specify alternate caret policies, subclass

CaretPolicy

and override

getStrongCaret

.

getStrongCaret

should inspect the two

TextHitInfo

arguments and choose
one of them as the strong caret.

Most clients do not need to use this class.

public static class

TextLayout.CaretPolicy

extends

Object

Defines a policy for determining the strong caret location.
This class contains one method,

getStrongCaret

, which
is used to specify the policy that determines the strong caret in
dual-caret text. The strong caret is used to move the caret to the
left or right. Instances of this class can be passed to

getCaretShapes

,

getNextLeftHit

and

getNextRightHit

to customize strong caret
selection.

To specify alternate caret policies, subclass

CaretPolicy

and override

getStrongCaret

.

getStrongCaret

should inspect the two

TextHitInfo

arguments and choose
one of them as the strong caret.

Most clients do not need to use this class.

To specify alternate caret policies, subclass

CaretPolicy

and override

getStrongCaret

.

getStrongCaret

should inspect the two

TextHitInfo

arguments and choose
one of them as the strong caret.

Most clients do not need to use this class.

Most clients do not need to use this class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CaretPolicy

()

Constructs a

CaretPolicy

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TextHitInfo

getStrongCaret

​(

TextHitInfo

hit1,

TextHitInfo

hit2,

TextLayout

layout)

Chooses one of the specified

TextHitInfo

instances as
a strong caret in the specified

TextLayout

.

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

CaretPolicy

()

Constructs a

CaretPolicy

.

---

#### Constructor Summary

Constructs a

CaretPolicy

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TextHitInfo

getStrongCaret

​(

TextHitInfo

hit1,

TextHitInfo

hit2,

TextLayout

layout)

Chooses one of the specified

TextHitInfo

instances as
a strong caret in the specified

TextLayout

.

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

Chooses one of the specified

TextHitInfo

instances as
a strong caret in the specified

TextLayout

.

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

- CaretPolicy

```java
public CaretPolicy()
```

Constructs a

CaretPolicy

.

============ METHOD DETAIL ==========

- Method Detail

- getStrongCaret

```java
public
TextHitInfo
getStrongCaret​(
TextHitInfo
hit1,

TextHitInfo
hit2,

TextLayout
layout)
```

Chooses one of the specified

TextHitInfo

instances as
a strong caret in the specified

TextLayout

.

**Parameters:** hit1

- a valid hit in

layout
**Parameters:** hit2

- a valid hit in

layout
**Parameters:** layout

- the

TextLayout

in which

hit1

and

hit2

are used
**Returns:** hit1

or

hit2

(or an equivalent

TextHitInfo

), indicating the
strong caret.

Constructor Detail

- CaretPolicy

```java
public CaretPolicy()
```

Constructs a

CaretPolicy

.

---

#### Constructor Detail

CaretPolicy

```java
public CaretPolicy()
```

Constructs a

CaretPolicy

.

---

#### CaretPolicy

public CaretPolicy()

Constructs a

CaretPolicy

.

Method Detail

- getStrongCaret

```java
public
TextHitInfo
getStrongCaret​(
TextHitInfo
hit1,

TextHitInfo
hit2,

TextLayout
layout)
```

Chooses one of the specified

TextHitInfo

instances as
a strong caret in the specified

TextLayout

.

**Parameters:** hit1

- a valid hit in

layout
**Parameters:** hit2

- a valid hit in

layout
**Parameters:** layout

- the

TextLayout

in which

hit1

and

hit2

are used
**Returns:** hit1

or

hit2

(or an equivalent

TextHitInfo

), indicating the
strong caret.

---

#### Method Detail

getStrongCaret

```java
public
TextHitInfo
getStrongCaret​(
TextHitInfo
hit1,

TextHitInfo
hit2,

TextLayout
layout)
```

Chooses one of the specified

TextHitInfo

instances as
a strong caret in the specified

TextLayout

.

**Parameters:** hit1

- a valid hit in

layout
**Parameters:** hit2

- a valid hit in

layout
**Parameters:** layout

- the

TextLayout

in which

hit1

and

hit2

are used
**Returns:** hit1

or

hit2

(or an equivalent

TextHitInfo

), indicating the
strong caret.

---

#### getStrongCaret

public

TextHitInfo

getStrongCaret​(

TextHitInfo

hit1,

TextHitInfo

hit2,

TextLayout

layout)

Chooses one of the specified

TextHitInfo

instances as
a strong caret in the specified

TextLayout

.

---

