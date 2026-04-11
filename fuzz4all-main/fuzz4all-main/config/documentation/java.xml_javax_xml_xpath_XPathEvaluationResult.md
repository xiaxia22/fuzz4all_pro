# Interface XPathEvaluationResult<T>

**Source:** `java.xml\javax\xml\xpath\XPathEvaluationResult.html`

### Class Description

```java
public interface
XPathEvaluationResult<T>
```

The

XPathEvaluationResult

interface represents the result of the
evaluation of an XPath expression within the context of a particular node.
The evaluation of an XPath expression can result in various result types as
defined in XML Path Language (XPath) Version 1.0.

**Type Parameters:** T

- the object type returned by the XPath evaluation.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### XPathEvaluationResult.XPathResultType
type()

Return the result type as an enum specified by

XPathResultType

**Returns:**
- the result type

---

#### T
value()

Returns the value of the result as the type

<T>

specified for the class.

**Returns:**
- The value of the result.

---

### Additional Sections

#### Interface XPathEvaluationResult<T>

**Type Parameters:** T

- the object type returned by the XPath evaluation.

```java
public interface
XPathEvaluationResult<T>
```

The

XPathEvaluationResult

interface represents the result of the
evaluation of an XPath expression within the context of a particular node.
The evaluation of an XPath expression can result in various result types as
defined in XML Path Language (XPath) Version 1.0.

**Since:** 9
**See Also:** XML Path Language (XPath) Version
1.0

public interface

XPathEvaluationResult<T>

The

XPathEvaluationResult

interface represents the result of the
evaluation of an XPath expression within the context of a particular node.
The evaluation of an XPath expression can result in various result types as
defined in XML Path Language (XPath) Version 1.0.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

XPathEvaluationResult.XPathResultType

XPathResultType represents possible return types of an XPath evaluation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

XPathEvaluationResult.XPathResultType

type

()

Return the result type as an enum specified by

XPathResultType

T

value

()

Returns the value of the result as the type

<T>

specified for the class.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

XPathEvaluationResult.XPathResultType

XPathResultType represents possible return types of an XPath evaluation.

---

#### Nested Class Summary

XPathResultType represents possible return types of an XPath evaluation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

XPathEvaluationResult.XPathResultType

type

()

Return the result type as an enum specified by

XPathResultType

T

value

()

Returns the value of the result as the type

<T>

specified for the class.

---

#### Method Summary

Return the result type as an enum specified by

XPathResultType

Returns the value of the result as the type

<T>

specified for the class.

============ METHOD DETAIL ==========

- Method Detail

- type

```java
XPathEvaluationResult.XPathResultType
type()
```

Return the result type as an enum specified by

XPathResultType

**Returns:** the result type

- value

```java
T
value()
```

Returns the value of the result as the type

<T>

specified for the class.

**Returns:** The value of the result.

Method Detail

- type

```java
XPathEvaluationResult.XPathResultType
type()
```

Return the result type as an enum specified by

XPathResultType

**Returns:** the result type

- value

```java
T
value()
```

Returns the value of the result as the type

<T>

specified for the class.

**Returns:** The value of the result.

---

#### Method Detail

type

```java
XPathEvaluationResult.XPathResultType
type()
```

Return the result type as an enum specified by

XPathResultType

**Returns:** the result type

---

#### type

XPathEvaluationResult.XPathResultType

type()

Return the result type as an enum specified by

XPathResultType

value

```java
T
value()
```

Returns the value of the result as the type

<T>

specified for the class.

**Returns:** The value of the result.

---

#### value

T

value()

Returns the value of the result as the type

<T>

specified for the class.

---

