PAYLOAD = {
    "query": """
            query GetSubcategoryProductsFilter($subcategoryProductsFilterInput:CatalogFilter_ProductsFilterInput!,$categoryFilterInput:Catalog_CategoryFilterInput!,$categoryCompilationFilterInput:Catalog_CategoryCompilationFilterInput!){
                productsFilter(filter:$subcategoryProductsFilterInput){
                    record{...SubcategoryProductsFilter},
                    error{
                        ... on CatalogFilter_ProductsFilterInternalError{__typename,message},
                        ... on CatalogFilter_ProductsFilterIncorrectArgumentsError{__typename,message}
                    }
                },
                category(filter:$categoryFilterInput){...SubcategoryCategoryInfo}
            }
            fragment SubcategoryProductsFilter on CatalogFilter_ProductsFilter{
                __typename,
                products{...ProductSnippetFull},
                sortings{id,name,slug,directions{id,isSelected,name,slug,isDefault}},
                groups{...SubcategoryProductsFilterGroup},
                compilations{popular{...SubcategoryProductCompilationInfo},brands{...SubcategoryProductCompilationInfo},carousel{...SubcategoryProductCompilationInfo}},
                pageInfo{...Pagination},
                searchStrategy
            }
            fragment ProductSnippetFull on Catalog_Product{...ProductSnippetShort,propertiesShort{...ProductProperty},rating,counters{opinions,reviews}}
            fragment ProductSnippetShort on Catalog_Product{...ProductSnippetBase,labels{...ProductLabel},delivery{__typename,self{__typename,availabilityByDays{__typename,deliveryTime,storeCount},availableInFavoriteStores{store{id,shortName},productsCount}}},stock{countInStores,maxCountInStock},yandexPay{withYandexSplit}}
            fragment ProductSnippetBase on Catalog_Product{id,name,shortName,slug,isAvailable,images{citilink{...Image}},price{...ProductPrice},category{id,name},brand{name},multiplicity,quantityInPackageFromSupplier}
            fragment Image on Image{sources{url,size}}
            fragment ProductPrice on Catalog_ProductPrice{current,old,club,clubPriceViewType,discount{percent}}
            fragment ProductLabel on Catalog_Label{id,type,title,description,target{...Target},textColor,backgroundColor,expirationTime}
            fragment Target on Catalog_Target{action{...TargetAction},url,inNewWindow}
            fragment TargetAction on Catalog_TargetAction{id}
            fragment ProductProperty on Catalog_Property{name,value}
            fragment SubcategoryProductsFilterGroup on CatalogFilter_FilterGroup{id,isCollapsed,isDisabled,name,description,filter{... on CatalogFilter_ListFilter{__typename,isSearchable,logic,filters{id,isDisabled,isInShortList,isInTagList,isSelected,name,total,childGroups{id,isCollapsed,isDisabled,name,filter{... on CatalogFilter_ListFilter{__typename,isSearchable,logic,filters{id,isDisabled,isInShortList,isInTagList,name,isSelected,total}},... on CatalogFilter_RangeFilter{__typename,fromValue,isInTagList,maxValue,minValue,serifValues,scaleStep,toValue,unit}}}}},... on CatalogFilter_RangeFilter{__typename,fromValue,isInTagList,maxValue,minValue,serifValues,scaleStep,toValue,unit}}}
            fragment SubcategoryProductCompilationInfo on CatalogFilter_CompilationInfo{__typename,compilation{...SubcategoryProductCompilation},isSelected}
            fragment SubcategoryProductCompilation on Catalog_ProductCompilation{__typename,id,type,name,slug,parentSlug,seo{h1,title,text,description}}
            fragment Pagination on PageInfo{hasNextPage,hasPreviousPage,perPage,page,totalItems,totalPages}
            fragment SubcategoryCategoryInfo on Catalog_CategoryResult{... on Catalog_Category{...Category,seo{h1,title,text,description},compilation(filter:$categoryCompilationFilterInput){... on Catalog_CategoryCompilation{__typename,id,name,seo{h1,title,description,text}},... on Catalog_CategoryCompilationIncorrectArgumentError{__typename,message},... on Catalog_CategoryCompilationNotFoundError{__typename,message}},defaultSnippetType},... on Catalog_CategoryIncorrectArgumentError{__typename,message},... on Catalog_CategoryNotFoundError{__typename,message}}
            fragment Category on Catalog_Category{__typename,id,name,slug}
        """,
    "variables": {
        "subcategoryProductsFilterInput": {
            "categorySlug": "processory",
            "compilationPath": [],
            "pagination": {"page": 1, "perPage": 1000},
            "conditions": [],
            "sorting": {"id": "price", "direction": "SORT_DIRECTION_DESC"},
            "popularitySegmentId": "THREE",
        },
        "categoryFilterInput": {"slug": "processory"},
        "categoryCompilationFilterInput": {"slug": ""},
    },
}
