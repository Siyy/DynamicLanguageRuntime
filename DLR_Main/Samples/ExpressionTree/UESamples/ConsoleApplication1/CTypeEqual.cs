#if CODEPLEX_40
using System;
#else
using System; using Microsoft;
#endif
using System.Collections.Generic;
#if CODEPLEX_40
using System.Linq;
using System.Linq.Expressions;
#else
using Microsoft.Linq;
using Microsoft.Linq.Expressions;
#endif
using System.Text;

namespace Samples {
    class CTypeEqual {
        //TypeEqual(Expression, Type)
        public static void TypeEqualSample() {
            //<Snippet5>
            //Add the following directive to your file
#if CODEPLEX_40
            //using System.Linq.Expressions;
#else
            //using Microsoft.Linq.Expressions;
#endif

            // Defines a TypeBinaryExpression representing an exact type equality check of the given value and type.
            // Equivalent C#: x.GetType() == T
            Expression Check1 =
                Expression.Condition(
                    Expression.TypeEqual(Expression.Constant(new DivideByZeroException()), typeof(DivideByZeroException)),
                    Expression.Constant(true),
                    Expression.Constant(false)
                );

            Expression Check2 =
                Expression.Condition(
                    Expression.TypeEqual(Expression.Constant(new DivideByZeroException()), typeof(Exception)),
                    Expression.Constant(true),
                    Expression.Constant(false)
                );

            // The first check will return true because TypeEqual's operand matched the type argument exactly.
            Console.WriteLine(Expression.Lambda<Func<bool>>(Check1).Compile().Invoke());
            // The second check will return false because TypeEqual does not check subtype equality, only exact type equality.
            Console.WriteLine(Expression.Lambda<Func<bool>>(Check2).Compile().Invoke());
            //</Snippet5>

            // validate sample
            if (Expression.Lambda<Func<bool>>(Check1).Compile().Invoke() != true ||
                Expression.Lambda<Func<bool>>(Check2).Compile().Invoke() != false)
                throw new Exception("TypeEqualSample failed");
        }
    }
}
