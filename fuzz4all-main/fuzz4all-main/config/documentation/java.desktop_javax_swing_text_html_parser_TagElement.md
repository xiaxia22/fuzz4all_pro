# Class TagElement

**Source:** `java.desktop\javax\swing\text\html\parser\TagElement.html`

### Class Description

```java
public class
TagElement

extends
Object
```

A generic HTML TagElement class. The methods define how white
space is interpreted around the tag.

---

### Field Details

*No entries found.*

### Constructor Details

#### public TagElement​(
Element
elem)

Creates a generic HTML TagElement class with

fictional

equals to

false

.

**Parameters:**
- elem

- an element

---

#### public TagElement​(
Element
elem,
boolean fictional)

Creates a generic HTML TagElement class.

**Parameters:**
- elem

- an element
- fictional

- if

true

the tag is inserted by error recovery.

---

### Method Details

#### public boolean breaksFlow()

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

**Returns:**
- true

if this tag causes a
line break to the flow of data, otherwise returns

false

---

#### public boolean isPreformatted()

Returns

true

if this tag is pre-formatted.

**Returns:**
- true

if this tag is pre-formatted,
otherwise returns

false

---

#### public
Element
getElement()

Returns the element.

**Returns:**
- the element

---

#### public
HTML.Tag
getHTMLTag()

Returns the tag constant corresponding to the name of the

element

**Returns:**
- the tag constant corresponding to the name of the

element

---

#### public boolean fictional()

Returns

true

if the tag is fictional.

**Returns:**
- true

if the tag is fictional.

---

### Additional Sections

#### Class TagElement

java.lang.Object

- javax.swing.text.html.parser.TagElement

javax.swing.text.html.parser.TagElement

```java
public class
TagElement

extends
Object
```

A generic HTML TagElement class. The methods define how white
space is interpreted around the tag.

public class

TagElement

extends

Object

A generic HTML TagElement class. The methods define how white
space is interpreted around the tag.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TagElement

​(

Element

elem)

Creates a generic HTML TagElement class with

fictional

equals to

false

.

TagElement

​(

Element

elem,
boolean fictional)

Creates a generic HTML TagElement class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

breaksFlow

()

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

boolean

fictional

()

Returns

true

if the tag is fictional.

Element

getElement

()

Returns the element.

HTML.Tag

getHTMLTag

()

Returns the tag constant corresponding to the name of the

element

boolean

isPreformatted

()

Returns

true

if this tag is pre-formatted.

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

TagElement

​(

Element

elem)

Creates a generic HTML TagElement class with

fictional

equals to

false

.

TagElement

​(

Element

elem,
boolean fictional)

Creates a generic HTML TagElement class.

---

#### Constructor Summary

Creates a generic HTML TagElement class with

fictional

equals to

false

.

Creates a generic HTML TagElement class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

breaksFlow

()

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

boolean

fictional

()

Returns

true

if the tag is fictional.

Element

getElement

()

Returns the element.

HTML.Tag

getHTMLTag

()

Returns the tag constant corresponding to the name of the

element

boolean

isPreformatted

()

Returns

true

if this tag is pre-formatted.

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

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

Returns

true

if the tag is fictional.

Returns the element.

Returns the tag constant corresponding to the name of the

element

Returns

true

if this tag is pre-formatted.

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

- TagElement

```java
public TagElement​(
Element
elem)
```

Creates a generic HTML TagElement class with

fictional

equals to

false

.

**Parameters:** elem

- an element

- TagElement

```java
public TagElement​(
Element
elem,
boolean fictional)
```

Creates a generic HTML TagElement class.

**Parameters:** elem

- an element
**Parameters:** fictional

- if

true

the tag is inserted by error recovery.

============ METHOD DETAIL ==========

- Method Detail

- breaksFlow

```java
public boolean breaksFlow()
```

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

**Returns:** true

if this tag causes a
line break to the flow of data, otherwise returns

false

- isPreformatted

```java
public boolean isPreformatted()
```

Returns

true

if this tag is pre-formatted.

**Returns:** true

if this tag is pre-formatted,
otherwise returns

false

- getElement

```java
public
Element
getElement()
```

Returns the element.

**Returns:** the element

- getHTMLTag

```java
public
HTML.Tag
getHTMLTag()
```

Returns the tag constant corresponding to the name of the

element

**Returns:** the tag constant corresponding to the name of the

element

- fictional

```java
public boolean fictional()
```

Returns

true

if the tag is fictional.

**Returns:** true

if the tag is fictional.

Constructor Detail

- TagElement

```java
public TagElement​(
Element
elem)
```

Creates a generic HTML TagElement class with

fictional

equals to

false

.

**Parameters:** elem

- an element

- TagElement

```java
public TagElement​(
Element
elem,
boolean fictional)
```

Creates a generic HTML TagElement class.

**Parameters:** elem

- an element
**Parameters:** fictional

- if

true

the tag is inserted by error recovery.

---

#### Constructor Detail

TagElement

```java
public TagElement​(
Element
elem)
```

Creates a generic HTML TagElement class with

fictional

equals to

false

.

**Parameters:** elem

- an element

---

#### TagElement

public TagElement​(

Element

elem)

Creates a generic HTML TagElement class with

fictional

equals to

false

.

TagElement

```java
public TagElement​(
Element
elem,
boolean fictional)
```

Creates a generic HTML TagElement class.

**Parameters:** elem

- an element
**Parameters:** fictional

- if

true

the tag is inserted by error recovery.

---

#### TagElement

public TagElement​(

Element

elem,
boolean fictional)

Creates a generic HTML TagElement class.

Method Detail

- breaksFlow

```java
public boolean breaksFlow()
```

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

**Returns:** true

if this tag causes a
line break to the flow of data, otherwise returns

false

- isPreformatted

```java
public boolean isPreformatted()
```

Returns

true

if this tag is pre-formatted.

**Returns:** true

if this tag is pre-formatted,
otherwise returns

false

- getElement

```java
public
Element
getElement()
```

Returns the element.

**Returns:** the element

- getHTMLTag

```java
public
HTML.Tag
getHTMLTag()
```

Returns the tag constant corresponding to the name of the

element

**Returns:** the tag constant corresponding to the name of the

element

- fictional

```java
public boolean fictional()
```

Returns

true

if the tag is fictional.

**Returns:** true

if the tag is fictional.

---

#### Method Detail

breaksFlow

```java
public boolean breaksFlow()
```

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

**Returns:** true

if this tag causes a
line break to the flow of data, otherwise returns

false

---

#### breaksFlow

public boolean breaksFlow()

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

isPreformatted

```java
public boolean isPreformatted()
```

Returns

true

if this tag is pre-formatted.

**Returns:** true

if this tag is pre-formatted,
otherwise returns

false

---

#### isPreformatted

public boolean isPreformatted()

Returns

true

if this tag is pre-formatted.

getElement

```java
public
Element
getElement()
```

Returns the element.

**Returns:** the element

---

#### getElement

public

Element

getElement()

Returns the element.

getHTMLTag

```java
public
HTML.Tag
getHTMLTag()
```

Returns the tag constant corresponding to the name of the

element

**Returns:** the tag constant corresponding to the name of the

element

---

#### getHTMLTag

public

HTML.Tag

getHTMLTag()

Returns the tag constant corresponding to the name of the

element

fictional

```java
public boolean fictional()
```

Returns

true

if the tag is fictional.

**Returns:** true

if the tag is fictional.

---

#### fictional

public boolean fictional()

Returns

true

if the tag is fictional.

---

