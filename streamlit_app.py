import streamlit as st
from autogen import AssistantAgent
import os

# Set your OpenAI API key using Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["openai_key"]

# Hashtag options per category
hashtags = {
    "PCI": [
        "#BusinessNews", "#naturalskincare", "#Partnership", "#naturalcosmetics", "#personalcare",
        "#dermatology", "#personalcareproducts", "#collagen", "#beautynews", "#acne",
        "#beautyindustry", "#planetaryhealth", "#beautybusiness", "#sustainability", "#beautyproducts",
        "#organicbeauty", "#beautycare", "#cleanbeauty", "#beautytrends", "#greenbeauty",
        "#beautytech", "#animaltesting", "#artificialintelligence", "#crueltyfree", "#makeup",
        "#veganbeauty", "#cosmetics", "#naturalingredients", "#cosmeticsindustry", "#cosmeticingredients",
        "#cosmeticindustry", "#productsafety", "#skin", "#regulations", "#skincare",
        "#ingredients", "#skincareproducts", "#perfume", "#skinhealth", "#fragrance",
        "#healthyskin", "#fragrances", "#sensitiveskin", "#cosmeticpackaging", "#sunscreen",
        "#aroma", "#suncare", "#aromatheraphy", "#beauty", "#antibiotics",
        "#crueltyfreebeauty", "#mensgrooming", "#botanical", "#oralcare", "#dentalhealth",
        "#dentalhygiene"
    ],
    "NI": [
        "#health", "#wellness", "#nutrition", "#organic", "#organicproducts",
        "#ingredients", "#microbiome", "#probiotics", "#prebiotics", "#holistichealth",
        "#protein", "#supplements", "#vitamins", "#infantnutrition", "#immunity",
        "#immunehealth", "#hearthealth", "#bloodpressure", "#obesity", "#diabetes",
        "#guthealth", "#pharmaceuticals", "#nutraceuticals", "#functionalfoods", "#plantbased",
        "#foodsecurity", "#foodinsecurity", "#foodsystems", "#botanicalextracts", "#healthissues",
        "#healthproducts", "#healthcare", "#junkfood", "#childnutrition", "#weightmanagement",
        "#capsules", "#metabolism", "#cardiovascularhealth", "#regulation", "#policy",
        "#innovation", "#mentalhealth", "#government", "#womenshealth", "#healthbenefits",
        "#foodindustry", "#environment", "#climatechange", "#chemicals", "#healthy",
        "#diet", "#sustainable", "#nutritional", "#wellbeing"
    ],
    "PI": [
        "#beveragepackaging", "#packagingtechnology", "#packagingsolutions", "#bioplastic", "#paperindustry",
        "#pharmapackaging", "#bioplastics", "#paperpackaging", "#smartpackaging", "#caps",
        "#plastic", "#biodegradable", "#chemicalrecycling", "#plasticbottles", "#circularpackaging",
        "#chemicals", "#plasticfree", "#ppwr", "#circulareconomy", "#plasticpackaging",
        "#biobasedmaterials", "#climatechange", "#plasticpollution", "#singleuseplastic", "#compostable",
        "#plastics", "#packagingmachinery", "#ecofriendly", "#plasticsindustry", "#plantbased",
        "#ecommerce", "#recycling", "#compostablepackaging", "#environmental", "#renewables",
        "#foodservice", "#environmentallyfriendly", "#reusablepackaging", "#biobased", "#environmentalsustainability",
        "#singleuseplastics", "#foodandbeverage", "#foodpackaging", "#sustainability", "#flexiblepackaging",
        "#foodwaste", "#sustainablepackaging", "#recyclablepackaging", "#globalwarming", "#wastemanagement",
        "#recycled", "#greenenergy", "#zeroplastic", "#greenhousegas", "#reuse",
        "#greenwashing", "#packagingindustry", "#labels", "#paper", "#packaging",
        "#bio", "#packagingdesign", "#packaginginnovation", "#packagingnews"
    ],
    "FIF": [
        "#agriculture", "#agrifood", "#alternativeproteins", "#bakery", "#beverages",
        "#bioscience", "#cleanlabel", "#climatechange", "#confectionery", "#consumertrends",
        "#dairy", "#desserts", "#farming", "#flavors", "#food",
        "#foodandbeverage", "#foodandbeverageindustry", "#foodindustry", "#foodingredients", "#foodinnovation",
        "#foodnews", "#foodsafety", "#foodscience", "#foodsecurity", "#foodtechnology",
        "#foodtrends", "#foodwaste", "#gmo", "#healthyfood", "#marketresearch",
        "#meatalternatives", "#plantbased", "#protein", "#shelflife", "#supplychain",
        "#sustainability", "#sustainablefood", "#sweets", "#taste", "#texture",
        "#vegan"
    ]
}

# Define assistant behavior
agent = AssistantAgent(
    name="analyzer_agent",
    system_message="""
You are an assistant that:
1. Extracts all mentioned people and companies from the article.
2. Selects 3–5 of the most relevant hashtags from the given list based on the article category.
Return the result as JSON with the keys: people, companies, hashtags.
"""
)

# Streamlit UI
st.title("📰 Article Analyzer")

article = st.text_area("Paste the article text here")
category = st.selectbox("Select the article category", ["PCI", "NI", "PI", "FIF"])

if st.button("Analyze") and article:
    tag_list = hashtags.get(category, [])
    message = f"""
Category: {category}
Available hashtags: {', '.join(tag_list)}

Article:
\"\"\"{article}\"\"\"
"""
    with st.spinner("Analyzing..."):
        result = agent.initiate_chat(message=message)
        st.subheader("🔍 Extracted Information")
        st.json(result)
