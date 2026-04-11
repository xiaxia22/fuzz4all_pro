# Interface XPathEvaluator

**Source:** `jdk.xml.dom\org\w3c\dom\xpath\XPathEvaluator.html`

### Class Description

```java
public interface
XPathEvaluator
```

The evaluation of XPath expressions is provided by

XPathEvaluator

. In a DOM implementation which supports the
XPath 3.0 feature, as described above, the

XPathEvaluator

interface will be implemented on the same object which implements the

Document

interface permitting it to be obtained by the usual
binding-specific method such as casting or by using the DOM Level 3
getInterface method. In this case the implementation obtained from the
Document supports the XPath DOM module and is compatible with the XPath
1.0 specification.

Evaluation of expressions with specialized extension functions or
variables may not work in all implementations and is, therefore, not
portable.

XPathEvaluator

implementations may be available
from other sources that could provide specific support for specialized
extension functions or variables as would be defined by other
specifications.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### XPathExpression
createExpression​(
String
expression,

XPathNSResolver
resolver)
throws
XPathException
,

DOMException

Creates a parsed XPath expression with resolved namespaces. This is
useful when an expression will be reused in an application since it
makes it possible to compile the expression string into a more
efficient internal form and preresolve all namespace prefixes which
occur within the expression.

**Parameters:**
- expression

- The XPath expression string to be parsed.
- resolver

- The

resolver

permits translation of
prefixes within the XPath expression into appropriate namespace URIs
. If this is specified as

null

, any namespace prefix
within the expression will result in

DOMException

being thrown with the code

NAMESPACE_ERR

.

**Returns:**
- The compiled form of the XPath expression.

**Throws:**
- XPathException

- INVALID_EXPRESSION_ERR: Raised if the expression is not legal
according to the rules of the

XPathEvaluator

i
- DOMException

- NAMESPACE_ERR: Raised if the expression contains namespace prefixes
which cannot be resolved by the specified

XPathNSResolver

.

---

#### XPathNSResolver
createNSResolver​(
Node
nodeResolver)

Adapts any DOM node to resolve namespaces so that an XPath expression
can be easily evaluated relative to the context of the node where it
appeared within the document. This adapter works like the DOM Level 3
method

lookupNamespaceURI

on nodes in resolving the
namespaceURI from a given prefix using the current information
available in the node's hierarchy at the time lookupNamespaceURI is
called. also correctly resolving the implicit xml prefix.

**Parameters:**
- nodeResolver

- The node to be used as a context for namespace
resolution.

**Returns:**
- XPathNSResolver

which resolves namespaces with
respect to the definitions in scope for a specified node.

---

#### Object
evaluate​(
String
expression,

Node
contextNode,

XPathNSResolver
resolver,
short type,

Object
result)
throws
XPathException
,

DOMException

Evaluates an XPath expression string and returns a result of the
specified type if possible.

**Parameters:**
- expression

- The XPath expression string to be parsed and
evaluated.
- contextNode

- The

context

is context node for the
evaluation of this XPath expression. If the XPathEvaluator was
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

node. If the context node is a

Text

or a

CDATASection

, then the context is interpreted as the
whole logical text node as seen by XPath, unless the node is empty
in which case it may not serve as the XPath context.
- resolver

- The

resolver

permits translation of
prefixes within the XPath expression into appropriate namespace URIs
. If this is specified as

null

, any namespace prefix
within the expression will result in

DOMException

being thrown with the code

NAMESPACE_ERR

.
- type

- If a specific

type

is specified, then the
result will be returned as the corresponding type.For XPath 1.0
results, this must be one of the codes of the

XPathResult

interface.
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

- INVALID_EXPRESSION_ERR: Raised if the expression is not legal
according to the rules of the

XPathEvaluator

i

TYPE_ERR: Raised if the result cannot be converted to return the
specified type.
- DOMException

- NAMESPACE_ERR: Raised if the expression contains namespace prefixes
which cannot be resolved by the specified

XPathNSResolver

.

WRONG_DOCUMENT_ERR: The Node is from a document that is not
supported by this

XPathEvaluator

.

NOT_SUPPORTED_ERR: The Node is not a type permitted as an XPath
context node or the request type is not permitted by this

XPathEvaluator

.

---

### Additional Sections

#### Interface XPathEvaluator

```java
public interface
XPathEvaluator
```

The evaluation of XPath expressions is provided by

XPathEvaluator

. In a DOM implementation which supports the
XPath 3.0 feature, as described above, the

XPathEvaluator

interface will be implemented on the same object which implements the

Document

interface permitting it to be obtained by the usual
binding-specific method such as casting or by using the DOM Level 3
getInterface method. In this case the implementation obtained from the
Document supports the XPath DOM module and is compatible with the XPath
1.0 specification.

Evaluation of expressions with specialized extension functions or
variables may not work in all implementations and is, therefore, not
portable.

XPathEvaluator

implementations may be available
from other sources that could provide specific support for specialized
extension functions or variables as would be defined by other
specifications.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

public interface

XPathEvaluator

The evaluation of XPath expressions is provided by

XPathEvaluator

. In a DOM implementation which supports the
XPath 3.0 feature, as described above, the

XPathEvaluator

interface will be implemented on the same object which implements the

Document

interface permitting it to be obtained by the usual
binding-specific method such as casting or by using the DOM Level 3
getInterface method. In this case the implementation obtained from the
Document supports the XPath DOM module and is compatible with the XPath
1.0 specification.

Evaluation of expressions with specialized extension functions or
variables may not work in all implementations and is, therefore, not
portable.

XPathEvaluator

implementations may be available
from other sources that could provide specific support for specialized
extension functions or variables as would be defined by other
specifications.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

Evaluation of expressions with specialized extension functions or
variables may not work in all implementations and is, therefore, not
portable.

XPathEvaluator

implementations may be available
from other sources that could provide specific support for specialized
extension functions or variables as would be defined by other
specifications.

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

XPathExpression

createExpression

​(

String

expression,

XPathNSResolver

resolver)

Creates a parsed XPath expression with resolved namespaces.

XPathNSResolver

createNSResolver

​(

Node

nodeResolver)

Adapts any DOM node to resolve namespaces so that an XPath expression
can be easily evaluated relative to the context of the node where it
appeared within the document.

Object

evaluate

​(

String

expression,

Node

contextNode,

XPathNSResolver

resolver,
short type,

Object

result)

Evaluates an XPath expression string and returns a result of the
specified type if possible.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

XPathExpression

createExpression

​(

String

expression,

XPathNSResolver

resolver)

Creates a parsed XPath expression with resolved namespaces.

XPathNSResolver

createNSResolver

​(

Node

nodeResolver)

Adapts any DOM node to resolve namespaces so that an XPath expression
can be easily evaluated relative to the context of the node where it
appeared within the document.

Object

evaluate

​(

String

expression,

Node

contextNode,

XPathNSResolver

resolver,
short type,

Object

result)

Evaluates an XPath expression string and returns a result of the
specified type if possible.

---

#### Method Summary

Creates a parsed XPath expression with resolved namespaces.

Adapts any DOM node to resolve namespaces so that an XPath expression
can be easily evaluated relative to the context of the node where it
appeared within the document.

Evaluates an XPath expression string and returns a result of the
specified type if possible.

============ METHOD DETAIL ==========

- Method Detail

- createExpression

```java
XPathExpression
createExpression​(
String
expression,

XPathNSResolver
resolver)
throws
XPathException
,

DOMException
```

Creates a parsed XPath expression with resolved namespaces. This is
useful when an expression will be reused in an application since it
makes it possible to compile the expression string into a more
efficient internal form and preresolve all namespace prefixes which
occur within the expression.

**Parameters:** expression

- The XPath expression string to be parsed.
**Parameters:** resolver

- The

resolver

permits translation of
prefixes within the XPath expression into appropriate namespace URIs
. If this is specified as

null

, any namespace prefix
within the expression will result in

DOMException

being thrown with the code

NAMESPACE_ERR

.
**Returns:** The compiled form of the XPath expression.
**Throws:** XPathException

- INVALID_EXPRESSION_ERR: Raised if the expression is not legal
according to the rules of the

XPathEvaluator

i
**Throws:** DOMException

- NAMESPACE_ERR: Raised if the expression contains namespace prefixes
which cannot be resolved by the specified

XPathNSResolver

.

- createNSResolver

```java
XPathNSResolver
createNSResolver​(
Node
nodeResolver)
```

Adapts any DOM node to resolve namespaces so that an XPath expression
can be easily evaluated relative to the context of the node where it
appeared within the document. This adapter works like the DOM Level 3
method

lookupNamespaceURI

on nodes in resolving the
namespaceURI from a given prefix using the current information
available in the node's hierarchy at the time lookupNamespaceURI is
called. also correctly resolving the implicit xml prefix.

**Parameters:** nodeResolver

- The node to be used as a context for namespace
resolution.
**Returns:** XPathNSResolver

which resolves namespaces with
respect to the definitions in scope for a specified node.

- evaluate

```java
Object
evaluate​(
String
expression,

Node
contextNode,

XPathNSResolver
resolver,
short type,

Object
result)
throws
XPathException
,

DOMException
```

Evaluates an XPath expression string and returns a result of the
specified type if possible.

**Parameters:** expression

- The XPath expression string to be parsed and
evaluated.
**Parameters:** contextNode

- The

context

is context node for the
evaluation of this XPath expression. If the XPathEvaluator was
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

node. If the context node is a

Text

or a

CDATASection

, then the context is interpreted as the
whole logical text node as seen by XPath, unless the node is empty
in which case it may not serve as the XPath context.
**Parameters:** resolver

- The

resolver

permits translation of
prefixes within the XPath expression into appropriate namespace URIs
. If this is specified as

null

, any namespace prefix
within the expression will result in

DOMException

being thrown with the code

NAMESPACE_ERR

.
**Parameters:** type

- If a specific

type

is specified, then the
result will be returned as the corresponding type.For XPath 1.0
results, this must be one of the codes of the

XPathResult

interface.
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

- INVALID_EXPRESSION_ERR: Raised if the expression is not legal
according to the rules of the

XPathEvaluator

i

TYPE_ERR: Raised if the result cannot be converted to return the
specified type.
**Throws:** DOMException

- NAMESPACE_ERR: Raised if the expression contains namespace prefixes
which cannot be resolved by the specified

XPathNSResolver

.

WRONG_DOCUMENT_ERR: The Node is from a document that is not
supported by this

XPathEvaluator

.

NOT_SUPPORTED_ERR: The Node is not a type permitted as an XPath
context node or the request type is not permitted by this

XPathEvaluator

.

Method Detail

- createExpression

```java
XPathExpression
createExpression​(
String
expression,

XPathNSResolver
resolver)
throws
XPathException
,

DOMException
```

Creates a parsed XPath expression with resolved namespaces. This is
useful when an expression will be reused in an application since it
makes it possible to compile the expression string into a more
efficient internal form and preresolve all namespace prefixes which
occur within the expression.

**Parameters:** expression

- The XPath expression string to be parsed.
**Parameters:** resolver

- The

resolver

permits translation of
prefixes within the XPath expression into appropriate namespace URIs
. If this is specified as

null

, any namespace prefix
within the expression will result in

DOMException

being thrown with the code

NAMESPACE_ERR

.
**Returns:** The compiled form of the XPath expression.
**Throws:** XPathException

- INVALID_EXPRESSION_ERR: Raised if the expression is not legal
according to the rules of the

XPathEvaluator

i
**Throws:** DOMException

- NAMESPACE_ERR: Raised if the expression contains namespace prefixes
which cannot be resolved by the specified

XPathNSResolver

.

- createNSResolver

```java
XPathNSResolver
createNSResolver​(
Node
nodeResolver)
```

Adapts any DOM node to resolve namespaces so that an XPath expression
can be easily evaluated relative to the context of the node where it
appeared within the document. This adapter works like the DOM Level 3
method

lookupNamespaceURI

on nodes in resolving the
namespaceURI from a given prefix using the current information
available in the node's hierarchy at the time lookupNamespaceURI is
called. also correctly resolving the implicit xml prefix.

**Parameters:** nodeResolver

- The node to be used as a context for namespace
resolution.
**Returns:** XPathNSResolver

which resolves namespaces with
respect to the definitions in scope for a specified node.

- evaluate

```java
Object
evaluate​(
String
expression,

Node
contextNode,

XPathNSResolver
resolver,
short type,

Object
result)
throws
XPathException
,

DOMException
```

Evaluates an XPath expression string and returns a result of the
specified type if possible.

**Parameters:** expression

- The XPath expression string to be parsed and
evaluated.
**Parameters:** contextNode

- The

context

is context node for the
evaluation of this XPath expression. If the XPathEvaluator was
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

node. If the context node is a

Text

or a

CDATASection

, then the context is interpreted as the
whole logical text node as seen by XPath, unless the node is empty
in which case it may not serve as the XPath context.
**Parameters:** resolver

- The

resolver

permits translation of
prefixes within the XPath expression into appropriate namespace URIs
. If this is specified as

null

, any namespace prefix
within the expression will result in

DOMException

being thrown with the code

NAMESPACE_ERR

.
**Parameters:** type

- If a specific

type

is specified, then the
result will be returned as the corresponding type.For XPath 1.0
results, this must be one of the codes of the

XPathResult

interface.
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

- INVALID_EXPRESSION_ERR: Raised if the expression is not legal
according to the rules of the

XPathEvaluator

i

TYPE_ERR: Raised if the result cannot be converted to return the
specified type.
**Throws:** DOMException

- NAMESPACE_ERR: Raised if the expression contains namespace prefixes
which cannot be resolved by the specified

XPathNSResolver

.

WRONG_DOCUMENT_ERR: The Node is from a document that is not
supported by this

XPathEvaluator

.

NOT_SUPPORTED_ERR: The Node is not a type permitted as an XPath
context node or the request type is not permitted by this

XPathEvaluator

.

---

#### Method Detail

createExpression

```java
XPathExpression
createExpression​(
String
expression,

XPathNSResolver
resolver)
throws
XPathException
,

DOMException
```

Creates a parsed XPath expression with resolved namespaces. This is
useful when an expression will be reused in an application since it
makes it possible to compile the expression string into a more
efficient internal form and preresolve all namespace prefixes which
occur within the expression.

**Parameters:** expression

- The XPath expression string to be parsed.
**Parameters:** resolver

- The

resolver

permits translation of
prefixes within the XPath expression into appropriate namespace URIs
. If this is specified as

null

, any namespace prefix
within the expression will result in

DOMException

being thrown with the code

NAMESPACE_ERR

.
**Returns:** The compiled form of the XPath expression.
**Throws:** XPathException

- INVALID_EXPRESSION_ERR: Raised if the expression is not legal
according to the rules of the

XPathEvaluator

i
**Throws:** DOMException

- NAMESPACE_ERR: Raised if the expression contains namespace prefixes
which cannot be resolved by the specified

XPathNSResolver

.

---

#### createExpression

XPathExpression

createExpression​(

String

expression,

XPathNSResolver

resolver)
throws

XPathException

,

DOMException

Creates a parsed XPath expression with resolved namespaces. This is
useful when an expression will be reused in an application since it
makes it possible to compile the expression string into a more
efficient internal form and preresolve all namespace prefixes which
occur within the expression.

createNSResolver

```java
XPathNSResolver
createNSResolver​(
Node
nodeResolver)
```

Adapts any DOM node to resolve namespaces so that an XPath expression
can be easily evaluated relative to the context of the node where it
appeared within the document. This adapter works like the DOM Level 3
method

lookupNamespaceURI

on nodes in resolving the
namespaceURI from a given prefix using the current information
available in the node's hierarchy at the time lookupNamespaceURI is
called. also correctly resolving the implicit xml prefix.

**Parameters:** nodeResolver

- The node to be used as a context for namespace
resolution.
**Returns:** XPathNSResolver

which resolves namespaces with
respect to the definitions in scope for a specified node.

---

#### createNSResolver

XPathNSResolver

createNSResolver​(

Node

nodeResolver)

Adapts any DOM node to resolve namespaces so that an XPath expression
can be easily evaluated relative to the context of the node where it
appeared within the document. This adapter works like the DOM Level 3
method

lookupNamespaceURI

on nodes in resolving the
namespaceURI from a given prefix using the current information
available in the node's hierarchy at the time lookupNamespaceURI is
called. also correctly resolving the implicit xml prefix.

evaluate

```java
Object
evaluate​(
String
expression,

Node
contextNode,

XPathNSResolver
resolver,
short type,

Object
result)
throws
XPathException
,

DOMException
```

Evaluates an XPath expression string and returns a result of the
specified type if possible.

**Parameters:** expression

- The XPath expression string to be parsed and
evaluated.
**Parameters:** contextNode

- The

context

is context node for the
evaluation of this XPath expression. If the XPathEvaluator was
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

node. If the context node is a

Text

or a

CDATASection

, then the context is interpreted as the
whole logical text node as seen by XPath, unless the node is empty
in which case it may not serve as the XPath context.
**Parameters:** resolver

- The

resolver

permits translation of
prefixes within the XPath expression into appropriate namespace URIs
. If this is specified as

null

, any namespace prefix
within the expression will result in

DOMException

being thrown with the code

NAMESPACE_ERR

.
**Parameters:** type

- If a specific

type

is specified, then the
result will be returned as the corresponding type.For XPath 1.0
results, this must be one of the codes of the

XPathResult

interface.
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

- INVALID_EXPRESSION_ERR: Raised if the expression is not legal
according to the rules of the

XPathEvaluator

i

TYPE_ERR: Raised if the result cannot be converted to return the
specified type.
**Throws:** DOMException

- NAMESPACE_ERR: Raised if the expression contains namespace prefixes
which cannot be resolved by the specified

XPathNSResolver

.

WRONG_DOCUMENT_ERR: The Node is from a document that is not
supported by this

XPathEvaluator

.

NOT_SUPPORTED_ERR: The Node is not a type permitted as an XPath
context node or the request type is not permitted by this

XPathEvaluator

.

---

#### evaluate

Object

evaluate​(

String

expression,

Node

contextNode,

XPathNSResolver

resolver,
short type,

Object

result)
throws

XPathException

,

DOMException

Evaluates an XPath expression string and returns a result of the
specified type if possible.

---

