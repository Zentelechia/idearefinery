def getRecommendationsFunding(projectId):
    tags = getTags(projectId)

    if "Game" in tags:
        return "Patreon"
    elif "Utility" in tags:
        return "Kickstarter"
    else:
        return "Investors"

def getRecommendationsMarketing(ProjectId):
    tags = getTags(ProjectId)
    funding = getFundings(ProjectId)

    MarketingOptions = []

    if "Investor" in funding or "Other" in funding or "GRANT_FUNDED" in funding:
        if "Game" in tags:
            if "Mobile" in tags:
                MarketingOptions.append("Advertise on google play store")
            if "PC" in tags:
                MarketingOptions.append("Advertise on Steam")
        if "Website" in tags and "Service" in tags:
            MarketingOptions.append("Advertise on google search campaign")
            



