# Interface XPathExpression

**Source:** `jdk.xml.dom\org\w3c\dom\xpath\XPathExpression.html`

### Class Description

```java
public interface
XPathExpression
```

The

XPathExpression

interface represents a parsed and resolved
XPath expression.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
evaluate​(
Node
contextNode,
short type,

Object
result)
throws
XPathException
,

DOMException

Evaluates this XPath expression and returns a result.

**Parameters:**
- contextNode

- The

context

is context node for the
evaluation of this XPath expression.If the XPathEvaluator was
obtained by casting the

Document

then this must be
owned by the same document and must be a

Document

,

Element

,

Attribute

,

Text

,

CDATASection

,

Comment

,

ProcessingInstruction

, or

XPathNamespace

node.If the context node is a

Text

or a

CDATASection

, then the context is interpreted as the
whole logical text node as seen by XPath, unless the node is empty
in which case it may not serve as the XPath context.
- type

- If a specific

type

is specified, then the
result will be coerced to return the specified type relying on
XPath conversions and fail if the desired coercion is not possible.
This must be one of the type codes of

XPathResult

.
- result

- The

result

specifies a specific result
object which may be reused and returned by this method. If this is
specified as

null

or the implementation does not reuse
the specified result, a new result object will be constructed and
returned.For XPath 1.0 results, this object will be of type

XPathResult

.

**Returns:**
- The result of the evaluation of the XPath expression.For XPath
1.0 results, this object will be of type

XPathResult

.

**Throws:**
- XPathException

- TYPE_ERR: Raised if the result cannot be converted to return the
specified type.
- DOMException

- WRONG_DOCUMENT_ERR: The Node is from a document that is not supported
by the XPathEvaluator that created this

XPathExpression

.

NOT_SUPPORTED_ERR: The Node is not a type permitted as an XPath
context node or the request type is not permitted by this

XPathExpression

.

---

### Additional Sections

#### Interface XPathExpression

```java
public interface
XPathExpression
```

The

XPathExpression

interface represents a parsed and resolved
XPath expression.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

public interface

XPathExpression

The

XPathExpression

interface represents a parsed and resolved
XPath expression.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

evaluate

​(

Node

contextNode,
short type,

Object

result)

Evaluates this XPath expression and returns a result.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

evaluate

​(

Node

contextNode,
short type,

Object

result)

Evaluates this XPath expression and returns a result.

---

#### Method Summary

Evaluates this XPath expression and returns a result.

============ METHOD DETAIL ==========

- Method Detail

- evaluate

```java
Object
evaluate​(
Node
contextNode,
short type,

Object
result)
throws
XPathException
,

DOMException
```

Evaluates this XPath expression and returns a result.

**Parameters:** contextNode

- The

context

is context node for the
evaluation of this XPath expression.If the XPathEvaluator was
obtained by casting the

Document

then this must be
owned by the same document and must be a

Document

,

Element

,

Attribute

,

Text

,

CDATASection

,

Comment

,

ProcessingInstruction

, or

XPathNamespace

node.If the context node is a

Text

or a

CDATASection

, then the context is interpreted as the
whole logical text node as seen by XPath, unless the node is empty
in which case it may not serve as the XPath context.
**Parameters:** type

- If a specific

type

is specified, then the
result will be coerced to return the specified type relying on
XPath conversions and fail if the desired coercion is not possible.
This must be one of the type codes of

XPathResult

.
**Parameters:** result

- The

result

specifies a specific result
object which may be reused and returned by this method. If this is
specified as

null

or the implementation does not reuse
the specified result, a new result object will be constructed and
returned.For XPath 1.0 results, this object will be of type

XPathResult

.
**Returns:** The result of the evaluation of the XPath expression.For XPath
1.0 results, this object will be of type

XPathResult

.
**Throws:** XPathException

- TYPE_ERR: Raised if the result cannot be converted to return the
specified type.
**Throws:** DOMException

- WRONG_DOCUMENT_ERR: The Node is from a document that is not supported
by the XPathEvaluator that created this

XPathExpression

.

NOT_SUPPORTED_ERR: The Node is not a type permitted as an XPath
context node or the request type is not permitted by this

XPathExpression

.

Method Detail

- evaluate

```java
Object
evaluate​(
Node
contextNode,
short type,

Object
result)
throws
XPathException
,

DOMException
```

Evaluates this XPath expression and returns a result.

**Parameters:** contextNode

- The

context

is context node for the
evaluation of this XPath expression.If the XPathEvaluator was
obtained by casting the

Document

then this must be
owned by the same document and must be a

Document

,

Element

,

Attribute

,

Text

,

CDATASection

,

Comment

,

ProcessingInstruction

, or

XPathNamespace

node.If the context node is a

Text

or a

CDATASection

, then the context is interpreted as the
whole logical text node as seen by XPath, unless the node is empty
in which case it may not serve as the XPath context.
**Parameters:** type

- If a specific

type

is specified, then the
result will be coerced to return the specified type relying on
XPath conversions and fail if the desired coercion is not possible.
This must be one of the type codes of

XPathResult

.
**Parameters:** result

- The

result

specifies a specific result
object which may be reused and returned by this method. If this is
specified as

null

or the implementation does not reuse
the specified result, a new result object will be constructed and
returned.For XPath 1.0 results, this object will be of type

XPathResult

.
**Returns:** The result of the evaluation of the XPath expression.For XPath
1.0 results, this object will be of type

XPathResult

.
**Throws:** XPathException

- TYPE_ERR: Raised if the result cannot be converted to return the
specified type.
**Throws:** DOMException

- WRONG_DOCUMENT_ERR: The Node is from a document that is not supported
by the XPathEvaluator that created this

XPathExpression

.

NOT_SUPPORTED_ERR: The Node is not a type permitted as an XPath
context node or the request type is not permitted by this

XPathExpression

.

---

#### Method Detail

evaluate

```java
Object
evaluate​(
Node
contextNode,
short type,

Object
result)
throws
XPathException
,

DOMException
```

Evaluates this XPath expression and returns a result.

**Parameters:** contextNode

- The

context

is context node for the
evaluation of this XPath expression.If the XPathEvaluator was
obtained by casting the

Document

then this must be
owned by the same document and must be a

Document

,

Element

,

Attribute

,

Text

,

CDATASection

,

Comment

,

ProcessingInstruction

, or

XPathNamespace

node.If the context node is a

Text

or a

CDATASection

, then the context is interpreted as the
whole logical text node as seen by XPath, unless the node is empty
in which case it may not serve as the XPath context.
**Parameters:** type

- If a specific

type

is specified, then the
result will be coerced to return the specified type relying on
XPath conversions and fail if the desired coercion is not possible.
This must be one of the type codes of

XPathResult

.
**Parameters:** result

- The

result

specifies a specific result
object which may be reused and returned by this method. If this is
specified as

null

or the implementation does not reuse
the specified result, a new result object will be constructed and
returned.For XPath 1.0 results, this object will be of type

XPathResult

.
**Returns:** The result of the evaluation of the XPath expression.For XPath
1.0 results, this object will be of type

XPathResult

.
**Throws:** XPathException

- TYPE_ERR: Raised if the result cannot be converted to return the
specified type.
**Throws:** DOMException

- WRONG_DOCUMENT_ERR: The Node is from a document that is not supported
by the XPathEvaluator that created this

XPathExpression

.

NOT_SUPPORTED_ERR: The Node is not a type permitted as an XPath
context node or the request type is not permitted by this

XPathExpression

.

---

#### evaluate

Object

evaluate​(

Node

contextNode,
short type,

Object

result)
throws

XPathException

,

DOMException

Evaluates this XPath expression and returns a result.

---

