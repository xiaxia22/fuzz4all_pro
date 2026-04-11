# Interface AccessibleIcon

**Source:** `java.desktop\javax\accessibility\AccessibleIcon.html`

### Class Description

```java
public interface
AccessibleIcon
```

The

AccessibleIcon

interface should be supported by any object that
has an associated icon (e.g., buttons). This interface provides the standard
mechanism for an assistive technology to get descriptive information about
icons. Applications can determine if an object supports the

AccessibleIcon

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleIcon()

method. If the return value is
not

null

, the object supports this interface.

**All Known Implementing Classes:** ImageIcon.AccessibleImageIcon

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getAccessibleIconDescription()

Gets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

**Returns:**
- the description of the icon

---

#### void setAccessibleIconDescription​(
String
description)

Sets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

**Parameters:**
- description

- the description of the icon

---

#### int getAccessibleIconWidth()

Gets the width of the icon.

**Returns:**
- the width of the icon

---

#### int getAccessibleIconHeight()

Gets the height of the icon.

**Returns:**
- the height of the icon

---

### Additional Sections

#### Interface AccessibleIcon

**All Known Implementing Classes:** ImageIcon.AccessibleImageIcon

```java
public interface
AccessibleIcon
```

The

AccessibleIcon

interface should be supported by any object that
has an associated icon (e.g., buttons). This interface provides the standard
mechanism for an assistive technology to get descriptive information about
icons. Applications can determine if an object supports the

AccessibleIcon

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleIcon()

method. If the return value is
not

null

, the object supports this interface.

**Since:** 1.3
**See Also:** Accessible

,

AccessibleContext

public interface

AccessibleIcon

The

AccessibleIcon

interface should be supported by any object that
has an associated icon (e.g., buttons). This interface provides the standard
mechanism for an assistive technology to get descriptive information about
icons. Applications can determine if an object supports the

AccessibleIcon

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleIcon()

method. If the return value is
not

null

, the object supports this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getAccessibleIconDescription

()

Gets the description of the icon.

int

getAccessibleIconHeight

()

Gets the height of the icon.

int

getAccessibleIconWidth

()

Gets the width of the icon.

void

setAccessibleIconDescription

​(

String

description)

Sets the description of the icon.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getAccessibleIconDescription

()

Gets the description of the icon.

int

getAccessibleIconHeight

()

Gets the height of the icon.

int

getAccessibleIconWidth

()

Gets the width of the icon.

void

setAccessibleIconDescription

​(

String

description)

Sets the description of the icon.

---

#### Method Summary

Gets the description of the icon.

Gets the height of the icon.

Gets the width of the icon.

Sets the description of the icon.

============ METHOD DETAIL ==========

- Method Detail

- getAccessibleIconDescription

```java
String
getAccessibleIconDescription()
```

Gets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

**Returns:** the description of the icon

- setAccessibleIconDescription

```java
void setAccessibleIconDescription​(
String
description)
```

Sets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

**Parameters:** description

- the description of the icon

- getAccessibleIconWidth

```java
int getAccessibleIconWidth()
```

Gets the width of the icon.

**Returns:** the width of the icon

- getAccessibleIconHeight

```java
int getAccessibleIconHeight()
```

Gets the height of the icon.

**Returns:** the height of the icon

Method Detail

- getAccessibleIconDescription

```java
String
getAccessibleIconDescription()
```

Gets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

**Returns:** the description of the icon

- setAccessibleIconDescription

```java
void setAccessibleIconDescription​(
String
description)
```

Sets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

**Parameters:** description

- the description of the icon

- getAccessibleIconWidth

```java
int getAccessibleIconWidth()
```

Gets the width of the icon.

**Returns:** the width of the icon

- getAccessibleIconHeight

```java
int getAccessibleIconHeight()
```

Gets the height of the icon.

**Returns:** the height of the icon

---

#### Method Detail

getAccessibleIconDescription

```java
String
getAccessibleIconDescription()
```

Gets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

**Returns:** the description of the icon

---

#### getAccessibleIconDescription

String

getAccessibleIconDescription()

Gets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

setAccessibleIconDescription

```java
void setAccessibleIconDescription​(
String
description)
```

Sets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

**Parameters:** description

- the description of the icon

---

#### setAccessibleIconDescription

void setAccessibleIconDescription​(

String

description)

Sets the description of the icon. This is meant to be a brief textual
description of the object. For example, it might be presented to a blind
user to give an indication of the purpose of the icon.

getAccessibleIconWidth

```java
int getAccessibleIconWidth()
```

Gets the width of the icon.

**Returns:** the width of the icon

---

#### getAccessibleIconWidth

int getAccessibleIconWidth()

Gets the width of the icon.

getAccessibleIconHeight

```java
int getAccessibleIconHeight()
```

Gets the height of the icon.

**Returns:** the height of the icon

---

#### getAccessibleIconHeight

int getAccessibleIconHeight()

Gets the height of the icon.

---

