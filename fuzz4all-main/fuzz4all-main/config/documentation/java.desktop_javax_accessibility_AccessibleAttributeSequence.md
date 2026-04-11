# Class AccessibleAttributeSequence

**Source:** `java.desktop\javax\accessibility\AccessibleAttributeSequence.html`

### Class Description

```java
public class
AccessibleAttributeSequence

extends
Object
```

This class collects together the span of text that share the same contiguous
set of attributes, along with that set of attributes. It is used by
implementors of the class

AccessibleContext

in order to generate

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

events.

**See Also:** AccessibleContext

,

AccessibleContext.ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

---

### Field Details

#### public int startIndex

The start index of the text sequence.

---

#### public int endIndex

The end index of the text sequence.

---

#### public
AttributeSet
attributes

The text attributes.

---

### Constructor Details

#### public AccessibleAttributeSequence​(int start,
int end,

AttributeSet
attr)

Constructs an

AccessibleAttributeSequence

with the given
parameters.

**Parameters:**
- start

- the beginning index of the span of text
- end

- the ending index of the span of text
- attr

- the

AttributeSet

shared by this text span

**Since:**
- 1.6

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AccessibleAttributeSequence

java.lang.Object

- javax.accessibility.AccessibleAttributeSequence

javax.accessibility.AccessibleAttributeSequence

```java
public class
AccessibleAttributeSequence

extends
Object
```

This class collects together the span of text that share the same contiguous
set of attributes, along with that set of attributes. It is used by
implementors of the class

AccessibleContext

in order to generate

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

events.

**See Also:** AccessibleContext

,

AccessibleContext.ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

public class

AccessibleAttributeSequence

extends

Object

This class collects together the span of text that share the same contiguous
set of attributes, along with that set of attributes. It is used by
implementors of the class

AccessibleContext

in order to generate

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

events.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

AttributeSet

attributes

The text attributes.

int

endIndex

The end index of the text sequence.

int

startIndex

The start index of the text sequence.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessibleAttributeSequence

​(int start,
int end,

AttributeSet

attr)

Constructs an

AccessibleAttributeSequence

with the given
parameters.

========== METHOD SUMMARY ===========

- Method Summary

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

Field Summary

Fields

Modifier and Type

Field

Description

AttributeSet

attributes

The text attributes.

int

endIndex

The end index of the text sequence.

int

startIndex

The start index of the text sequence.

---

#### Field Summary

The text attributes.

The end index of the text sequence.

The start index of the text sequence.

Constructor Summary

Constructors

Constructor

Description

AccessibleAttributeSequence

​(int start,
int end,

AttributeSet

attr)

Constructs an

AccessibleAttributeSequence

with the given
parameters.

---

#### Constructor Summary

Constructs an

AccessibleAttributeSequence

with the given
parameters.

Method Summary

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

============ FIELD DETAIL ===========

- Field Detail

- startIndex

```java
public int startIndex
```

The start index of the text sequence.

- endIndex

```java
public int endIndex
```

The end index of the text sequence.

- attributes

```java
public
AttributeSet
attributes
```

The text attributes.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibleAttributeSequence

```java
public AccessibleAttributeSequence​(int start,
int end,

AttributeSet
attr)
```

Constructs an

AccessibleAttributeSequence

with the given
parameters.

**Parameters:** start

- the beginning index of the span of text
**Parameters:** end

- the ending index of the span of text
**Parameters:** attr

- the

AttributeSet

shared by this text span
**Since:** 1.6

Field Detail

- startIndex

```java
public int startIndex
```

The start index of the text sequence.

- endIndex

```java
public int endIndex
```

The end index of the text sequence.

- attributes

```java
public
AttributeSet
attributes
```

The text attributes.

---

#### Field Detail

startIndex

```java
public int startIndex
```

The start index of the text sequence.

---

#### startIndex

public int startIndex

The start index of the text sequence.

endIndex

```java
public int endIndex
```

The end index of the text sequence.

---

#### endIndex

public int endIndex

The end index of the text sequence.

attributes

```java
public
AttributeSet
attributes
```

The text attributes.

---

#### attributes

public

AttributeSet

attributes

The text attributes.

Constructor Detail

- AccessibleAttributeSequence

```java
public AccessibleAttributeSequence​(int start,
int end,

AttributeSet
attr)
```

Constructs an

AccessibleAttributeSequence

with the given
parameters.

**Parameters:** start

- the beginning index of the span of text
**Parameters:** end

- the ending index of the span of text
**Parameters:** attr

- the

AttributeSet

shared by this text span
**Since:** 1.6

---

#### Constructor Detail

AccessibleAttributeSequence

```java
public AccessibleAttributeSequence​(int start,
int end,

AttributeSet
attr)
```

Constructs an

AccessibleAttributeSequence

with the given
parameters.

**Parameters:** start

- the beginning index of the span of text
**Parameters:** end

- the ending index of the span of text
**Parameters:** attr

- the

AttributeSet

shared by this text span
**Since:** 1.6

---

#### AccessibleAttributeSequence

public AccessibleAttributeSequence​(int start,
int end,

AttributeSet

attr)

Constructs an

AccessibleAttributeSequence

with the given
parameters.

---

