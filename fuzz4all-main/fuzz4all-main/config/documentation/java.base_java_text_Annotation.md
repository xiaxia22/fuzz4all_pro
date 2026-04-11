# Class Annotation

**Source:** `java.base\java\text\Annotation.html`

### Class Description

```java
public class
Annotation

extends
Object
```

An Annotation object is used as a wrapper for a text attribute value if
the attribute has annotation characteristics. These characteristics are:

- The text range that the attribute is applied to is critical to the
semantics of the range. That means, the attribute cannot be applied to subranges
of the text range that it applies to, and, if two adjacent text ranges have
the same value for this attribute, the attribute still cannot be applied to
the combined range as a whole with this value.

The attribute or its value usually do no longer apply if the underlying text is
changed.

An example is grammatical information attached to a sentence:
For the previous sentence, you can say that "an example"
is the subject, but you cannot say the same about "an", "example", or "exam".
When the text is changed, the grammatical information typically becomes invalid.
Another example is Japanese reading information (yomi).

Wrapping the attribute value into an Annotation object guarantees that
adjacent text runs don't get merged even if the attribute values are equal,
and indicates to text containers that the attribute should be discarded if
the underlying text is modified.

**Since:** 1.2
**See Also:** AttributedCharacterIterator

---

### Field Details

*No entries found.*

### Constructor Details

#### public Annotation​(
Object
value)

Constructs an annotation record with the given value, which
may be null.

**Parameters:**
- value

- the value of the attribute

---

### Method Details

#### public
Object
getValue()

Returns the value of the attribute, which may be null.

**Returns:**
- the value of the attribute

---

#### public
String
toString()

Returns the String representation of this Annotation.

**Overrides:**
- toString

in class

Object

**Returns:**
- the

String

representation of this

Annotation

---

### Additional Sections

#### Class Annotation

java.lang.Object

- java.text.Annotation

java.text.Annotation

```java
public class
Annotation

extends
Object
```

An Annotation object is used as a wrapper for a text attribute value if
the attribute has annotation characteristics. These characteristics are:

- The text range that the attribute is applied to is critical to the
semantics of the range. That means, the attribute cannot be applied to subranges
of the text range that it applies to, and, if two adjacent text ranges have
the same value for this attribute, the attribute still cannot be applied to
the combined range as a whole with this value.

The attribute or its value usually do no longer apply if the underlying text is
changed.

An example is grammatical information attached to a sentence:
For the previous sentence, you can say that "an example"
is the subject, but you cannot say the same about "an", "example", or "exam".
When the text is changed, the grammatical information typically becomes invalid.
Another example is Japanese reading information (yomi).

Wrapping the attribute value into an Annotation object guarantees that
adjacent text runs don't get merged even if the attribute values are equal,
and indicates to text containers that the attribute should be discarded if
the underlying text is modified.

**Since:** 1.2
**See Also:** AttributedCharacterIterator

public class

Annotation

extends

Object

An Annotation object is used as a wrapper for a text attribute value if
the attribute has annotation characteristics. These characteristics are:

- The text range that the attribute is applied to is critical to the
semantics of the range. That means, the attribute cannot be applied to subranges
of the text range that it applies to, and, if two adjacent text ranges have
the same value for this attribute, the attribute still cannot be applied to
the combined range as a whole with this value.

The attribute or its value usually do no longer apply if the underlying text is
changed.

An example is grammatical information attached to a sentence:
For the previous sentence, you can say that "an example"
is the subject, but you cannot say the same about "an", "example", or "exam".
When the text is changed, the grammatical information typically becomes invalid.
Another example is Japanese reading information (yomi).

Wrapping the attribute value into an Annotation object guarantees that
adjacent text runs don't get merged even if the attribute values are equal,
and indicates to text containers that the attribute should be discarded if
the underlying text is modified.

The text range that the attribute is applied to is critical to the
semantics of the range. That means, the attribute cannot be applied to subranges
of the text range that it applies to, and, if two adjacent text ranges have
the same value for this attribute, the attribute still cannot be applied to
the combined range as a whole with this value.

The attribute or its value usually do no longer apply if the underlying text is
changed.

Wrapping the attribute value into an Annotation object guarantees that
adjacent text runs don't get merged even if the attribute values are equal,
and indicates to text containers that the attribute should be discarded if
the underlying text is modified.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Annotation

​(

Object

value)

Constructs an annotation record with the given value, which
may be null.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getValue

()

Returns the value of the attribute, which may be null.

String

toString

()

Returns the String representation of this Annotation.

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

Annotation

​(

Object

value)

Constructs an annotation record with the given value, which
may be null.

---

#### Constructor Summary

Constructs an annotation record with the given value, which
may be null.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getValue

()

Returns the value of the attribute, which may be null.

String

toString

()

Returns the String representation of this Annotation.

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

Returns the value of the attribute, which may be null.

Returns the String representation of this Annotation.

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

- Annotation

```java
public Annotation​(
Object
value)
```

Constructs an annotation record with the given value, which
may be null.

**Parameters:** value

- the value of the attribute

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public
Object
getValue()
```

Returns the value of the attribute, which may be null.

**Returns:** the value of the attribute

- toString

```java
public
String
toString()
```

Returns the String representation of this Annotation.

**Overrides:** toString

in class

Object
**Returns:** the

String

representation of this

Annotation

Constructor Detail

- Annotation

```java
public Annotation​(
Object
value)
```

Constructs an annotation record with the given value, which
may be null.

**Parameters:** value

- the value of the attribute

---

#### Constructor Detail

Annotation

```java
public Annotation​(
Object
value)
```

Constructs an annotation record with the given value, which
may be null.

**Parameters:** value

- the value of the attribute

---

#### Annotation

public Annotation​(

Object

value)

Constructs an annotation record with the given value, which
may be null.

Method Detail

- getValue

```java
public
Object
getValue()
```

Returns the value of the attribute, which may be null.

**Returns:** the value of the attribute

- toString

```java
public
String
toString()
```

Returns the String representation of this Annotation.

**Overrides:** toString

in class

Object
**Returns:** the

String

representation of this

Annotation

---

#### Method Detail

getValue

```java
public
Object
getValue()
```

Returns the value of the attribute, which may be null.

**Returns:** the value of the attribute

---

#### getValue

public

Object

getValue()

Returns the value of the attribute, which may be null.

toString

```java
public
String
toString()
```

Returns the String representation of this Annotation.

**Overrides:** toString

in class

Object
**Returns:** the

String

representation of this

Annotation

---

#### toString

public

String

toString()

Returns the String representation of this Annotation.

---

