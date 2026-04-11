# Class StringCharacterIterator

**Source:** `java.base\java\text\StringCharacterIterator.html`

### Class Description

```java
public final class
StringCharacterIterator

extends
Object

implements
CharacterIterator
```

StringCharacterIterator

implements the

CharacterIterator

protocol for a

String

.
The

StringCharacterIterator

class iterates over the
entire

String

.

**All Implemented Interfaces:** Cloneable

,

CharacterIterator

---

### Field Details

*No entries found.*

### Constructor Details

#### public StringCharacterIterator​(
String
text)

Constructs an iterator with an initial index of 0.

**Parameters:**
- text

- the

String

to be iterated over

---

#### public StringCharacterIterator​(
String
text,
int pos)

Constructs an iterator with the specified initial index.

**Parameters:**
- text

- The String to be iterated over
- pos

- Initial iterator position

---

#### public StringCharacterIterator​(
String
text,
int begin,
int end,
int pos)

Constructs an iterator over the given range of the given string, with the
index set at the specified position.

**Parameters:**
- text

- The String to be iterated over
- begin

- Index of the first character
- end

- Index of the character following the last character
- pos

- Initial iterator position

---

### Method Details

#### public void setText​(
String
text)

Reset this iterator to point to a new string. This package-visible
method is used by other java.text classes that want to avoid allocating
new StringCharacterIterator objects every time their setText method
is called.

**Parameters:**
- text

- The String to be iterated over

**Since:**
- 1.2

---

#### public char first()

Implements CharacterIterator.first() for String.

**Specified by:**
- first

in interface

CharacterIterator

**Returns:**
- the first character in the text, or DONE if the text is empty

**See Also:**
- CharacterIterator.first()

---

#### public char last()

Implements CharacterIterator.last() for String.

**Specified by:**
- last

in interface

CharacterIterator

**Returns:**
- the last character in the text, or DONE if the text is empty

**See Also:**
- CharacterIterator.last()

---

#### public char setIndex​(int p)

Implements CharacterIterator.setIndex() for String.

**Specified by:**
- setIndex

in interface

CharacterIterator

**Parameters:**
- p

- the position within the text. Valid values range from
getBeginIndex() to getEndIndex(). An IllegalArgumentException is thrown
if an invalid value is supplied.

**Returns:**
- the character at the specified position or DONE if the specified position is equal to getEndIndex()

**See Also:**
- CharacterIterator.setIndex(int)

---

#### public char current()

Implements CharacterIterator.current() for String.

**Specified by:**
- current

in interface

CharacterIterator

**Returns:**
- the character at the current position or DONE if the current
position is off the end of the text.

**See Also:**
- CharacterIterator.current()

---

#### public char next()

Implements CharacterIterator.next() for String.

**Specified by:**
- next

in interface

CharacterIterator

**Returns:**
- the character at the new position or DONE if the new
position is off the end of the text range.

**See Also:**
- CharacterIterator.next()

---

#### public char previous()

Implements CharacterIterator.previous() for String.

**Specified by:**
- previous

in interface

CharacterIterator

**Returns:**
- the character at the new position or DONE if the current
position is equal to getBeginIndex().

**See Also:**
- CharacterIterator.previous()

---

#### public int getBeginIndex()

Implements CharacterIterator.getBeginIndex() for String.

**Specified by:**
- getBeginIndex

in interface

CharacterIterator

**Returns:**
- the index at which the text begins.

**See Also:**
- CharacterIterator.getBeginIndex()

---

#### public int getEndIndex()

Implements CharacterIterator.getEndIndex() for String.

**Specified by:**
- getEndIndex

in interface

CharacterIterator

**Returns:**
- the index after the last character in the text

**See Also:**
- CharacterIterator.getEndIndex()

---

#### public int getIndex()

Implements CharacterIterator.getIndex() for String.

**Specified by:**
- getIndex

in interface

CharacterIterator

**Returns:**
- the current index.

**See Also:**
- CharacterIterator.getIndex()

---

#### public boolean equals​(
Object
obj)

Compares the equality of two StringCharacterIterator objects.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the StringCharacterIterator object to be compared with.

**Returns:**
- true if the given obj is the same as this
StringCharacterIterator object; false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Computes a hashcode for this iterator.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- A hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
Object
clone()

Creates a copy of this iterator.

**Specified by:**
- clone

in interface

CharacterIterator

**Overrides:**
- clone

in class

Object

**Returns:**
- A copy of this

**See Also:**
- Cloneable

---

### Additional Sections

#### Class StringCharacterIterator

java.lang.Object

- java.text.StringCharacterIterator

java.text.StringCharacterIterator

**All Implemented Interfaces:** Cloneable

,

CharacterIterator

```java
public final class
StringCharacterIterator

extends
Object

implements
CharacterIterator
```

StringCharacterIterator

implements the

CharacterIterator

protocol for a

String

.
The

StringCharacterIterator

class iterates over the
entire

String

.

**Since:** 1.1
**See Also:** CharacterIterator

public final class

StringCharacterIterator

extends

Object

implements

CharacterIterator

StringCharacterIterator

implements the

CharacterIterator

protocol for a

String

.
The

StringCharacterIterator

class iterates over the
entire

String

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.text.

CharacterIterator

DONE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StringCharacterIterator

​(

String

text)

Constructs an iterator with an initial index of 0.

StringCharacterIterator

​(

String

text,
int pos)

Constructs an iterator with the specified initial index.

StringCharacterIterator

​(

String

text,
int begin,
int end,
int pos)

Constructs an iterator over the given range of the given string, with the
index set at the specified position.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of this iterator.

char

current

()

Implements CharacterIterator.current() for String.

boolean

equals

​(

Object

obj)

Compares the equality of two StringCharacterIterator objects.

char

first

()

Implements CharacterIterator.first() for String.

int

getBeginIndex

()

Implements CharacterIterator.getBeginIndex() for String.

int

getEndIndex

()

Implements CharacterIterator.getEndIndex() for String.

int

getIndex

()

Implements CharacterIterator.getIndex() for String.

int

hashCode

()

Computes a hashcode for this iterator.

char

last

()

Implements CharacterIterator.last() for String.

char

next

()

Implements CharacterIterator.next() for String.

char

previous

()

Implements CharacterIterator.previous() for String.

char

setIndex

​(int p)

Implements CharacterIterator.setIndex() for String.

void

setText

​(

String

text)

Reset this iterator to point to a new string.

- Methods declared in class java.lang.

Object

finalize

,

getClass

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

- Fields declared in interface java.text.

CharacterIterator

DONE

---

#### Field Summary

Fields declared in interface java.text.

CharacterIterator

DONE

---

#### Fields declared in interface java.text. CharacterIterator

Constructor Summary

Constructors

Constructor

Description

StringCharacterIterator

​(

String

text)

Constructs an iterator with an initial index of 0.

StringCharacterIterator

​(

String

text,
int pos)

Constructs an iterator with the specified initial index.

StringCharacterIterator

​(

String

text,
int begin,
int end,
int pos)

Constructs an iterator over the given range of the given string, with the
index set at the specified position.

---

#### Constructor Summary

Constructs an iterator with an initial index of 0.

Constructs an iterator with the specified initial index.

Constructs an iterator over the given range of the given string, with the
index set at the specified position.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of this iterator.

char

current

()

Implements CharacterIterator.current() for String.

boolean

equals

​(

Object

obj)

Compares the equality of two StringCharacterIterator objects.

char

first

()

Implements CharacterIterator.first() for String.

int

getBeginIndex

()

Implements CharacterIterator.getBeginIndex() for String.

int

getEndIndex

()

Implements CharacterIterator.getEndIndex() for String.

int

getIndex

()

Implements CharacterIterator.getIndex() for String.

int

hashCode

()

Computes a hashcode for this iterator.

char

last

()

Implements CharacterIterator.last() for String.

char

next

()

Implements CharacterIterator.next() for String.

char

previous

()

Implements CharacterIterator.previous() for String.

char

setIndex

​(int p)

Implements CharacterIterator.setIndex() for String.

void

setText

​(

String

text)

Reset this iterator to point to a new string.

- Methods declared in class java.lang.

Object

finalize

,

getClass

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

Creates a copy of this iterator.

Implements CharacterIterator.current() for String.

Compares the equality of two StringCharacterIterator objects.

Implements CharacterIterator.first() for String.

Implements CharacterIterator.getBeginIndex() for String.

Implements CharacterIterator.getEndIndex() for String.

Implements CharacterIterator.getIndex() for String.

Computes a hashcode for this iterator.

Implements CharacterIterator.last() for String.

Implements CharacterIterator.next() for String.

Implements CharacterIterator.previous() for String.

Implements CharacterIterator.setIndex() for String.

Reset this iterator to point to a new string.

Methods declared in class java.lang.

Object

finalize

,

getClass

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

- StringCharacterIterator

```java
public StringCharacterIterator​(
String
text)
```

Constructs an iterator with an initial index of 0.

**Parameters:** text

- the

String

to be iterated over

- StringCharacterIterator

```java
public StringCharacterIterator​(
String
text,
int pos)
```

Constructs an iterator with the specified initial index.

**Parameters:** text

- The String to be iterated over
**Parameters:** pos

- Initial iterator position

- StringCharacterIterator

```java
public StringCharacterIterator​(
String
text,
int begin,
int end,
int pos)
```

Constructs an iterator over the given range of the given string, with the
index set at the specified position.

**Parameters:** text

- The String to be iterated over
**Parameters:** begin

- Index of the first character
**Parameters:** end

- Index of the character following the last character
**Parameters:** pos

- Initial iterator position

============ METHOD DETAIL ==========

- Method Detail

- setText

```java
public void setText​(
String
text)
```

Reset this iterator to point to a new string. This package-visible
method is used by other java.text classes that want to avoid allocating
new StringCharacterIterator objects every time their setText method
is called.

**Parameters:** text

- The String to be iterated over
**Since:** 1.2

- first

```java
public char first()
```

Implements CharacterIterator.first() for String.

**Specified by:** first

in interface

CharacterIterator
**Returns:** the first character in the text, or DONE if the text is empty
**See Also:** CharacterIterator.first()

- last

```java
public char last()
```

Implements CharacterIterator.last() for String.

**Specified by:** last

in interface

CharacterIterator
**Returns:** the last character in the text, or DONE if the text is empty
**See Also:** CharacterIterator.last()

- setIndex

```java
public char setIndex​(int p)
```

Implements CharacterIterator.setIndex() for String.

**Specified by:** setIndex

in interface

CharacterIterator
**Parameters:** p

- the position within the text. Valid values range from
getBeginIndex() to getEndIndex(). An IllegalArgumentException is thrown
if an invalid value is supplied.
**Returns:** the character at the specified position or DONE if the specified position is equal to getEndIndex()
**See Also:** CharacterIterator.setIndex(int)

- current

```java
public char current()
```

Implements CharacterIterator.current() for String.

**Specified by:** current

in interface

CharacterIterator
**Returns:** the character at the current position or DONE if the current
position is off the end of the text.
**See Also:** CharacterIterator.current()

- next

```java
public char next()
```

Implements CharacterIterator.next() for String.

**Specified by:** next

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the new
position is off the end of the text range.
**See Also:** CharacterIterator.next()

- previous

```java
public char previous()
```

Implements CharacterIterator.previous() for String.

**Specified by:** previous

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the current
position is equal to getBeginIndex().
**See Also:** CharacterIterator.previous()

- getBeginIndex

```java
public int getBeginIndex()
```

Implements CharacterIterator.getBeginIndex() for String.

**Specified by:** getBeginIndex

in interface

CharacterIterator
**Returns:** the index at which the text begins.
**See Also:** CharacterIterator.getBeginIndex()

- getEndIndex

```java
public int getEndIndex()
```

Implements CharacterIterator.getEndIndex() for String.

**Specified by:** getEndIndex

in interface

CharacterIterator
**Returns:** the index after the last character in the text
**See Also:** CharacterIterator.getEndIndex()

- getIndex

```java
public int getIndex()
```

Implements CharacterIterator.getIndex() for String.

**Specified by:** getIndex

in interface

CharacterIterator
**Returns:** the current index.
**See Also:** CharacterIterator.getIndex()

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the equality of two StringCharacterIterator objects.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the StringCharacterIterator object to be compared with.
**Returns:** true if the given obj is the same as this
StringCharacterIterator object; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes a hashcode for this iterator.

**Overrides:** hashCode

in class

Object
**Returns:** A hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Creates a copy of this iterator.

**Specified by:** clone

in interface

CharacterIterator
**Overrides:** clone

in class

Object
**Returns:** A copy of this
**See Also:** Cloneable

Constructor Detail

- StringCharacterIterator

```java
public StringCharacterIterator​(
String
text)
```

Constructs an iterator with an initial index of 0.

**Parameters:** text

- the

String

to be iterated over

- StringCharacterIterator

```java
public StringCharacterIterator​(
String
text,
int pos)
```

Constructs an iterator with the specified initial index.

**Parameters:** text

- The String to be iterated over
**Parameters:** pos

- Initial iterator position

- StringCharacterIterator

```java
public StringCharacterIterator​(
String
text,
int begin,
int end,
int pos)
```

Constructs an iterator over the given range of the given string, with the
index set at the specified position.

**Parameters:** text

- The String to be iterated over
**Parameters:** begin

- Index of the first character
**Parameters:** end

- Index of the character following the last character
**Parameters:** pos

- Initial iterator position

---

#### Constructor Detail

StringCharacterIterator

```java
public StringCharacterIterator​(
String
text)
```

Constructs an iterator with an initial index of 0.

**Parameters:** text

- the

String

to be iterated over

---

#### StringCharacterIterator

public StringCharacterIterator​(

String

text)

Constructs an iterator with an initial index of 0.

StringCharacterIterator

```java
public StringCharacterIterator​(
String
text,
int pos)
```

Constructs an iterator with the specified initial index.

**Parameters:** text

- The String to be iterated over
**Parameters:** pos

- Initial iterator position

---

#### StringCharacterIterator

public StringCharacterIterator​(

String

text,
int pos)

Constructs an iterator with the specified initial index.

StringCharacterIterator

```java
public StringCharacterIterator​(
String
text,
int begin,
int end,
int pos)
```

Constructs an iterator over the given range of the given string, with the
index set at the specified position.

**Parameters:** text

- The String to be iterated over
**Parameters:** begin

- Index of the first character
**Parameters:** end

- Index of the character following the last character
**Parameters:** pos

- Initial iterator position

---

#### StringCharacterIterator

public StringCharacterIterator​(

String

text,
int begin,
int end,
int pos)

Constructs an iterator over the given range of the given string, with the
index set at the specified position.

Method Detail

- setText

```java
public void setText​(
String
text)
```

Reset this iterator to point to a new string. This package-visible
method is used by other java.text classes that want to avoid allocating
new StringCharacterIterator objects every time their setText method
is called.

**Parameters:** text

- The String to be iterated over
**Since:** 1.2

- first

```java
public char first()
```

Implements CharacterIterator.first() for String.

**Specified by:** first

in interface

CharacterIterator
**Returns:** the first character in the text, or DONE if the text is empty
**See Also:** CharacterIterator.first()

- last

```java
public char last()
```

Implements CharacterIterator.last() for String.

**Specified by:** last

in interface

CharacterIterator
**Returns:** the last character in the text, or DONE if the text is empty
**See Also:** CharacterIterator.last()

- setIndex

```java
public char setIndex​(int p)
```

Implements CharacterIterator.setIndex() for String.

**Specified by:** setIndex

in interface

CharacterIterator
**Parameters:** p

- the position within the text. Valid values range from
getBeginIndex() to getEndIndex(). An IllegalArgumentException is thrown
if an invalid value is supplied.
**Returns:** the character at the specified position or DONE if the specified position is equal to getEndIndex()
**See Also:** CharacterIterator.setIndex(int)

- current

```java
public char current()
```

Implements CharacterIterator.current() for String.

**Specified by:** current

in interface

CharacterIterator
**Returns:** the character at the current position or DONE if the current
position is off the end of the text.
**See Also:** CharacterIterator.current()

- next

```java
public char next()
```

Implements CharacterIterator.next() for String.

**Specified by:** next

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the new
position is off the end of the text range.
**See Also:** CharacterIterator.next()

- previous

```java
public char previous()
```

Implements CharacterIterator.previous() for String.

**Specified by:** previous

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the current
position is equal to getBeginIndex().
**See Also:** CharacterIterator.previous()

- getBeginIndex

```java
public int getBeginIndex()
```

Implements CharacterIterator.getBeginIndex() for String.

**Specified by:** getBeginIndex

in interface

CharacterIterator
**Returns:** the index at which the text begins.
**See Also:** CharacterIterator.getBeginIndex()

- getEndIndex

```java
public int getEndIndex()
```

Implements CharacterIterator.getEndIndex() for String.

**Specified by:** getEndIndex

in interface

CharacterIterator
**Returns:** the index after the last character in the text
**See Also:** CharacterIterator.getEndIndex()

- getIndex

```java
public int getIndex()
```

Implements CharacterIterator.getIndex() for String.

**Specified by:** getIndex

in interface

CharacterIterator
**Returns:** the current index.
**See Also:** CharacterIterator.getIndex()

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the equality of two StringCharacterIterator objects.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the StringCharacterIterator object to be compared with.
**Returns:** true if the given obj is the same as this
StringCharacterIterator object; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes a hashcode for this iterator.

**Overrides:** hashCode

in class

Object
**Returns:** A hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Creates a copy of this iterator.

**Specified by:** clone

in interface

CharacterIterator
**Overrides:** clone

in class

Object
**Returns:** A copy of this
**See Also:** Cloneable

---

#### Method Detail

setText

```java
public void setText​(
String
text)
```

Reset this iterator to point to a new string. This package-visible
method is used by other java.text classes that want to avoid allocating
new StringCharacterIterator objects every time their setText method
is called.

**Parameters:** text

- The String to be iterated over
**Since:** 1.2

---

#### setText

public void setText​(

String

text)

Reset this iterator to point to a new string. This package-visible
method is used by other java.text classes that want to avoid allocating
new StringCharacterIterator objects every time their setText method
is called.

first

```java
public char first()
```

Implements CharacterIterator.first() for String.

**Specified by:** first

in interface

CharacterIterator
**Returns:** the first character in the text, or DONE if the text is empty
**See Also:** CharacterIterator.first()

---

#### first

public char first()

Implements CharacterIterator.first() for String.

last

```java
public char last()
```

Implements CharacterIterator.last() for String.

**Specified by:** last

in interface

CharacterIterator
**Returns:** the last character in the text, or DONE if the text is empty
**See Also:** CharacterIterator.last()

---

#### last

public char last()

Implements CharacterIterator.last() for String.

setIndex

```java
public char setIndex​(int p)
```

Implements CharacterIterator.setIndex() for String.

**Specified by:** setIndex

in interface

CharacterIterator
**Parameters:** p

- the position within the text. Valid values range from
getBeginIndex() to getEndIndex(). An IllegalArgumentException is thrown
if an invalid value is supplied.
**Returns:** the character at the specified position or DONE if the specified position is equal to getEndIndex()
**See Also:** CharacterIterator.setIndex(int)

---

#### setIndex

public char setIndex​(int p)

Implements CharacterIterator.setIndex() for String.

current

```java
public char current()
```

Implements CharacterIterator.current() for String.

**Specified by:** current

in interface

CharacterIterator
**Returns:** the character at the current position or DONE if the current
position is off the end of the text.
**See Also:** CharacterIterator.current()

---

#### current

public char current()

Implements CharacterIterator.current() for String.

next

```java
public char next()
```

Implements CharacterIterator.next() for String.

**Specified by:** next

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the new
position is off the end of the text range.
**See Also:** CharacterIterator.next()

---

#### next

public char next()

Implements CharacterIterator.next() for String.

previous

```java
public char previous()
```

Implements CharacterIterator.previous() for String.

**Specified by:** previous

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the current
position is equal to getBeginIndex().
**See Also:** CharacterIterator.previous()

---

#### previous

public char previous()

Implements CharacterIterator.previous() for String.

getBeginIndex

```java
public int getBeginIndex()
```

Implements CharacterIterator.getBeginIndex() for String.

**Specified by:** getBeginIndex

in interface

CharacterIterator
**Returns:** the index at which the text begins.
**See Also:** CharacterIterator.getBeginIndex()

---

#### getBeginIndex

public int getBeginIndex()

Implements CharacterIterator.getBeginIndex() for String.

getEndIndex

```java
public int getEndIndex()
```

Implements CharacterIterator.getEndIndex() for String.

**Specified by:** getEndIndex

in interface

CharacterIterator
**Returns:** the index after the last character in the text
**See Also:** CharacterIterator.getEndIndex()

---

#### getEndIndex

public int getEndIndex()

Implements CharacterIterator.getEndIndex() for String.

getIndex

```java
public int getIndex()
```

Implements CharacterIterator.getIndex() for String.

**Specified by:** getIndex

in interface

CharacterIterator
**Returns:** the current index.
**See Also:** CharacterIterator.getIndex()

---

#### getIndex

public int getIndex()

Implements CharacterIterator.getIndex() for String.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the equality of two StringCharacterIterator objects.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the StringCharacterIterator object to be compared with.
**Returns:** true if the given obj is the same as this
StringCharacterIterator object; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the equality of two StringCharacterIterator objects.

hashCode

```java
public int hashCode()
```

Computes a hashcode for this iterator.

**Overrides:** hashCode

in class

Object
**Returns:** A hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes a hashcode for this iterator.

clone

```java
public
Object
clone()
```

Creates a copy of this iterator.

**Specified by:** clone

in interface

CharacterIterator
**Overrides:** clone

in class

Object
**Returns:** A copy of this
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a copy of this iterator.

---

